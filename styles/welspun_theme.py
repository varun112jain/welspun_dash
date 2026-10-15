"""
Welspun Branding & Theme Utilities for Streamlit
"""
import os
import streamlit as st
import plotly.graph_objects as go
import plotly.io as pio

# Welspun Official Brand Color Palette
WELSPUN_COLORS = {
    "primary": "#005BAA",        # Official Welspun Blue
    "royal": "#2C2B7C",          # Deep Welspun Royal / Corporate Blue
    "astral": "#3071A9",         # Astral Blue
    "deep_navy": "#0B2545",      # Deep Navy Accent
    "cyan": "#00A6E6",           # Welspun Spark Cyan
    "steel_grey": "#919496",     # Brand Silver / Steel Grey
    "light_bg": "#F8FAFC",       # Page Background
    "light_blue": "#EEF4FA",     # Card Background
    "border_blue": "#D0E1F5",    # Card Borders
    "success": "#10B981",        # Positive status
    "warning": "#F59E0B",        # Alert status
    "danger": "#EF4444"          # Critical status
}

# Plotly Theme Color Sequence
WELSPUN_SEQUENCE = [
    "#005BAA",  # Primary Blue
    "#00A6E6",  # Spark Cyan
    "#2C2B7C",  # Royal Blue
    "#3071A9",  # Astral
    "#4B6584",  # Slate
    "#20BF6B",  # Emerald
    "#FA8231",  # Amber/Orange
    "#8854D0"   # Purple
]

def load_css():
    """Load the Welspun custom CSS stylesheet into the Streamlit session."""
    css_file_path = os.path.join(os.path.dirname(__file__), "theme.css")
    if os.path.exists(css_file_path):
        with open(css_file_path, "r", encoding="utf-8") as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

def style_plotly_chart(fig: go.Figure, height: int = 380, title: str = "") -> go.Figure:
    """Applies clean, responsive Welspun corporate styling to any Plotly figure."""
    fig.update_layout(
        title={
            "text": title,
            "font": {"size": 16, "family": "Inter, Roboto, sans-serif", "color": WELSPUN_COLORS["deep_navy"], "weight": 600},
            "x": 0.02,
            "y": 0.95
        } if title else None,
        height=height,
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(248,250,252,0.6)",
        font={"family": "Inter, Roboto, sans-serif", "color": "#334155"},
        margin=dict(l=20, r=20, t=50 if title else 25, b=25),
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1,
            bgcolor="rgba(255,255,255,0.7)",
            bordercolor=WELSPUN_COLORS["border_blue"],
            borderwidth=1
        ),
        xaxis=dict(
            gridcolor="#E2E8F0",
            linecolor="#CBD5E1",
            zerolinecolor="#E2E8F0"
        ),
        yaxis=dict(
            gridcolor="#E2E8F0",
            linecolor="#CBD5E1",
            zerolinecolor="#E2E8F0"
        )
    )
    return fig
