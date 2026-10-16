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

    # 1. Top KPI Row (Native Streamlit Metrics)
    b1, b2, b3, b4, b5, b6 = st.columns(6)
    with b1:
        with st.container(border=True):
            st.caption("FLEET SIZE")
            st.metric("Active Buses", kpis['active_fleet']['value'], kpis['active_fleet']['sub'])
    with b2:
        with st.container(border=True):
            st.caption("RIDERSHIP")
            st.metric("Commuters", kpis['commuters_today']['value'], kpis['commuters_today']['sub'])
    with b3:
        with st.container(border=True):
            st.caption("SCHEDULE")
            st.metric("On-Time Dep.", kpis['on_time_departure']['value'], kpis['on_time_departure']['sub'])
    with b4:
        with st.container(border=True):
            st.caption("DSM SAFETY")
            st.metric("Alertness", kpis['driver_alertness']['value'], kpis['driver_alertness']['sub'])
    with b5:
        with st.container(border=True):
            st.caption("OCCUPANCY")
            st.metric("Avg Seat Occ.", kpis['seat_occupancy']['value'], kpis['seat_occupancy']['sub'])
    with b6:
        with st.container(border=True):
            st.caption("COMPLIANCE")
            st.metric("Safety Index", kpis['safety_index']['value'], kpis['safety_index']['sub'])

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
        with st.container(border=True):
            d_hdr1, d_hdr2 = st.columns([2.2, 1.2])
            with d_hdr1:
                st.caption("AI DRIVER STATUS MONITORING (DSM) & FATIGUE TELEMETRY")
            with d_hdr2:
                st.success("● ALL 12 DRIVERS ATTENTIVE")
            
            dc1, dc2, dc3 = st.columns(3)
            with dc1:
                st.markdown("Eye Blink Rate: :green[**NORMAL (14/min)**]")
            with dc2:
                st.markdown("Yawn / Head Tilt: :green[**ZERO DETECTED**]")
            with dc3:
                st.markdown("Speed Governor: :blue[**LOCKED (50 KM/H)**]")

    with col_ctrl_right:
        st.markdown("#### 🚌 Shift Rostering & Employee Transit Timetable")
        
        # Shift Schedule Breakdown
        for item in schedule:
            with st.container(border=True):
                s_c1, s_c2 = st.columns([2, 1.2])
                with s_c1:
                    st.markdown(f"**{item['shift']}** — 🕒 `{item['timing']}`")
                    st.caption(f"Fleet Allocation: **{item['buses']} Dedicated Buses**")
                with s_c2:
                    st.markdown(f":blue[**{item['workers_moved']} Workers**]")
                    st.caption(f":green[✓ {item['on_time_pct']} On-Time]")

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
