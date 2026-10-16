"""
Employee Transit & Commuter Bus Fleet Command Screen Component
Monitors the bus shuttle network carrying employees between Welspun City Township, Anjar, Gandhidham, and the manufacturing mills.
Includes live Dashcam feeds, in-cabin occupancy, RFID contactless turnstiles, and AI Driver Status Monitoring (DSM).
"""
import streamlit as st
import pandas as pd
from styles.welspun_theme import WELSPUN_COLORS
from components.cctv_view import render_cctv_video_card
from data.bus_transit_data import (
    get_bus_transit_kpis,
    get_bus_transit_feeds,
    get_commuter_bus_roster,
    get_shift_schedule
)

def render_bus_transit_screen(stream_format: str = "Live Stream"):
    """Renders the comprehensive Employee Transit & Commuter Bus Fleet Command Screen."""
    kpis = get_bus_transit_kpis()
    feeds = get_bus_transit_feeds()
    roster = get_commuter_bus_roster()
    schedule = get_shift_schedule()

    # 1. Top KPI Row
    st.markdown(
        f"""
        <div class="kpi-grid" style="grid-template-columns: repeat(6, 1fr); margin-bottom:1rem;">
            <div class="surv-kpi-card optimal" style="border-left-color: #005BAA;">
                <div class="surv-kpi-label">Active Bus Fleet</div>
                <div class="surv-kpi-val" style="color:#005BAA;">{kpis['active_fleet']['value']}</div>
                <div class="surv-kpi-sub"><b>{kpis['active_fleet']['sub']}</b></div>
            </div>
            <div class="surv-kpi-card optimal" style="border-left-color: #10B981;">
                <div class="surv-kpi-label">Commuters Today</div>
                <div class="surv-kpi-val" style="color:#059669;">{kpis['commuters_today']['value']}</div>
                <div class="surv-kpi-sub"><b>{kpis['commuters_today']['sub']}</b></div>
            </div>
            <div class="surv-kpi-card optimal" style="border-left-color: #00A6E6;">
                <div class="surv-kpi-label">On-Time Performance</div>
                <div class="surv-kpi-val" style="color:#0284C7;">{kpis['on_time_departure']['value']}</div>
                <div class="surv-kpi-sub"><b>{kpis['on_time_departure']['sub']}</b></div>
            </div>
            <div class="surv-kpi-card optimal" style="border-left-color: #10B981;">
                <div class="surv-kpi-label">Driver Alertness (DSM)</div>
                <div class="surv-kpi-val" style="color:#059669;">{kpis['driver_alertness']['value']}</div>
                <div class="surv-kpi-sub"><b>{kpis['driver_alertness']['sub']}</b></div>
            </div>
            <div class="surv-kpi-card optimal" style="border-left-color: #005BAA;">
                <div class="surv-kpi-label">Average Seat Occupancy</div>
                <div class="surv-kpi-val" style="color:#005BAA;">{kpis['seat_occupancy']['value']}</div>
                <div class="surv-kpi-sub">{kpis['seat_occupancy']['sub']}</div>
            </div>
            <div class="surv-kpi-card optimal" style="border-left-color: #10B981;">
                <div class="surv-kpi-label">Transit Safety Compliance</div>
                <div class="surv-kpi-val" style="color:#059669;">{kpis['safety_index']['value']}</div>
                <div class="surv-kpi-sub"><b>{kpis['safety_index']['sub']}</b></div>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    # 2. Main Layout: Feeds Left, Control & Shift Telemetry Right
    col_feeds_left, col_ctrl_right = st.columns([1.6, 1.4])

    with col_feeds_left:
        st.markdown("#### 🎥 Employee Transit Terminal & Commuter Dashcam Feeds")
        feed_cols = st.columns(2)
        with feed_cols[0]:
            render_cctv_video_card(feeds[0], stream_format=stream_format)
        with feed_cols[1]:
            render_cctv_video_card(feeds[1], stream_format=stream_format)

        # AI Driver Status Monitoring (DSM) & Cabin Safety Matrix
        st.markdown(
            """
            <div style="background:#0F172A; border:1px solid #334155; border-radius:8px; padding:12px 16px; margin-top:4px;">
                <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:8px;">
                    <span style="color:#38BDF8; font-size:0.78rem; font-weight:700; text-transform:uppercase; letter-spacing:0.05em;">
                        AI Driver Status Monitoring (DSM) &amp; Fatigue Telemetry
                    </span>
                    <span style="background:rgba(16, 185, 129, 0.2); color:#10B981; font-size:0.72rem; font-weight:700; padding:2px 8px; border-radius:4px; border:1px solid #059669;">
                        ● ALL 12 DRIVERS 100% ATTENTIVE
                    </span>
                </div>
                <div style="display:grid; grid-template-columns:repeat(3, 1fr); gap:10px; font-size:0.78rem; color:#CBD5E1;">
                    <div>Eye Blink Rate: <b style="color:#10B981;">NORMAL (14/min)</b></div>
                    <div>Yawn / Head Tilt: <b style="color:#10B981;">ZERO DETECTED</b></div>
                    <div>Speed Governor: <b style="color:#38BDF8;">LOCKED (50 KM/H MAX)</b></div>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col_ctrl_right:
        st.markdown("#### 🚌 Shift Rostering & Employee Transit Timetable")
        
        # Shift Schedule Breakdown
        for item in schedule:
            st.markdown(
                f"""
                <div style="background:#FFFFFF; border:1px solid #CBD5E1; border-left:4px solid #005BAA; border-radius:8px; padding:10px 14px; margin-bottom:8px; display:flex; justify-content:space-between; align-items:center; box-shadow:0 1px 4px rgba(0,0,0,0.03);">
                    <div>
                        <b style="color:#0F172A; font-size:0.9rem;">{item['shift']}</b>
                        <span style="color:#64748B; font-size:0.78rem; margin-left:8px;">🕒 {item['timing']}</span><br>
                        <span style="font-size:0.78rem; color:#475569;">Fleet Allocation: <b>{item['buses']} Dedicated Buses</b></span>
                    </div>
                    <div style="text-align:right;">
                        <span style="color:#005BAA; font-weight:700; font-size:0.92rem;">{item['workers_moved']} Workers</span><br>
                        <span style="color:#10B981; font-size:0.75rem; font-weight:600;">✓ {item['on_time_pct']} On-Time</span>
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )

        st.markdown("#### 🎛️ Employee Shuttle Dispatch & Emergency PA")
        selected_bus = st.selectbox(
            "Select Shuttle Bus for Live Telemetry Intercept",
            [f"{b['bus_id']} — {b['route_name']} ({b['driver']})" for b in roster]
        )
        
        col_btn1, col_btn2 = st.columns(2)
        with col_btn1:
            if st.button("🚀 Dispatch Next Shuttle", use_container_width=True, type="primary"):
                st.toast("DISPATCH: Bay 2 Bus WB-02 departed for Anjar City!", icon="🚌")
                st.toast("RFID Turnstiles synced: 38 Boarded, 4 Seats Reserved.", icon="🎟️")
        with col_btn2:
            if st.button("📢 Broadcast Bus Station PA", use_container_width=True):
                st.toast("PA Announcement: Shift B boarding commences at Bays 1 - 4.", icon="📢")

    # 3. Comprehensive Commuter Bus Fleet Table
    st.markdown("---")
    st.markdown("#### 🗺️ Live Commuter Bus Fleet Telemetry & Occupancy Matrix")
    st.caption("Real-time GPS tracking, speed governor status, passenger seat occupancy, and Driver Status Monitoring (DSM).")

    df_buses = pd.DataFrame(roster)
    st.dataframe(
        df_buses,
        use_container_width=True,
        hide_index=True,
        column_config={
            "bus_id": st.column_config.TextColumn("Bus ID"),
            "route_name": st.column_config.TextColumn("Transit Route"),
            "driver": st.column_config.TextColumn("Designated Driver"),
            "shift": st.column_config.TextColumn("Assigned Shift"),
            "capacity": st.column_config.NumberColumn("Capacity", format="%d"),
            "occupied": st.column_config.NumberColumn("Occupied Seats", format="%d"),
            "speed_kmh": st.column_config.NumberColumn("Speed (km/h)", format="%.1f"),
            "status": st.column_config.TextColumn("Transit Status"),
            "dsm_status": st.column_config.TextColumn("AI DSM Driver Status"),
            "eta_mins": st.column_config.NumberColumn("ETA (Mins)", format="%d"),
            "destination": st.column_config.TextColumn("Destination")
        }
    )
