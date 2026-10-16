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

    # 1. Top KPI Row
    st.markdown(
        f"""
        <div class="kpi-grid" style="grid-template-columns: repeat(6, 1fr); margin-bottom:1rem;">
            <div class="surv-kpi-card optimal" style="border-left-color: #005BAA;">
                <div class="surv-kpi-label">Truck Traffic Today</div>
                <div class="surv-kpi-val" style="color:#005BAA;">{kpi_data['trucks_today']['value']}</div>
                <div class="surv-kpi-sub"><b>{kpi_data['trucks_today']['sub']}</b></div>
            </div>
            <div class="surv-kpi-card optimal" style="border-left-color: #10B981;">
                <div class="surv-kpi-label">Weighbridge Automation</div>
                <div class="surv-kpi-val" style="color:#059669;">{kpi_data['unmanned_pct']['value']}</div>
                <div class="surv-kpi-sub"><b>{kpi_data['unmanned_pct']['sub']}</b></div>
            </div>
            <div class="surv-kpi-card optimal" style="border-left-color: #00A6E6;">
                <div class="surv-kpi-label">Avg Gate Turnaround</div>
                <div class="surv-kpi-val" style="color:#0284C7;">{kpi_data['avg_turnaround_min']['value']}</div>
                <div class="surv-kpi-sub"><b>{kpi_data['avg_turnaround_min']['sub']}</b></div>
            </div>
            <div class="surv-kpi-card optimal" style="border-left-color: #10B981;">
                <div class="surv-kpi-label">SAP S/4HANA Sync</div>
                <div class="surv-kpi-val" style="color:#059669;">{kpi_data['sap_sync_health']['value']}</div>
                <div class="surv-kpi-sub"><b>{kpi_data['sap_sync_health']['sub']}</b></div>
            </div>
            <div class="surv-kpi-card optimal" style="border-left-color: #005BAA;">
                <div class="surv-kpi-label">Active Scales</div>
                <div class="surv-kpi-val" style="color:#005BAA;">{kpi_data['active_weighbridges']['value']}</div>
                <div class="surv-kpi-sub">{kpi_data['active_weighbridges']['sub']}</div>
            </div>
            <div class="surv-kpi-card optimal" style="border-left-color: #10B981;">
                <div class="surv-kpi-label">Tolerance / Compliance</div>
                <div class="surv-kpi-val" style="color:#059669;">{kpi_data['weight_tolerance']['value']}</div>
                <div class="surv-kpi-sub"><b>{kpi_data['weight_tolerance']['sub']}</b></div>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

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
        st.markdown(
            """
            <div style="background:#0F172A; border:1px solid #334155; border-radius:8px; padding:12px 16px; margin-top:4px;">
                <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:8px;">
                    <span style="color:#38BDF8; font-size:0.78rem; font-weight:700; text-transform:uppercase; letter-spacing:0.05em;">
                        Automated UVIS Undercarriage &amp; Container Seal AI Scanner
                    </span>
                    <span style="background:rgba(16, 185, 129, 0.2); color:#10B981; font-size:0.72rem; font-weight:700; padding:2px 8px; border-radius:4px; border:1px solid #059669;">
                        ● SCAN CLEAR • ZERO ANOMALIES
                    </span>
                </div>
                <div style="display:grid; grid-template-columns:repeat(3, 1fr); gap:10px; font-size:0.78rem; color:#CBD5E1;">
                    <div>Chassis Foreign Object: <b style="color:#10B981;">CLEARED (0 Detect)</b></div>
                    <div>Container Door Seal: <b style="color:#38BDF8;">#WLP-SEAL-8894 INTACT</b></div>
                    <div>FASTag RFID ID: <b style="color:#A78BFA;">3416-1FA8-9920-55B1</b></div>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col_tele_right:
        st.markdown("#### ⚖️ Unmanned Weighbridge Automation Platform (WB-01)")
        
        # Live Digital Weight Scale Display (Industrial look)
        gross_wt = active_state["gross_weight_kg"]
        tare_wt = active_state["tare_weight_kg"]
        net_wt = active_state["net_weight_kg"]

        st.markdown(
            f"""
            <div style="background:#020617; border:2px solid #005BAA; border-radius:10px; padding:16px; color:#FFFFFF; margin-bottom:12px; box-shadow:0 4px 18px rgba(0, 91, 170, 0.25);">
                <div style="display:flex; justify-content:space-between; align-items:center; border-bottom:1px solid #1E293B; padding-bottom:8px; margin-bottom:12px;">
                    <div>
                        <span style="font-size:0.72rem; color:#38BDF8; text-transform:uppercase; font-weight:700; letter-spacing:0.06em;">Digital Load Cell Weighment Indicator</span><br>
                        <b style="font-size:1.05rem; color:#F8FAFC;">{active_state['truck_plate']}</b> 
                        <span style="font-size:0.8rem; color:#94A3B8;">({active_state['transporter']})</span>
                    </div>
                    <div style="text-align:right;">
                        <span style="background:#10B981; color:#020617; font-weight:800; font-size:0.78rem; padding:3px 8px; border-radius:4px;">
                            WEIGHT STABILIZED
                        </span><br>
                        <span style="font-size:0.72rem; color:#94A3B8;">Ticket: {active_state['weight_slip_no']}</span>
                    </div>
                </div>
                
                <div style="display:grid; grid-template-columns:repeat(3, 1fr); gap:8px; text-align:center; background:#0F172A; padding:12px; border-radius:8px; border:1px solid #334155;">
                    <div>
                        <div style="font-size:0.70rem; color:#94A3B8; text-transform:uppercase;">Gross Weight</div>
                        <div style="font-size:1.55rem; font-weight:800; color:#38BDF8; font-family:monospace;">{gross_wt:,} KG</div>
                        <div style="font-size:0.68rem; color:#64748B;">±0.0 kg stability</div>
                    </div>
                    <div style="border-left:1px solid #334155; border-right:1px solid #334155;">
                        <div style="font-size:0.70rem; color:#94A3B8; text-transform:uppercase;">Tare Weight</div>
                        <div style="font-size:1.55rem; font-weight:800; color:#CBD5E1; font-family:monospace;">{tare_wt:,} KG</div>
                        <div style="font-size:0.68rem; color:#64748B;">Registered RTO Baseline</div>
                    </div>
                    <div>
                        <div style="font-size:0.70rem; color:#94A3B8; text-transform:uppercase;">Net Material Wt</div>
                        <div style="font-size:1.55rem; font-weight:800; color:#10B981; font-family:monospace;">{net_wt:,} KG</div>
                        <div style="font-size:0.68rem; color:#10B981; font-weight:600;">28.63 Metric Tons</div>
                    </div>
                </div>

                <div style="margin-top:12px; font-size:0.78rem; color:#CBD5E1; background:rgba(0,0,0,0.4); padding:10px; border-radius:6px;">
                    <div style="display:flex; justify-content:space-between; margin-bottom:4px;">
                        <span><b>Cargo Material:</b> {active_state['material']}</span>
                        <span style="color:#38BDF8;"><b>Vendor:</b> {active_state['sap_vendor_code']}</span>
                    </div>
                    <div style="display:flex; justify-content:space-between; align-items:center; border-top:1px solid #1E293B; padding-top:6px; margin-top:6px;">
                        <span><b>IR Platform Position:</b> <span style="color:#10B981;">✓ 100% On-Deck (Zero Overhang)</span></span>
                        <span><b>Boom Barrier:</b> <span style="color:#10B981; font-weight:bold;">● {active_state['boom_barrier_state']}</span></span>
                    </div>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

        # 3. SAP S/4HANA ERP Seamless Integration Module
        st.markdown("#### 🔗 Seamless SAP S/4HANA ERP Integration")
        st.markdown(
            f"""
            <div style="background:#FFFFFF; border:1px solid #CBD5E1; border-top:4px solid #005BAA; border-radius:10px; padding:14px 16px; margin-bottom:12px; box-shadow:0 2px 10px rgba(0,0,0,0.04);">
                <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:10px;">
                    <div style="display:flex; align-items:center; gap:8px;">
                        <span style="background:#005BAA; color:#FFFFFF; font-weight:800; font-size:0.78rem; padding:3px 8px; border-radius:4px;">SAP S/4HANA</span>
                        <b style="font-size:0.92rem; color:#0F172A;">Enterprise RFC / OData Sync</b>
                    </div>
                    <span style="color:#10B981; font-size:0.78rem; font-weight:700;">
                        ● CONNECTED (Latency: 12ms)
                    </span>
                </div>
                
                <div style="background:#F8FAFC; border:1px solid #E2E8F0; border-radius:8px; padding:10px; font-size:0.80rem; color:#334155; line-height:1.5;">
                    <div style="display:flex; justify-content:space-between; margin-bottom:4px;">
                        <span><b>Mapped SAP PO Number:</b></span>
                        <span style="color:#005BAA; font-weight:700;">{active_state['sap_po_number']}</span>
                    </div>
                    <div style="display:flex; justify-content:space-between; margin-bottom:4px;">
                        <span><b>Automated MIGO Goods Receipt Doc:</b></span>
                        <span style="color:#10B981; font-weight:700;">#{active_state['sap_migo_doc']}</span>
                    </div>
                    <div style="display:flex; justify-content:space-between; margin-bottom:4px;">
                        <span><b>Movement Type:</b></span>
                        <span><b>101 GR against PO</b> (Plant 2001 - Anjar Mega Complex)</span>
                    </div>
                    <div style="display:flex; justify-content:space-between;">
                        <span><b>Weighment Discrepancy:</b></span>
                        <span style="color:#10B981; font-weight:600;">0.00% (Within ±0.5% PO Tolerance)</span>
                    </div>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

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
