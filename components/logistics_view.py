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

    # 1. Top KPI Row (Native Streamlit Metrics)
    k1, k2, k3, k4, k5, k6 = st.columns(6)
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
            st.caption("SAP S/4HANA")
            st.metric("Sync Status", kpi_data['sap_sync_health']['value'], kpi_data['sap_sync_health']['sub'])
    with k5:
        with st.container(border=True):
            st.caption("SCALES")
            st.metric("Active Scales", kpi_data['active_weighbridges']['value'], kpi_data['active_weighbridges']['sub'])
    with k6:
        with st.container(border=True):
            st.caption("COMPLIANCE")
            st.metric("Tolerance", kpi_data['weight_tolerance']['value'], kpi_data['weight_tolerance']['sub'])

    # 2. Main Layout: Left 2 Columns for Live Feeds, Right Column for Unmanned Automation & SAP Sync
    col_video_left, col_tele_right = st.columns([1.6, 1.4])

    with col_video_left:
        st.markdown("#### 🎥 Logistics Gate, Weighbridge & Supporting Dashcam Feeds")
        feed_cols = st.columns(2)
        with feed_cols[0]:
            render_cctv_video_card(feeds[0], stream_format=stream_format)
        with feed_cols[1]:
            render_cctv_video_card(feeds[1], stream_format=stream_format)

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
                st.markdown(f"**Vendor:** `{active_state['sap_vendor_code']}`")
                st.markdown(f"**Boom Barrier:** :green[**● {active_state['boom_barrier_state']}**]")

        # 3. SAP S/4HANA ERP Seamless Integration Module
        st.markdown("#### 🔗 Seamless SAP S/4HANA ERP Integration")
        with st.container(border=True):
            sap_h1, sap_h2 = st.columns([2, 1.2])
            with sap_h1:
                st.caption("ENTERPRISE RFC / ODATA SYNC")
                st.markdown("### SAP S/4HANA")
            with sap_h2:
                st.success("● CONNECTED (Latency: 12ms)")
            
            sap_c1, sap_c2 = st.columns(2)
            with sap_c1:
                st.markdown(f"**Mapped SAP PO Number:** `{active_state['sap_po_number']}`")
                st.markdown(f"**Automated MIGO Goods Receipt:** :green[**#{active_state['sap_migo_doc']}**]")
            with sap_c2:
                st.markdown("**Movement Type:** 101 GR against PO (Plant 2001)")
                st.markdown("**Weighment Discrepancy:** :green[**0.00% (Within ±0.5% PO Tolerance)**]")

        # Interactive Simulation Trigger
        col_btn1, col_btn2 = st.columns(2)
        with col_btn1:
            if st.button("⚡ Simulate Inbound Weighment", use_container_width=True, type="primary"):
                st.toast("TRUCK DETECTED: ANPR GJ-12-BW-9842 Verified. Auto-Weighing...", icon="⚖️")
                st.toast("SAP MIGO #5002918491 Generated & Committed in SAP S/4HANA!", icon="✅")
        with col_btn2:
            if st.button("🖨️ Re-Print SAP Weigh Slip", use_container_width=True):
                st.toast("Weigh Slip #WS-2026-10492 sent to Gate 1 Thermal Kiosk.", icon="📄")

    # 4. Comprehensive Truck Movements & SAP Posting Table
    st.markdown("---")
    st.markdown("#### 📋 Real-Time Inbound & Outbound Truck Log (Integrated with SAP S/4HANA)")
    st.caption("Showing 100% automated weighments, zero manual scalemaster interventions, and immediate MIGO/PGI document generation.")

    df_trucks = pd.DataFrame(truck_log)
    st.dataframe(
        df_trucks,
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
            "sap_po_so": st.column_config.TextColumn("SAP PO / SO"),
            "sap_doc": st.column_config.TextColumn("SAP Material Doc"),
            "weight_slip": st.column_config.TextColumn("Weight Slip #"),
            "status": st.column_config.TextColumn("Gate Status")
        }
    )
