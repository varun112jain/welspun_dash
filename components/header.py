"""
Header Component for Welspun Dashboard
"""
import streamlit as st

def render_welspun_header(
    title: str = "Welspun Integrated Command & Control Centre (ICCC)",
    subtitle: str = "Live CCTV Surveillance, Fire Network & Safety Intelligence • Anjar Plants & City Quarters",
    badge_text: str = "LIVE DEFENSE MESH",
    days_incident_free: int = 148,
    online_cameras: int = 1424,
    total_cameras: int = 1438
):
    """Renders a polished Welspun header banner with corporate branding, cameras uptime, and incident milestone."""
    uptime_pct = (online_cameras / total_cameras) * 100
    st.markdown(
        f"""
        <div class="welspun-header-card">
            <div>
                <div style="font-size:0.8rem; font-weight:700; letter-spacing:0.12em; color:#38BDF8; margin-bottom:4px; text-transform:uppercase;">
                    WELSPUN GROUP • ANJAR MEGA COMPLEX
                </div>
                <h1 class="welspun-header-title">{title}</h1>
                <p class="welspun-header-subtitle">{subtitle}</p>
            </div>
            <div style="text-align: right; display:flex; flex-direction:row; align-items:center; gap:12px;">
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
