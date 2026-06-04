import { useRef, useCallback, useEffect } from 'react';

// ==================== Types ====================

export interface ThreatAttackVector {
  type: 'attack_vector';
  id: string;
  from: string;
  fromLat: number;
  fromLng: number;
  to: string;
  toLat: number;
  toLng: number;
  attackType: string;
  severity: 'critical' | 'medium' | 'safe';
  sourceIp?: string;
  isp?: string;
  org?: string;
  source?: string;      // Which threat feed: ThreatFox, Feodo, IPsum
  malware?: string;     // Real malware family name from feed
  timestamp: string;
}

export interface ThreatTickerEvent {
  type: 'threat_event' | 'news_event';
  id: string;
  severity: 'critical' | 'medium' | 'safe';
  text: string;
  icon: string;
  source?: string;
  city?: string;
  attackType?: string;
  url?: string;
  timestamp: string;
}

export interface ThreatInitialState {
  type: 'initial_state';
  events: (ThreatAttackVector | ThreatTickerEvent)[];
  cities: Array<{
    name: string;
    lat: number;
    lng: number;
    risk: string;
    assetCount: number;
    activeThreats: number;
  }>;
  timestamp: string;
}

export type ThreatFeedMessage =
  | ThreatInitialState
  | ThreatAttackVector
  | ThreatTickerEvent;

interface UseThreatFeedOptions {
  onAttackVector?: (vector: ThreatAttackVector) => void;
  onThreatEvent?: (event: ThreatTickerEvent) => void;
  onInitialState?: (state: ThreatInitialState) => void;
  onError?: (error: Event) => void;
}

function getWebSocketBase(): string {
  const protocol = window.location.protocol === 'https:' ? 'wss:' : 'ws:';
  return `${protocol}//${window.location.host}`;
}

/**
 * Custom hook that manages a WebSocket connection to the live threat feed.
 *
 * Streams real-time attack vectors, threat events, and news headlines
 * for the interactive map and ticker.
 */
export function useThreatFeed(options: UseThreatFeedOptions) {
  const wsRef = useRef<WebSocket | null>(null);
  const reconnectTimerRef = useRef<ReturnType<typeof setTimeout> | null>(null);
  const optionsRef = useRef(options);
  optionsRef.current = options;

  const cleanup = useCallback(() => {
    if (reconnectTimerRef.current) {
      clearTimeout(reconnectTimerRef.current);
      reconnectTimerRef.current = null;
    }
    if (wsRef.current) {
      wsRef.current.close();
      wsRef.current = null;
    }
  }, []);

  // Cleanup on unmount
  useEffect(() => {
    return () => cleanup();
  }, [cleanup]);

  const connect = useCallback(() => {
    cleanup();

    const ws = new WebSocket(`${getWebSocketBase()}/ws/threats`);
    wsRef.current = ws;

    ws.onopen = () => {
      // Connected to live threat stream
    };

    ws.onmessage = (event) => {
      try {
        const msg: ThreatFeedMessage = JSON.parse(event.data);

        switch (msg.type) {
          case 'initial_state':
            optionsRef.current.onInitialState?.(msg);
            break;
          case 'attack_vector':
            optionsRef.current.onAttackVector?.(msg);
            break;
          case 'threat_event':
          case 'news_event':
            optionsRef.current.onThreatEvent?.(msg);
            break;
        }
      } catch (err) {
        console.error('[ThreatFeed] Failed to parse message:', err);
      }
    };

    ws.onerror = (event) => {
      console.error('[ThreatFeed] WebSocket error:', event);
      optionsRef.current.onError?.(event);
    };

    ws.onclose = () => {
      // Disconnected, reconnecting in 3s...
      wsRef.current = null;
      // Auto-reconnect after 3 seconds
      reconnectTimerRef.current = setTimeout(() => {
        connect();
      }, 3000);
    };
  }, [cleanup]);

  const disconnect = useCallback(() => {
    if (reconnectTimerRef.current) {
      clearTimeout(reconnectTimerRef.current);
      reconnectTimerRef.current = null;
    }
    if (wsRef.current) {
      wsRef.current.close();
      wsRef.current = null;
    }
  }, []);

  return { connect, disconnect };
}
