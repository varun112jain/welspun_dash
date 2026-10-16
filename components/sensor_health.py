"""
Smoke and Fire Sensor Health Telemetry Components
Resilient across all Python & Plotly runtime environments.
"""
import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from styles.welspun_theme import WELSPUN_COLORS

def render_sensor_health_gauge(health_pct: float = 99.4):
    """Renders a gauge showing overall networked smoke & fire sensor network health with resilient fallback."""
    try:
        fig = go.Figure(go.Indicator(
            mode="gauge+number",
            value=float(health_pct),
            number={'suffix': "%", 'font': {'size': 26, 'color': WELSPUN_COLORS["primary"], 'weight': 700}},
            title={'text': "Sensor Network Health", 'font': {'size': 14, 'color': WELSPUN_COLORS["deep_navy"]}},
            gauge={
                'axis': {'range': [90.0, 100.0], 'tickwidth': 1, 'tickcolor': "#94A3B8"},
                'bar': {'color': "#10B981" if health_pct >= 98.0 else "#F59E0B", 'thickness': 0.28},
                'bgcolor': "white",
                'borderwidth': 1,
                'bordercolor': "#CBD5E1",
                'steps': [
                    {'range': [90.0, 95.0], 'color': "rgba(239, 68, 68, 0.2)"},
                    {'range': [95.0, 98.0], 'color': "rgba(245, 158, 11, 0.2)"},
                    {'range': [98.0, 100.0], 'color': "rgba(16, 185, 129, 0.25)"}
                ]
            }
        ))
        fig.update_layout(
            height=180,
            margin=dict(l=15, r=15, t=30, b=10),
            paper_bgcolor="rgba(0,0,0,0)"
        )
        return fig
    except Exception:
        return None

def render_sensor_health_panel(sensor_data: dict):
    """Renders the comprehensive smoke & fire detection network health matrix."""
    summary = sensor_data["summary"]
    categories = sensor_data["sensor_categories"]
    sectors = sensor_data["sector_breakdown"]
    
    st.markdown("### 🔥 Smoke & Fire Detection System Health")
    
    c_g, c_metrics = st.columns([1, 2])
    with c_g:
        fig_g = render_sensor_health_gauge(summary["overall_health_pct"])
        if fig_g is not None:
            try:
                st.plotly_chart(fig_g, use_container_width=True)
            except Exception:
                fig_g = None
                
        if fig_g is None:
            with st.container(border=True):
                st.caption("SENSOR NETWORK HEALTH")
                st.metric("Health Score", f"{summary['overall_health_pct']:.1f}%", "Target: > 98.0%")

    with c_metrics:
        with st.container(border=True):
            r1, r2 = st.columns(2)
            with r1:
                st.metric("Total Detectors", f"{summary['total_sensors']:,} Units")
                st.metric("Loop Bus Voltage", f"{summary['loop_voltage_vdc']} VDC", "Nominal")
            with r2:
                st.metric("Fully Operational", f"{summary['operational_sensors']:,}", f"{summary['overall_health_pct']}%")
                st.metric("Fiber Ring Bus", "DUAL REDUNDANT", "Active", delta_color="normal")
        
    st.markdown("#### 📡 Detector Categories & Drift Diagnostics")
    for cat in categories:
        with st.container(border=True):
            cat_c1, cat_c2 = st.columns([2, 1.2])
            with cat_c1:
                st.markdown(f"**{cat['type']}**")
                st.caption(f"Active: **{cat['healthy']} / {cat['total']}** ({cat['health_pct']}%)")
            with cat_c2:
                if cat['drift_warning'] > 0:
                    st.warning(f"⚠️ {cat['drift_warning']} Drift")
                else:
                    st.success("✓ Zero Drift")
                if cat['calibration_due'] > 0:
                    st.error(f"🔧 {cat['calibration_due']} Due")
                else:
                    st.success("✓ Calibrated")
        
    st.markdown("#### 🏭 Sector-wise Sensor Status")
    st.dataframe(
        sectors,
        use_container_width=True,
        hide_index=True,
        column_config={
            "sector": st.column_config.TextColumn("Sector / Facility"),
            "sensors": st.column_config.NumberColumn("Total Detectors"),
            "health": st.column_config.TextColumn("Health %"),
            "status": st.column_config.TextColumn("Network Status"),
            "last_test": st.column_config.TextColumn("Last Automated Ping")
        }
    )
