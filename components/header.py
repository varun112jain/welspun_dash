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
    title: str = "Welspun Integrated Command & Control Centre",
    subtitle: str = "24/7 AI Multi-Screen CCTV Surveillance, Fire Network & Safety Intelligence • Anjar Complex",
    badge_text: str = "LIVE DEFENSE MESH",
    days_incident_free: int = 148,
    online_cameras: int = 1424,
    total_cameras: int = 1438
):
    """Renders a polished Welspun header banner with corporate branding, cameras uptime, and incident milestone."""
    uptime_pct = (online_cameras / total_cameras) * 100
    logo_b64 = get_welspun_logo_b64()
    logo_html = f'<img src="data:image/png;base64,{logo_b64}" style="height:46px; width:auto; max-width:210px; object-fit:contain;" alt="WELSPUN" />' if logo_b64 else '<span style="font-size:1.8rem; font-weight:800; letter-spacing:0.04em; color:#FFFFFF;">WELSPUN</span>'

    st.markdown(
        f"""
        <div class="welspun-header-card">
            <div style="display:flex; align-items:center; gap:22px; flex-wrap:wrap;">
                {logo_html}
                <div style="border-left: 2px solid rgba(255,255,255,0.25); padding-left: 18px;">
                    <div style="font-size:0.72rem; font-weight:700; letter-spacing:0.12em; color:#38BDF8; margin-bottom:2px; text-transform:uppercase;">
                        ENTERPRISE SURVEILLANCE &amp; FIRE COMMAND HUB
                    </div>
                    <h1 class="welspun-header-title">{title}</h1>
                    <p class="welspun-header-subtitle">{subtitle}</p>
                </div>
            </div>
            <div style="display:flex; flex-direction:row; align-items:center; gap:12px; margin-top:8px;">
                <div style="background:rgba(15, 23, 42, 0.45); border:1px solid rgba(255,255,255,0.22); border-radius:8px; padding:6px 14px; text-align:right;">
                    <span style="font-size:0.7rem; color:#BAE6FD; text-transform:uppercase; letter-spacing:0.05em; font-weight:600;">Active CCTV Feeds</span><br>
                    <b style="font-size:1.15rem; color:#FFFFFF;">{online_cameras:,} <span style="font-size:0.82rem; color:#94A3B8;">/ {total_cameras:,}</span> <span style="color:#34D399; font-size:0.88rem;">({uptime_pct:.1f}%)</span></b>
                </div>
                <div style="background:rgba(15, 23, 42, 0.45); border:1px solid rgba(255,255,255,0.22); border-radius:8px; padding:6px 14px; text-align:right;">
                    <span style="font-size:0.7rem; color:#BAE6FD; text-transform:uppercase; letter-spacing:0.05em; font-weight:600;">Incident-Free Streak</span><br>
                    <b style="font-size:1.15rem; color:#34D399;">{days_incident_free} DAYS</b>
                </div>
                <div class="welspun-badge">
                    <span class="pulse-dot-green"></span>
                    {badge_text}
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )
