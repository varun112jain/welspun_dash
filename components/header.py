"""
Header Component for Welspun Dashboard
"""
import os
import base64
import streamlit as st

def get_welspun_logo_b64():
    """Returns base64 encoded Welspun white logo for zero-latency header rendering."""
    logo_path = os.path.join(os.path.dirname(__file__), "..", "assets", "welspun_full_logo_dark.png")
    if os.path.exists(logo_path):
        with open(logo_path, "rb") as f:
            return base64.b64encode(f.read()).decode("utf-8")
    return None

def render_welspun_header(
    title: str = "Welspun Command & Control Centre (ICCC)",
    subtitle: str = "24/7 AI Multi-Screen CCTV Surveillance, Fire Network & Safety Intelligence • Welspun City, Anjar",
    badge_text: str = "LIVE DEFENSE MESH",
    days_incident_free: int = 148,
    online_cameras: int = 1424,
    total_cameras: int = 1438
):
    """Renders a polished Welspun header banner with compact typography and unsquashed stat tiles."""
    uptime_pct = (online_cameras / total_cameras) * 100
    logo_b64 = get_welspun_logo_b64()
    logo_html = f'<img src="data:image/png;base64,{logo_b64}" style="height:32px; width:auto; max-width:120px; object-fit:contain; flex-shrink:0;" alt="WELSPUN" />' if logo_b64 else '<span style="font-size:1.25rem; font-weight:800; letter-spacing:0.04em; color:#FFFFFF; flex-shrink:0;">WELSPUN</span>'

    st.html(
        f"""
        <div class="welspun-header-card">
            <div style="display:flex; align-items:center; gap:14px; min-width:0; flex-shrink:1;">
                {logo_html}
                <div style="border-left: 2px solid rgba(255,255,255,0.25); padding-left: 12px; min-width:0;">
                    <div style="font-size:0.68rem; font-weight:700; letter-spacing:0.1em; color:#38BDF8; margin-bottom:2px; text-transform:uppercase;">
                        WELSPUN GROUP • ANJAR MEGA COMPLEX
                    </div>
                    <h1 class="welspun-header-title">{title}</h1>
                    <p class="welspun-header-subtitle">{subtitle}</p>
                </div>
            </div>
            <div style="display:flex; flex-direction:row; align-items:center; gap:10px; flex-shrink:0;">
                <div class="welspun-header-stat">
                    <span style="font-size:0.65rem; color:#BAE6FD; text-transform:uppercase; letter-spacing:0.04em; font-weight:600;">Active CCTV Feeds</span><br>
                    <b style="font-size:0.95rem; color:#FFFFFF;">{online_cameras:,} <span style="font-size:0.75rem; color:#94A3B8;">/ {total_cameras:,}</span> <span style="color:#34D399; font-size:0.78rem;">({uptime_pct:.1f}%)</span></b>
                </div>
                <div class="welspun-header-stat">
                    <span style="font-size:0.65rem; color:#BAE6FD; text-transform:uppercase; letter-spacing:0.04em; font-weight:600;">Incident-Free Streak</span><br>
                    <b style="font-size:0.95rem; color:#34D399;">{days_incident_free} DAYS</b>
                </div>
                <div class="welspun-badge" style="flex-shrink:0;">
                    <span class="pulse-dot-green"></span>
                    {badge_text}
                </div>
            </div>
        </div>
        """
    )
