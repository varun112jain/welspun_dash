"""
Networked Fire Station & Emergency Command Components
"""
import streamlit as st
import plotly.graph_objects as go
from styles.welspun_theme import WELSPUN_COLORS

def render_hydrant_gauge(pressure_bar: float = 8.6, target_bar: float = 8.0) -> go.Figure:
    """Renders a high-precision Plotly gauge for the Anjar Fire Hydrant Ring pressure."""
    fig = go.Figure(go.Indicator(
        mode="gauge+number+delta",
        value=pressure_bar,
        domain={'x': [0, 1], 'y': [0, 1]},
        delta={'reference': target_bar, 'increasing': {'color': "#10B981"}, 'suffix': " Bar"},
        title={'text': "Anjar Ring Hydrant Pressure", 'font': {'size': 15, 'color': WELSPUN_COLORS["deep_navy"], 'family': 'sans-serif'}},
        number={'suffix': " Bar", 'font': {'size': 24, 'color': WELSPUN_COLORS["primary"], 'weight': 700}},
        gauge={
            'axis': {'range': [0, 14], 'tickwidth': 1, 'tickcolor': "#94A3B8"},
            'bar': {'color': WELSPUN_COLORS["primary"], 'thickness': 0.28},
            'bgcolor': "white",
            'borderwidth': 1,
            'bordercolor': "#CBD5E1",
            'steps': [
                {'range': [0, 6.0], 'color': "rgba(239, 68, 68, 0.25)"},
                {'range': [6.0, 7.5], 'color': "rgba(245, 158, 11, 0.25)"},
                {'range': [7.5, 10.5], 'color': "rgba(16, 185, 129, 0.3)"},
                {'range': [10.5, 14.0], 'color': "rgba(239, 68, 68, 0.25)"}
            ],
            'threshold': {
                'line': {'color': "#EF4444", 'width': 3},
                'thickness': 0.75,
                'value': target_bar
            }
        }
    ))
    fig.update_layout(
        height=220,
        margin=dict(l=15, r=15, t=35, b=10),
        paper_bgcolor="rgba(0,0,0,0)"
    )
    return fig

def render_fire_network_panel(fire_data: dict):
    """Renders the comprehensive networked fire command hub."""
    st.markdown("### 🚒 Networked Fire Station Command")
    
    col_st1, col_st2 = st.columns(2)
    
    stations = fire_data.get("stations", [])
    if len(stations) >= 2:
        with col_st1:
            st.markdown(
                f"""
                <div class="fire-panel" style="border-top: 3px solid #005BAA;">
                    <div class="fire-panel-header">
                        <span>🏢 {stations[0]['name']}</span>
                        <span style="color:#10B981; font-size:0.8rem; font-weight:700;">● {stations[0]['readiness']}</span>
                    </div>
                    <div style="font-size:0.85rem; color:#475569; margin-bottom:8px;">
                        <b>Crew on Duty:</b> {stations[0]['crew_on_duty']} Firefighters & Hazmat Techs<br>
                        <b>Primary Sector:</b> {stations[0]['coverage']}<br>
                        <b>Proximity to Plant Core:</b> {stations[0]['distance_to_core']}
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )
        with col_st2:
            st.markdown(
                f"""
                <div class="fire-panel" style="border-top: 3px solid #3071A9;">
                    <div class="fire-panel-header">
                        <span>🏡 {stations[1]['name']}</span>
                        <span style="color:#10B981; font-size:0.8rem; font-weight:700;">● {stations[1]['readiness']}</span>
                    </div>
                    <div style="font-size:0.85rem; color:#475569; margin-bottom:8px;">
                        <b>Crew on Duty:</b> {stations[1]['crew_on_duty']} Firefighters & EMS Officers<br>
                        <b>Primary Sector:</b> {stations[1]['coverage']}<br>
                        <b>Proximity to City Centre:</b> {stations[1]['distance_to_core']}
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )
            
    # Fleet Table & Dispatch
    st.markdown("#### 🚨 Fleet Readiness & Active Tenders")
    fleet = fire_data.get("fleet", [])
    
    for tender in fleet:
        is_dispatched = "Dispatched" in tender["status"]
        chip_class = "dispatched" if is_dispatched else ""
        status_badge = f"<span style='color:#EF4444; font-weight:bold;'>⚡ {tender['status']}</span>" if is_dispatched else f"<span style='color:#10B981; font-weight:bold;'>✓ {tender['status']}</span>"
        
        st.markdown(
            f"""
            <div class="tender-chip {chip_class}">
                <div>
                    <b>{tender['id']}</b> — {tender['name']}
                    <span style="color:#64748B; font-size:0.8rem; margin-left:8px;">({tender['station']})</span>
                </div>
                <div style="display:flex; align-items:center; gap:16px;">
                    <span style="color:#475569; font-size:0.8rem;">Fuel: <b>{tender['fuel']}</b> | Foam: <b>{tender['foam_lvl']}</b></span>
                    {status_badge}
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )
