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
            # Fallback high-impact metric tile
            st.html(
                f"""
                <div style="background:#FFFFFF; border:1px solid #CBD5E1; border-radius:10px; padding:18px; text-align:center; box-shadow:0 2px 8px rgba(0,0,0,0.05); margin-top:10px;">
                    <div style="font-size:0.8rem; color:#475569; text-transform:uppercase; font-weight:700;">Sensor Network Health</div>
                    <div style="font-size:2.4rem; font-weight:800; color:#10B981; margin:4px 0;">{summary['overall_health_pct']:.1f}%</div>
                    <div style="font-size:0.8rem; color:#64748B;">Target: &gt; 98.0% Operational</div>
                </div>
                """
            )
        
    with c_metrics:
        st.html(
            f"""
            <div style="background:#F8FAFC; border:1px solid #CBD5E1; border-radius:10px; padding:14px; margin-top:10px;">
                <div style="display:grid; grid-template-columns: repeat(2, 1fr); gap:12px;">
                    <div>
                        <span style="font-size:0.75rem; color:#64748B; text-transform:uppercase;">Total Networked Detectors</span><br>
                        <b style="font-size:1.3rem; color:#0F172A;">{summary['total_sensors']:,} Units</b>
                    </div>
                    <div>
                        <span style="font-size:0.75rem; color:#64748B; text-transform:uppercase;">Fully Operational</span><br>
                        <b style="font-size:1.3rem; color:#10B981;">{summary['operational_sensors']:,} ({summary['overall_health_pct']}%)</b>
                    </div>
                    <div>
                        <span style="font-size:0.75rem; color:#64748B; text-transform:uppercase;">Loop Bus Voltage</span><br>
                        <b style="font-size:1.1rem; color:#005BAA;">{summary['loop_voltage_vdc']} VDC (Nominal)</b>
                    </div>
                    <div>
                        <span style="font-size:0.75rem; color:#64748B; text-transform:uppercase;">Fiber Ring Bus</span><br>
                        <b style="font-size:0.95rem; color:#10B981;">● DUAL REDUNDANT OK</b>
                    </div>
                </div>
            </div>
            """
        )
        
    st.markdown("#### 📡 Detector Categories & Drift Diagnostics")
    for cat in categories:
        drift_badge = f"<span style='color:#F59E0B; font-weight:bold;'>⚠️ {cat['drift_warning']} Drift Warnings</span>" if cat['drift_warning'] > 0 else "<span style='color:#10B981;'>✓ Zero Drift</span>"
        cal_badge = f"<span style='color:#EF4444; font-weight:bold;'>🔧 {cat['calibration_due']} Due</span>" if cat['calibration_due'] > 0 else "<span style='color:#10B981;'>✓ Calibrated</span>"
        
        st.html(
            f"""
            <div style="background:#FFFFFF; border:1px solid #E2E8F0; border-radius:8px; padding:10px 14px; margin-bottom:8px; display:flex; justify-content:space-between; align-items:center;">
                <div>
                    <b>{cat['type']}</b><br>
                    <span style="font-size:0.8rem; color:#64748B;">Active: <b>{cat['healthy']} / {cat['total']}</b> ({cat['health_pct']}%)</span>
                </div>
                <div style="display:flex; gap:16px; font-size:0.82rem;">
                    <div>{drift_badge}</div>
                    <div>{cal_badge}</div>
                </div>
            </div>
            """
        )
        
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
