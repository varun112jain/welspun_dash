"""
Networked Fire Station & Emergency Command Components
"""
import streamlit as st
import plotly.graph_objects as go
from styles.welspun_theme import WELSPUN_COLORS

def render_hydrant_gauge(pressure_bar: float = 8.6, target_bar: float = 8.0):
    """Renders a high-precision Plotly gauge for the Anjar Fire Hydrant Ring pressure with resilient fallback."""
    try:
        fig = go.Figure(go.Indicator(
            mode="gauge+number+delta",
            value=float(pressure_bar),
            domain={'x': [0, 1], 'y': [0, 1]},
            delta={'reference': float(target_bar), 'increasing': {'color': "#10B981"}, 'suffix': " Bar"},
            title={'text': "Anjar Ring Hydrant Pressure", 'font': {'size': 15, 'color': WELSPUN_COLORS["deep_navy"], 'family': 'sans-serif'}},
            number={'suffix': " Bar", 'font': {'size': 24, 'color': WELSPUN_COLORS["primary"], 'weight': 700}},
            gauge={
                'axis': {'range': [0.0, 14.0], 'tickwidth': 1, 'tickcolor': "#94A3B8"},
                'bar': {'color': WELSPUN_COLORS["primary"], 'thickness': 0.28},
                'bgcolor': "white",
                'borderwidth': 1,
                'bordercolor': "#CBD5E1",
                'steps': [
                    {'range': [0.0, 6.0], 'color': "rgba(239, 68, 68, 0.25)"},
                    {'range': [6.0, 7.5], 'color': "rgba(245, 158, 11, 0.25)"},
                    {'range': [7.5, 10.5], 'color': "rgba(16, 185, 129, 0.3)"},
                    {'range': [10.5, 14.0], 'color': "rgba(239, 68, 68, 0.25)"}
                ],
                'threshold': {
                    'line': {'color': "#EF4444", 'width': 3},
                    'thickness': 0.75,
                    'value': float(target_bar)
                }
            }
        ))
        fig.update_layout(
            height=220,
            margin=dict(l=15, r=15, t=35, b=10),
            paper_bgcolor="rgba(0,0,0,0)"
        )
        return fig
    except Exception:
        return None

def render_fire_network_panel(fire_data: dict):
    """Renders the comprehensive networked fire command hub."""
    st.markdown("### 🚒 Networked Fire Station Command")
    
    col_st1, col_st2 = st.columns(2)
    
    stations = fire_data.get("stations", [])
    if len(stations) >= 2:
        with col_st1:
            with st.container(border=True):
                h1, h2 = st.columns([2, 1.2])
                with h1:
                    st.markdown(f"**🏢 {stations[0]['name']}**")
                with h2:
                    st.success(f"● {stations[0]['readiness']}")
                st.caption(f"Crew on Duty: **{stations[0]['crew_on_duty']} Firefighters & Hazmat Techs**")
                st.caption(f"Sector: **{stations[0]['coverage']}** | Core Proximity: **{stations[0]['distance_to_core']}**")
        with col_st2:
            with st.container(border=True):
                h1, h2 = st.columns([2, 1.2])
                with h1:
                    st.markdown(f"**🏡 {stations[1]['name']}**")
                with h2:
                    st.success(f"● {stations[1]['readiness']}")
                st.caption(f"Crew on Duty: **{stations[1]['crew_on_duty']} Firefighters & EMS Officers**")
                st.caption(f"Sector: **{stations[1]['coverage']}** | Proximity: **{stations[1]['distance_to_core']}**")
            
    # Fleet Table & Dispatch
    st.markdown("#### 🚨 Fleet Readiness & Active Tenders")
    fleet = fire_data.get("fleet", [])
    
    for tender in fleet:
        is_dispatched = "Dispatched" in tender["status"]
        with st.container(border=True):
            t1, t2 = st.columns([2, 1.2])
            with t1:
                st.markdown(f"**{tender['id']}** — {tender['name']} `({tender['station']})`")
                st.caption(f"Fuel: **{tender['fuel']}** | Foam: **{tender['foam_lvl']}**")
            with t2:
                if is_dispatched:
                    st.error(f"⚡ {tender['status']}")
                else:
                    st.success(f"✓ {tender['status']}")
