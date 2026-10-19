"""
Logistics Gate, Truck Entry/Exit & Unmanned Weighbridge Screen Component
Full unmanned weighbridge automation with multi-load cell telemetry, dashcam feeds, and seamless SAP S/4HANA integration.
"""
import streamlit as st
import pandas as pd
from styles.welspun_theme import WELSPUN_COLORS
from components.cctv_view import render_cctv_video_card
from data.logistics_data import (
    get_weighbridge_kpis,
    get_weighbridge_feeds,
    get_current_weighment_state,
    get_logistics_truck_log
)

def render_logistics_screen(stream_format: str = "Live Stream"):
    """Renders the comprehensive Logistics Gate & Unmanned Weighbridge Command Screen."""
    kpi_data = get_weighbridge_kpis()
    feeds = get_weighbridge_feeds()
    active_state = get_current_weighment_state()
    truck_log = get_logistics_truck_log()

    # 1. Top KPI Row (4 Verified Operational Metrics)
    k1, k2, k3, k4 = st.columns(4)
    with k1:
        with st.container(border=True):
            st.caption("TRUCK TRAFFIC")
            st.metric("Trucks Today", kpi_data['trucks_today']['value'], kpi_data['trucks_today']['sub'])
    with k2:
        with st.container(border=True):
            st.caption("AUTOMATION")
            st.metric("Unmanned %", kpi_data['unmanned_pct']['value'], kpi_data['unmanned_pct']['sub'])
    with k3:
        with st.container(border=True):
            st.caption("TURNAROUND")
            st.metric("Avg Gate Time", kpi_data['avg_turnaround_min']['value'], kpi_data['avg_turnaround_min']['sub'])
    with k4:
        with st.container(border=True):
            st.caption("SCALES")
            st.metric("Active Scales", kpi_data['active_weighbridges']['value'], kpi_data['active_weighbridges']['sub'])

    # 2. Main Layout: Left Column for Weighbridge Overhead CCTV & UVIS Scanner, Right Column for Digital Scale Telemetry
    col_video_left, col_tele_right = st.columns([1.5, 1.5])

    with col_video_left:
        st.markdown("#### 🎥 Logistics Gate & Unmanned Weighbridge Overhead CCTV")
        # Only weighbridge overhead camera (CAM-WB01); truck dashcam omitted per requirement
        render_cctv_video_card(feeds[0], stream_format=stream_format)

        # Automated Undercarriage & Container Seal Inspection Telemetry
        with st.container(border=True):
            u_hdr1, u_hdr2 = st.columns([2.2, 1.2])
            with u_hdr1:
                st.caption("AUTOMATED UVIS UNDERCARRIAGE & SEAL AI SCANNER")
            with u_hdr2:
                st.success("● SCAN CLEAR • ZERO ANOMALIES")
            
            uc1, uc2, uc3 = st.columns(3)
            with uc1:
                st.markdown("Chassis Object: :green[**CLEARED (0 Detect)**]")
            with uc2:
                st.markdown("Container Seal: :blue[**#WLP-SEAL-8894 INTACT**]")
            with uc3:
                st.markdown("FASTag RFID: `3416-1FA8-9920-55B1`")

    with col_tele_right:
        st.markdown("#### ⚖️ Unmanned Weighbridge Automation Platform (WB-01)")
        
        # Live Digital Weight Scale Display (Native Streamlit Container)
        gross_wt = active_state["gross_weight_kg"]
        tare_wt = active_state["tare_weight_kg"]
        net_wt = active_state["net_weight_kg"]

        with st.container(border=True):
            col_hdr1, col_hdr2 = st.columns([2, 1.2])
            with col_hdr1:
                st.caption("DIGITAL LOAD CELL WEIGHMENT INDICATOR")
                st.subheader(f"{active_state['truck_plate']}")
                st.caption(f"Transporter: **{active_state['transporter']}**")
            with col_hdr2:
                st.success("● WEIGHT STABILIZED")
                st.caption(f"Ticket: `{active_state['weight_slip_no']}`")
            
            # 3 High-Impact Real-Time Metrics
            m1, m2, m3 = st.columns(3)
            with m1:
                st.metric(
                    label="Gross Weight",
                    value=f"{gross_wt:,} KG",
                    delta="±0.0 kg stability",
                    delta_color="normal"
                )
            with m2:
                st.metric(
                    label="Tare Weight",
                    value=f"{tare_wt:,} KG",
                    delta="Registered RTO Baseline",
                    delta_color="off"
                )
            with m3:
                st.metric(
                    label="Net Material Wt",
                    value=f"{net_wt:,} KG",
                    delta=f"{net_wt/1000:.2f} Metric Tons",
                    delta_color="normal"
                )
            
            st.divider()
            
            det1, det2 = st.columns(2)
            with det1:
                st.markdown(f"**Cargo Material:** {active_state['material']}")
                st.markdown("**IR Platform Position:** :green[✓ 100% On-Deck (Zero Overhang)]")
            with det2:
                st.markdown("**Barrier State:** :green[**● OPEN (AUTOMATED CLEARANCE)**]")
                st.markdown("**Scale Deck Light:** :green[**● GREEN (PROCEED)**]")

        # 3. 6-Point Electronic Load Cell Distribution Array
        st.markdown("#### 🎛️ Digital Load Cell Weight Sensors (6-Point Deck Array)")
        with st.container(border=True):
            lc_h1, lc_h2 = st.columns([2, 1.2])
            with lc_h1:
                st.caption("CALIBRATED SENSOR DISTRIBUTION")
                st.markdown("##### 100 MT Electronic Deck Array")
            with lc_h2:
                st.success("● ALL CELLS BALANCED")
            
            lc1, lc2, lc3 = st.columns(3)
            with lc1:
                st.metric("LC-1 Front Left", f"{active_state['load_cells'][0]['weight_kg']:,} kg", "Normal")
                st.metric("LC-2 Front Right", f"{active_state['load_cells'][1]['weight_kg']:,} kg", "Normal")
            with lc2:
                st.metric("LC-3 Mid Left", f"{active_state['load_cells'][2]['weight_kg']:,} kg", "Normal")
                st.metric("LC-4 Mid Right", f"{active_state['load_cells'][3]['weight_kg']:,} kg", "Normal")
            with lc3:
                st.metric("LC-5 Rear Left", f"{active_state['load_cells'][4]['weight_kg']:,} kg", "Normal")
                st.metric("LC-6 Rear Right", f"{active_state['load_cells'][5]['weight_kg']:,} kg", "Normal")

        # Interactive Scale Action Buttons
        col_btn1, col_btn2 = st.columns(2)
        with col_btn1:
            if st.button("⚡ Trigger Scale Calibration / Re-Zero", use_container_width=True, type="primary"):
                st.toast("CALIBRATION OK: 6 Load Cells Balanced. Deck Zero Offset Verified.", icon="⚖️")
        with col_btn2:
            if st.button("🖨️ Print Digital Weight Slip", use_container_width=True):
                st.toast("Weight Slip #WS-2026-10492 printed at Gate 1 Kiosk.", icon="📄")

    # 4. Comprehensive Truck Movements Table (Pure Operational Weighment Data)
    st.markdown("---")
    st.markdown("#### 📋 Real-Time Inbound & Outbound Truck Weighment Log")
    st.caption("Showing automated weighments, vehicle license plates, verified scale weights, and gate clearance status.")

    df_trucks = pd.DataFrame(truck_log)
    # Remove SAP-specific columns per requirement
    display_cols = [c for c in df_trucks.columns if c not in ["sap_po_so", "sap_doc"]]
    st.dataframe(
        df_trucks[display_cols],
        use_container_width=True,
        hide_index=True,
        column_config={
            "time": st.column_config.TextColumn("Gate Time"),
            "truck_no": st.column_config.TextColumn("Vehicle Plate"),
            "type": st.column_config.TextColumn("Movement Type"),
            "material": st.column_config.TextColumn("Material Description"),
            "gate": st.column_config.TextColumn("Weighbridge"),
            "gross_kg": st.column_config.NumberColumn("Gross Wt (kg)", format="%d"),
            "tare_kg": st.column_config.NumberColumn("Tare Wt (kg)", format="%d"),
            "net_kg": st.column_config.NumberColumn("Net Wt (kg)", format="%d"),
            "weight_slip": st.column_config.TextColumn("Weight Slip #"),
            "status": st.column_config.TextColumn("Gate Status")
        }
    )
