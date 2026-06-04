import React from 'react';
import { AttackVector } from '../../types';

// ==================== VectorLike Type ====================

export type VectorLike = Pick<AttackVector, 'id' | 'from' | 'fromLat' | 'fromLng' | 'to' | 'toLat' | 'toLng' | 'attackType' | 'severity' | 'sourceIp' | 'isp' | 'org' | 'source' | 'malware'>;

// ==================== Country Flag Mapping ====================

const COUNTRY_FLAGS: Record<string, string> = {
  'Pakistan': '🇵🇰',
  'China': '🇨🇳',
  'North Korea': '🇰🇵',
  'Russia': '🇷🇺',
  'Iran': '🇮🇷',
  'USA': '🇺🇸',
  'India': '🇮🇳',
  'Unknown': '🏴',
};

// ==================== Vector Detail Modal ====================

export function VectorDetailModal({ vector, onClose }: { vector: VectorLike | null; onClose: () => void }) {
  if (!vector) return null;

  const severityColor = vector.severity === 'critical' ? 'var(--accent-red)' : vector.severity === 'medium' ? 'var(--accent-yellow)' : 'var(--accent-green)';

  const copyToClipboard = async (text: string) => {
    try {
      await navigator.clipboard.writeText(text);
    } catch {
      // Fallback for non-HTTPS
      const ta = document.createElement('textarea');
      ta.value = text;
      document.body.appendChild(ta);
      ta.select();
      document.execCommand('copy');
      document.body.removeChild(ta);
    }
  };

  const reportUrls = {
    abuseCh: vector.sourceIp ? `https://threatfox.abuse.ch/browse.php?search=${vector.sourceIp}` : '#',
    certIn: 'https://www.cert-in.org.in/reporting',
    alienVault: vector.sourceIp ? `https://otx.alienvault.com/browse/global/pulses?q=${vector.sourceIp}` : '#',
  };

  return (
    <div className="vector-detail-overlay" onClick={onClose}>
      <div className="vector-detail-modal" onClick={e => e.stopPropagation()}>
        {/* Header */}
        <div className="vd-header">
          <div className="vd-header-left">
            <span className="vd-header-icon">🛡️</span>
            <div>
              <div className="vd-header-title">Attack Vector Details</div>
              <div className="vd-header-id">ID: {vector.id}</div>
            </div>
          </div>
          <button className="vd-close-btn" onClick={onClose}>✕</button>
        </div>

        <div className="vd-body">
          {/* IP Info Card */}
          <div className="vd-card vd-card-ip">
            <div className="vd-card-header">SOURCE IP</div>
            <div className="vd-ip-display">
              <code className="vd-ip-value">{vector.sourceIp || 'N/A'}</code>
              {vector.sourceIp && (
                <button className="vd-copy-btn" onClick={() => copyToClipboard(vector.sourceIp!)} title="Copy IP">
                  📋 Copy
                </button>
              )}
            </div>
            <div className="vd-meta-grid">
              <div className="vd-meta-item">
                <span className="vd-meta-label">ISP</span>
                <span className="vd-meta-value">{vector.isp || 'Unknown'}</span>
              </div>
              <div className="vd-meta-item">
                <span className="vd-meta-label">Organization</span>
                <span className="vd-meta-value">{vector.org || 'N/A'}</span>
              </div>
            </div>
          </div>

          {/* Attack Info Card */}
          <div className="vd-card">
            <div className="vd-card-header">ATTACK ROUTE</div>
            <div className="vd-route-display">
              <div className="vd-route-origin">
                <span className="vd-route-flag">{COUNTRY_FLAGS[vector.from] || '🏴'}</span>
                <div>
                  <div className="vd-route-label">Origin</div>
                  <div className="vd-route-value">{vector.from}</div>
                </div>
              </div>
              <span className="vd-route-arrow">→</span>
              <div className="vd-route-target">
                <div>
                  <div className="vd-route-label">Target</div>
                  <div className="vd-route-value">{vector.to}</div>
                </div>
              </div>
            </div>
          </div>

          {/* Classification Card */}
          <div className="vd-card">
            <div className="vd-card-header">CLASSIFICATION</div>
            <div className="vd-classification-row">
              <div className="vd-class-item">
                <span className="vd-meta-label">Attack Type</span>
                <span className="vd-class-badge type">{vector.attackType}</span>
              </div>
              <div className="vd-class-item">
                <span className="vd-meta-label">Severity</span>
                <span className={`vd-class-badge severity ${vector.severity}`} style={{ background: `${severityColor}18`, color: severityColor, border: `1px solid ${severityColor}30` }}>
                  {vector.severity.toUpperCase()}
                </span>
              </div>
            </div>
            {(vector.malware || vector.source) && (
              <div className="vd-classification-row" style={{ marginTop: 8 }}>
                {vector.malware && (
                  <div className="vd-class-item">
                    <span className="vd-meta-label">Malware</span>
                    <span className="vd-class-badge" style={{ background: 'rgba(249, 115, 22, 0.08)', color: 'var(--accent-orange)', border: '1px solid rgba(249, 115, 22, 0.15)' }}>
                      {vector.malware}
                    </span>
                  </div>
                )}
                {vector.source && (
                  <div className="vd-class-item">
                    <span className="vd-meta-label">Source Feed</span>
                    <span className="vd-class-badge" style={{ background: vector.source === 'ThreatFox' ? 'rgba(139, 92, 246, 0.08)' : vector.source === 'Feodo' ? 'rgba(6, 182, 212, 0.08)' : 'rgba(100, 116, 139, 0.08)', color: vector.source === 'ThreatFox' ? 'var(--accent-purple)' : vector.source === 'Feodo' ? 'var(--accent-cyan)' : 'var(--text-secondary)', border: `1px solid ${vector.source === 'ThreatFox' ? 'rgba(139, 92, 246, 0.15)' : vector.source === 'Feodo' ? 'rgba(6, 182, 212, 0.15)' : 'rgba(100, 116, 139, 0.15)'}` }}>
                      {vector.source}
                    </span>
                  </div>
                )}
              </div>
            )}
          </div>

          {/* Target City Note */}
          <div className="vd-card" style={{ borderColor: 'rgba(234, 179, 8, 0.15)', background: 'rgba(234, 179, 8, 0.02)' }}>
            <div className="vd-card-header">⚠️ DATA NOTE</div>
            <p style={{ fontSize: 10, color: 'var(--text-secondary)', lineHeight: 1.5, margin: 0 }}>
              The source IP and geo-location are <strong style={{color:'var(--accent-green)'}}>real</strong> (from {vector.source || 'threat intel feeds'}).
              The attack type and severity are based on real feed classifications. The target city is assigned
              for visualization purposes — actual victim data is not available from these feeds.
            </p>
          </div>

          {/* Report Actions */}
          <div className="vd-card vd-card-actions">
            <div className="vd-card-header">REPORT THIS THREAT</div>
            <p className="vd-actions-desc">Submit this malicious IP to threat intelligence platforms:</p>
            <div className="vd-actions-grid">
              <a href={reportUrls.abuseCh} target="_blank" rel="noopener noreferrer" className={`vd-action-btn ${!vector.sourceIp ? 'disabled' : ''}`}>
                <span className="vd-action-icon">🦊</span>
                <div className="vd-action-text">
                  <span className="vd-action-name">Abuse.ch ThreatFox</span>
                  <span className="vd-action-desc">Submit to malware IOC database</span>
                </div>
              </a>
              <a href={reportUrls.alienVault} target="_blank" rel="noopener noreferrer" className={`vd-action-btn ${!vector.sourceIp ? 'disabled' : ''}`}>
                <span className="vd-action-icon">👾</span>
                <div className="vd-action-text">
                  <span className="vd-action-name">AlienVault OTX</span>
                  <span className="vd-action-desc">Open Threat Exchange pulse</span>
                </div>
              </a>
              <a href={reportUrls.certIn} target="_blank" rel="noopener noreferrer" className="vd-action-btn">
                <span className="vd-action-icon">🇮🇳</span>
                <div className="vd-action-text">
                  <span className="vd-action-name">CERT-In</span>
                  <span className="vd-action-desc">Indian CERT reporting portal</span>
                </div>
              </a>
              <button className="vd-action-btn vd-action-copy" onClick={() => copyToClipboard(JSON.stringify({
                ip: vector.sourceIp,
                country: vector.from,
                attackType: vector.attackType,
                severity: vector.severity,
                target: vector.to,
                isp: vector.isp,
                org: vector.org,
              }, null, 2))}>
                <span className="vd-action-icon">📋</span>
                <div className="vd-action-text">
                  <span className="vd-action-name">Copy JSON Report</span>
                  <span className="vd-action-desc">Raw intelligence data</span>
                </div>
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
