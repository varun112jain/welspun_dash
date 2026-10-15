"""
KPI and Container Components for Welspun Dashboard
"""
import streamlit as st

def render_kpi_card(label: str, value: str, delta: str = None, delta_positive: bool = True, subtext: str = ""):
    """Renders a custom styled KPI card in Welspun Blue style."""
    delta_html = ""
    if delta:
        delta_class = "positive" if delta_positive else "negative"
        arrow = "▲" if delta_positive else "▼"
        delta_html = f'<div class="kpi-delta {delta_class}">{arrow} {delta} <span style="color:#64748B; font-weight: normal;">{subtext}</span></div>'
    
    html = f"""
    <div class="kpi-card">
        <div class="kpi-label">{label}</div>
        <div class="kpi-value">{value}</div>
        {delta_html}
    </div>
    """
    st.markdown(html, unsafe_allow_html=True)

def render_notification_banner(message: str, icon: str = "⏳"):
    """Renders an informative Welspun themed notification banner."""
    html = f"""
    <div class="welspun-banner">
        <span style="font-size: 1.4rem;">{icon}</span>
        <div>{message}</div>
    </div>
    """
    st.markdown(html, unsafe_allow_html=True)
