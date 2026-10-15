"""
Welspun Integrated Command & Control Centre (ICCC) - Anjar Plant & City
Surveillance, Fire Network & Safety Dashboard with 8 Native Streaming Video Feeds,
Perimeter Crossing Detection, Smoke/Fire Sensor Health, and Incident Milestone Clock.
"""
import os
import streamlit as st

# Local modules
from styles.welspun_theme import load_css, WELSPUN_COLORS
from components.header import render_welspun_header
from components.cctv_view import render_cctv_video_card
from components.fire_command import render_hydrant_gauge, render_fire_network_panel
from components.incident_panel import render_incident_panel
from components.spatial_map import render_anjar_spatial_map
from components.sensor_health import render_sensor_health_panel
from data.surveillance_data import (
    get_safety_incident_stats,
    get_sensor_health_telemetry,
    get_surveillance_kpis,
    get_cctv_feeds,
    get_fire_network_status,
    get_active_alarms
)

# Page Setup
icon_path = os.path.join(os.path.dirname(__file__), "assets", "welspun_icon.png")
st.set_page_config(
    page_title="Welspun Anjar ICCC • Multi-Screen Surveillance",
    page_icon=icon_path if os.path.exists(icon_path) else "🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Apply Welspun Corporate Styling
load_css()

# Session State for Dynamic Feeds & Switching
if "active_spotlight_idx" not in st.session_state:
    st.session_state["active_spotlight_idx"] = 0  # CAM-04 (Perimeter Crossing)
if "grid_cols" not in st.session_state:
    st.session_state["grid_cols"] = 2
if "perimeter_alert_active" not in st.session_state:
    st.session_state["perimeter_alert_active"] = True

# Fetch Synthetic Data
safety_stats = get_safety_incident_stats()
sensor_health = get_sensor_health_telemetry()
kpi_data = get_surveillance_kpis()
cctv_feeds = get_cctv_feeds()
fire_data = get_fire_network_status()
alarms_data = get_active_alarms()

# ----------------- SIDEBAR -----------------
with st.sidebar:
    logo_path = os.path.join(os.path.dirname(__file__), "assets", "welspun_full_logo.png")
    if os.path.exists(logo_path):
        st.image(logo_path, use_container_width=True)
    else:
        st.markdown(f"<h2 style='color:{WELSPUN_COLORS['primary']};'>WELSPUN</h2>", unsafe_allow_html=True)
    
    st.markdown(
        """
        <div style="background:#0F172A; color:#E2E8F0; padding:10px 14px; border-radius:8px; margin-top:8px; border-left:4px solid #00A6E6;">
            <div style="font-size:0.72rem; text-transform:uppercase; letter-spacing:0.08em; color:#94A3B8;">Enterprise Facility</div>
            <div style="font-size:1.05rem; font-weight:700;">WELSPUN ANJAR</div>
            <div style="font-size:0.8rem; color:#38BDF8;">Mega Industrial Plants & Welspun City</div>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    st.markdown("---")
    st.markdown("### 🎛️ Video Wall Configuration")
    
    stream_mode = st.radio(
        "Stream Rendering Engine",
        ["⚡ Live Continuous Stream (Optimized)", "🎥 H.264 HTML5 Video Player", "📸 Static Snapshot HUD"],
        index=0
    )
    stream_fmt = "MP4" if "H.264" in stream_mode else ("Snapshot" if "Snapshot" in stream_mode else "Live Stream")
    
    feed_filter = st.selectbox(
        "Screen Sector Filter",
        [
            "🖥️ All 8 Active Screens (Master Wall)",
            "🏭 Industrial Manufacturing Plants (CAM-01, 02, 06)",
            "🚷 Perimeter & High-Voltage Gates (CAM-04, 07)",
            "🏡 Welspun City Quarters & Campus (CAM-05, 08)",
            "🚒 Fire Station Emergency Bay (CAM-03)"
        ]
    )
    
    cols_choice = st.radio(
        "Screen Layout Density",
        ["2 Screens per Row (Large HD)", "3 Screens per Row (Dense)", "4 Screens per Row (Quad Row)"],
        index=0
    )
    num_cols = 2 if "2" in cols_choice else (3 if "3" in cols_choice else 4)
    st.session_state["grid_cols"] = num_cols

    st.markdown("---")
    st.markdown("### 🚨 Perimeter & Incident Simulator")
    st.caption("Trigger or resolve real-time synthetic events:")
    
    col_sim1, col_sim2 = st.columns(2)
    with col_sim1:
        if st.button("🚷 Trigger Breach", use_container_width=True, type="primary"):
            st.session_state["perimeter_alert_active"] = True
            st.session_state["active_spotlight_idx"] = 0  # Jump to CAM-04 perimeter breach
            st.toast("ALARM: Virtual Tripwire Crossed at Sector 4!", icon="🚨")
            st.rerun()
    with col_sim2:
        if st.button("✅ Clear Breach", use_container_width=True):
            st.session_state["perimeter_alert_active"] = False
            st.toast("Perimeter sector cleared & secured.", icon="🛡️")
            st.rerun()
            
    st.markdown("---")
    st.markdown("#### 🚒 Emergency Fire Dispatch")
    selected_tender = st.selectbox(
        "Dispatch Unit",
        ["Tender WF-01 (12kL Water Bowser)", "Tender WF-02 (Foam Tender)", "Tender WF-03 (32m Sky-Lift)", "Tender WF-04 (QRV Rapid Unit)"]
    )
    if st.button("🚨 Dispatch Tender to Sector 4", use_container_width=True):
        st.toast(f"Emergency: {selected_tender} en route to Sector 4!", icon="🚒")

    st.markdown("---")
    st.caption("Welspun Anjar Security Mesh • 100% Fiber Backhaul")

# ----------------- MAIN CONTENT -----------------

# Welspun Header Banner (Updated to WELSPUN & Days Since Last Incident)
render_welspun_header(
    title="Welspun Integrated Command & Control Centre",
    subtitle="AI Multi-Screen CCTV Surveillance, Fire Network & Safety Intelligence • Anjar Plants & Welspun City",
    badge_text="LIVE DEFENSE MESH",
    days_incident_free=safety_stats["days_since_last_incident"]
)

# Critical Breach Notification Bar if perimeter crossing is active
if st.session_state["perimeter_alert_active"]:
    st.markdown(
        """
        <div style="background:linear-gradient(90deg, #7F1D1D 0%, #B91C1C 50%, #EF4444 100%); color:#FFFFFF; padding:12px 18px; border-radius:8px; margin-bottom:14px; box-shadow:0 4px 14px rgba(239, 68, 68, 0.35); display:flex; justify-content:space-between; align-items:center;">
            <div style="display:flex; align-items:center; gap:12px;">
                <span style="font-size:1.6rem; animation:pulse-red 1s infinite;">🚨</span>
                <div>
                    <b style="font-size:1.05rem; letter-spacing:0.02em;">CRITICAL BREACH: PERIMETER TRIPWIRE CROSSING DETECTED</b><br>
                    <span style="font-size:0.85rem; color:#FEE2E2;">CAM-04 (Sector 4 West Boundary) flagged unauthorized individual entering high-voltage hazmat zone. Security patrol dispatched.</span>
                </div>
            </div>
            <div style="background:rgba(255,255,255,0.2); padding:6px 14px; border-radius:6px; font-weight:700; font-size:0.85rem;">
                CODE RED • ACTIVE
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

# Top KPI Metric Row (Includes CCTV Uptime Count)
k_cam, k1, k2, k3, k4, k5 = st.columns(6)

with k_cam:
    st.markdown(
        f"""
        <div class="surv-kpi-card optimal" style="border-left-color: #005BAA;">
            <div class="surv-kpi-label">CCTV Feeds Online</div>
            <div class="surv-kpi-val" style="color:#005BAA;">1,424 / 1,438</div>
            <div class="surv-kpi-sub"><b>99.0% Active</b> • 14 Maint.</div>
        </div>
        """,
        unsafe_allow_html=True
    )

with k1:
    st.markdown(
        f"""
        <div class="surv-kpi-card optimal" style="border-left-color: #10B981;">
            <div class="surv-kpi-label">Safety Milestone</div>
            <div class="surv-kpi-val" style="color:#059669;">{safety_stats["days_since_last_incident"]} DAYS</div>
            <div class="surv-kpi-sub"><b>{safety_stats["safe_man_hours"]}</b> Zero Incident</div>
        </div>
        """,
        unsafe_allow_html=True
    )

with k2:
    st.markdown(
        f"""
        <div class="surv-kpi-card critical">
            <div class="surv-kpi-label">{kpi_data["perimeter_crossings"]["label"]}</div>
            <div class="surv-kpi-val" style="color:#EF4444;">{kpi_data["perimeter_crossings"]["value"]}</div>
            <div class="surv-kpi-sub" style="color:#B91C1C;">⚠️ {kpi_data["perimeter_crossings"]["sub"]}</div>
        </div>
        """,
        unsafe_allow_html=True
    )

with k3:
    st.markdown(
        f"""
        <div class="surv-kpi-card critical">
            <div class="surv-kpi-label">{kpi_data["active_fire_alarms"]["label"]}</div>
            <div class="surv-kpi-val" style="color:#EA580C;">{kpi_data["active_fire_alarms"]["value"]}</div>
            <div class="surv-kpi-sub" style="color:#C2410C;">⚠️ {kpi_data["active_fire_alarms"]["sub"]}</div>
        </div>
        """,
        unsafe_allow_html=True
    )

with k4:
    st.markdown(
        f"""
        <div class="surv-kpi-card optimal">
            <div class="surv-kpi-label">{kpi_data["sensor_health"]["label"]}</div>
            <div class="surv-kpi-val" style="color:#005BAA;">{kpi_data["sensor_health"]["value"]}</div>
            <div class="surv-kpi-sub">{kpi_data["sensor_health"]["sub"]}</div>
        </div>
        """,
        unsafe_allow_html=True
    )

with k5:
    st.markdown(
        f"""
        <div class="surv-kpi-card optimal">
            <div class="surv-kpi-label">{kpi_data["fire_station_readiness"]["label"]}</div>
            <div class="surv-kpi-val">{kpi_data["fire_station_readiness"]["value"]}</div>
            <div class="surv-kpi-sub">{kpi_data["fire_station_readiness"]["sub"]}</div>
        </div>
        """,
        unsafe_allow_html=True
    )

st.markdown("<br>", unsafe_allow_html=True)

# ----------------- TABS WORKSPACE -----------------
tab_video, tab_sensors, tab_fire, tab_alerts, tab_map = st.tabs([
    "🎥 CCTV Multi-Screen Video Wall",
    "🔥 Smoke & Fire Sensor Health",
    "🚒 Networked Fire Station Hub",
    "⚠️ Live Alarms & Security Log",
    "🗺️ Anjar Spatial Topology Map"
])

# ----------------- TAB 1: CCTV FEEDS -----------------
with tab_video:
    # Filter feeds by sector if user selected a subset
    display_feeds = cctv_feeds
    if "Industrial" in feed_filter:
        display_feeds = [f for f in cctv_feeds if "Plant Core" in f["zone"]]
    elif "Perimeter" in feed_filter:
        display_feeds = [f for f in cctv_feeds if "Perimeter" in f["zone"] or "Gate" in f["name"]]
    elif "Quarters" in feed_filter:
        display_feeds = [f for f in cctv_feeds if "Welspun City" in f["zone"]]
    elif "Fire Station" in feed_filter:
        display_feeds = [f for f in cctv_feeds if "Emergency" in f["zone"]]

    # Prominent Camera Online Telemetry Banner
    st.markdown(
        """
        <div style="background:#0F172A; border:1px solid #334155; border-radius:8px; padding:12px 18px; margin-bottom:14px; display:flex; justify-content:space-between; align-items:center;">
            <div>
                <span style="color:#BAE6FD; font-size:0.75rem; text-transform:uppercase; font-weight:700; letter-spacing:0.05em;">Surveillance Camera Network Telemetry</span><br>
                <b style="font-size:1.35rem; color:#FFFFFF;">1,424 <span style="color:#94A3B8; font-size:0.92rem;">UP OUT OF</span> 1,438 <span style="color:#10B981; font-size:1.05rem;">(99.0% OPERATIONAL)</span></b>
            </div>
            <div style="display:flex; gap:16px; font-size:0.8rem; color:#E2E8F0;">
                <div>🏭 Plant Core: <b style="color:#38BDF8;">812/820</b></div>
                <div>🚷 Perimeter: <b style="color:#FBBF24;">216/218</b></div>
                <div>🏡 City Quarters: <b style="color:#34D399;">348/350</b></div>
                <div>🚒 Fire Hub: <b style="color:#F87171;">48/50</b></div>
                <div>🔧 Maintenance: <b style="color:#94A3B8;">14</b></div>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    # Render Multi-Screen Grid (All feeds visible at once)
    cols = st.columns(num_cols)
    for idx, feed in enumerate(display_feeds):
        target_col = cols[idx % num_cols]
        with target_col:
            render_cctv_video_card(feed, stream_format=stream_fmt)

# ----------------- TAB 2: SENSOR HEALTH -----------------
with tab_sensors:
    render_sensor_health_panel(sensor_health)

# ----------------- TAB 3: FIRE NETWORK -----------------
with tab_fire:
    col_f_left, col_f_right = st.columns([1.8, 1.2])
    with col_f_left:
        render_fire_network_panel(fire_data)
    with col_f_right:
        st.markdown("### 💧 Hydrant Ring Telemetry")
        fig_gauge = render_hydrant_gauge(pressure_bar=fire_data["hydrant_telemetry"]["main_ring_pressure_bar"])
        st.plotly_chart(fig_gauge, use_container_width=True)
        
        tele = fire_data["hydrant_telemetry"]
        st.markdown(
            f"""
            <div style="background:#F8FAFC; border:1px solid #E2E8F0; border-radius:8px; padding:12px; font-size:0.85rem; color:#334155;">
                <div style="display:flex; justify-content:space-between; margin-bottom:6px;">
                    <span><b>Dedicated Static Reserve:</b></span>
                    <span style="color:#005BAA; font-weight:700;">{tele['static_water_reserves_litres']}</span>
                </div>
                <div style="display:flex; justify-content:space-between; margin-bottom:6px;">
                    <span><b>Networked Hydrant Posts:</b></span>
                    <span>{tele['active_hydrant_posts']} Outlets Active</span>
                </div>
                <div style="display:flex; justify-content:space-between; margin-bottom:6px;">
                    <span><b>Electric Jockey Pump:</b></span>
                    <span style="color:#10B981; font-weight:600;">{tele['jockey_pump_status']}</span>
                </div>
                <div style="display:flex; justify-content:space-between; margin-bottom:6px;">
                    <span><b>Diesel Emergency Pump:</b></span>
                    <span style="color:#10B981; font-weight:600;">{tele['diesel_main_pump_status']}</span>
                </div>
                <div style="display:flex; justify-content:space-between;">
                    <span><b>Telemetry Backhaul:</b></span>
                    <span>{tele['network_connectivity']}</span>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

# ----------------- TAB 4: ALARMS & INCIDENTS -----------------
with tab_alerts:
    col_a_feed, col_a_sim = st.columns([2.2, 1])
    with col_a_feed:
        render_incident_panel(alarms_data)
    with col_a_sim:
        st.markdown("### ⚡ Security & Safety Command")
        st.markdown(
            """
            <div style="background:#FEF2F2; border:1px solid #FECACA; border-radius:8px; padding:14px; margin-bottom:14px;">
                <div style="color:#991B1B; font-weight:bold; font-size:0.95rem; margin-bottom:4px;">🚨 Active Security Event</div>
                <div style="color:#7F1D1D; font-size:0.85rem;">
                    Sector 4 West Tripwire breached. Video recording flagged for security review.
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )
        if st.button("📢 Broadcast Perimeter Evacuation PA Siren", use_container_width=True, type="secondary"):
            st.warning("Perimeter Horn Sounded at Sector 4 Boundary.")
        if st.button("🚔 Dispatch Rapid Security Intervention Vehicle", use_container_width=True):
            st.error("Quick Response Security Squad dispatched to Sector 4.")
        if st.button("✅ Mark Perimeter Zone Inspected & Secured", use_container_width=True):
            st.session_state["perimeter_alert_active"] = False
            st.success("Perimeter status updated to SECURE.")
            st.rerun()

# ----------------- TAB 5: SPATIAL MAP -----------------
with tab_map:
    st.markdown("#### Spatial Defense, Perimeter & Hydrant Topology")
    st.caption("Visualizing manufacturing plant sectors, restricted perimeter fence, Welspun City residential quarters, and dual fire stations.")
    fig_map = render_anjar_spatial_map()
    st.plotly_chart(fig_map, use_container_width=True)
