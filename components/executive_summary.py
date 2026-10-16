"""
Executive Operations Summary & Analytical Intelligence Component for Welspun City, Anjar
Delivers an interactive operational briefing featuring multi-feed strategic video reels,
Plotly analytics graphics, autonomous AI mitigation metrics, and energy balance.
"""
import os
import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import importlib
import data.executive_data

# Reload data module to ensure freshest data definitions
importlib.reload(data.executive_data)

from styles.welspun_theme import WELSPUN_COLORS
from data.executive_data import (
    get_executive_kpis,
    get_executive_video_showcases,
    get_ai_prevention_breakdown,
    get_energy_generation_mix
)

def render_ai_prevention_donut(ai_data: dict) -> go.Figure:
    """Builds a high-impact donut chart displaying AI autonomous threat mitigations."""
    fig = go.Figure(data=[go.Pie(
        labels=ai_data["categories"],
        values=ai_data["counts"],
        hole=0.58,
        marker=dict(colors=ai_data["colors"]),
        textinfo="percent",
        hoverinfo="label+value+percent"
    )])

    fig.update_layout(
        height=320,
        margin=dict(l=10, r=10, t=20, b=20),
        showlegend=True,
        legend=dict(
            orientation="v",
            yanchor="middle",
            y=0.5,
            xanchor="left",
            x=1.02,
            font=dict(size=10)
        ),
        paper_bgcolor="#FFFFFF",
        annotations=[
            dict(
                text="<b>148</b><br><span style='font-size:10px; color:#64748B;'>PREVENTED</span>",
                x=0.5,
                y=0.5,
                font=dict(size=16, color="#0F172A"),
                showarrow=False
            )
        ]
    )
    return fig

def render_energy_mix_chart(energy_data: dict) -> go.Figure:
    """Builds an executive energy balance chart showing solar generation and captive thermal base."""
    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=energy_data["hours"],
        y=energy_data["demand_mw"],
        name="Plant Power Demand (MW)",
        mode="lines",
        line=dict(color="#0F172A", width=3)
    ))

    fig.add_trace(go.Scatter(
        x=energy_data["hours"],
        y=energy_data["cpp_thermal_mw"],
        name="123 MW Captive Power Plant",
        mode="lines",
        fill="tozeroy",
        line=dict(color="#005BAA", width=1.5),
        fillcolor="rgba(0, 91, 170, 0.25)"
    ))

    fig.add_trace(go.Scatter(
        x=energy_data["hours"],
        y=[c + s for c, s in zip(energy_data["cpp_thermal_mw"], energy_data["solar_mw"])],
        name="Total Gen (CPP + 42MW Solar)",
        mode="lines",
        fill="tonexty",
        line=dict(color="#10B981", width=2),
        fillcolor="rgba(16, 185, 129, 0.35)"
    ))

    fig.update_layout(
        height=320,
        margin=dict(l=20, r=20, t=30, b=20),
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1,
            font=dict(size=11)
        ),
        plot_bgcolor="#FFFFFF",
        paper_bgcolor="#FFFFFF",
        xaxis=dict(
            title=dict(text="Time of Day (24-Hour Cycle)", font=dict(size=11, color="#64748B")),
            showgrid=False,
            color="#334155"
        ),
        yaxis=dict(
            title=dict(text="Megawatts (MW)", font=dict(size=11, color="#64748B")),
            gridcolor="#F1F5F9",
            color="#334155"
        ),
        hovermode="x unified"
    )
    return fig

def render_executive_video_item(video_info: dict, stream_format: str = "Live Stream"):
    """Renders a single executive video tile with live animation, status HUD, and business impact."""
    with st.container(border=True):
        # Header HUD using native columns
        h_left, h_right = st.columns([2.2, 1.2])
        with h_left:
            st.caption(video_info['sector'].upper())
            st.markdown(f"**{video_info['title']}**")
        with h_right:
            if "PATROL" in video_info["status"] or "CRITICAL" in video_info["status"]:
                st.error(video_info["status"])
            else:
                st.success(video_info["status"])
            st.caption(f"Camera: `{video_info['camera_id']}`")

        # Video / GIF feed rendering
        gif_path = video_info.get("gif", "")
        vid_path = video_info.get("video", "")
        img_path = video_info.get("image", "")

        rendered = False
        if stream_format == "MP4" and vid_path and os.path.exists(vid_path):
            try:
                st.video(vid_path, loop=True, autoplay=True, muted=True)
                rendered = True
            except Exception:
                rendered = False

        if not rendered and stream_format != "Snapshot" and gif_path and os.path.exists(gif_path):
            st.image(gif_path, use_container_width=True)
            rendered = True

        if not rendered and img_path and os.path.exists(img_path):
            st.image(img_path, use_container_width=True)
            rendered = True

        if not rendered:
            st.error(f"Feed offline: {video_info['title']}")

        # Operational Metric & Real-Time Telemetry
        m_left, m_right = st.columns([1.5, 1.5])
        with m_left:
            st.metric(label=video_info['kpi_label'], value=video_info['kpi_value'])
        with m_right:
            st.caption("TELEMETRY")
            st.markdown(f"*{video_info['telemetry']}*")

def render_executive_summary_screen(stream_format: str = "Live Stream"):
    """Renders the comprehensive Executive Operations & Plant Intelligence Screen."""
    kpis = get_executive_kpis()
    videos = get_executive_video_showcases()
    ai_data = get_ai_prevention_breakdown()
    energy_data = get_energy_generation_mix()

    # 1. Executive Operations Banner
    with st.container(border=True):
        b1, b2, b3 = st.columns([2.5, 1, 1])
        with b1:
            st.caption("WELSPUN GROUP • INTEGRATED PLANT OPERATIONS SUMMARY")
            st.markdown("### Executive Operations, Safety & Surveillance Intelligence")
            st.caption("Consolidated 24/7 operational safety, surveillance, and security telemetry across the 2,500-Acre Anjar Mega Complex.")
        with b2:
            st.metric("CCTV Camera Uptime", "99.0%", "1,424 Feeds Online")
        with b3:
            st.metric("Workforce on Duty", "14,820", "Active on Shift")

    # Safe fallbacks to prevent any KeyError across module reloads
    cctv_kpi = kpis.get('cctv_network_health') or kpis.get('complex_output') or {
        'title': 'CCTV Surveillance Mesh',
        'value': '1,424 / 1,438',
        'target': '99.0% Operational',
        'delta': '14 Maint Loops'
    }
    safe_kpi = kpis.get('safe_man_hours') or {
        'title': 'Safety & LTI Streak',
        'value': '1,420 DAYS',
        'delta': 'Zero Fatalities / LTI',
        'target': '18.4M Safe Hours'
    }
    log_kpi = kpis.get('logistics_automation') or {
        'title': 'Weighbridge Automation',
        'value': '99.4%',
        'delta': '100% Paperless MIGO',
        'target': '1,842 Trucks Handled'
    }
    sap_kpi = kpis.get('sap_transacted_value') or {
        'title': 'Automated SAP Velocity',
        'value': '₹42.8 Cr',
        'target': 'Daily Inbound/Outbound',
        'delta': '+12ms RFC Latency'
    }
    clean_kpi = kpis.get('clean_energy_share') or {
        'title': 'Green Energy & Self-Reliance',
        'value': '100%',
        'delta': '14 MW Export to Grid',
        'target': '165 MW Total Generation'
    }
    ai_kpi = kpis.get('ai_threat_prevention') or {
        'title': 'AI Autonomous Interceptions',
        'value': '148 Events',
        'delta': 'Zero Asset Loss',
        'target': '100% Mitigated'
    }

    # 2. Executive KPI Cards Row (6 Equal Responsive Cards)
    st.html(
        f"""
        <div class="kpi-grid" style="margin-bottom:1.2rem;">
            <div class="surv-kpi-card optimal" style="border-left-color: #005BAA;">
                <div class="surv-kpi-label">{cctv_kpi['title']}</div>
                <div class="surv-kpi-val" style="color:#005BAA;">{cctv_kpi['value']}</div>
                <div class="surv-kpi-sub"><b>{cctv_kpi['target']}</b> • {cctv_kpi['delta']}</div>
            </div>
            <div class="surv-kpi-card optimal" style="border-left-color: #10B981;">
                <div class="surv-kpi-label">{safe_kpi['title']}</div>
                <div class="surv-kpi-val" style="color:#059669;">{safe_kpi['value']}</div>
                <div class="surv-kpi-sub"><b>{safe_kpi['delta']}</b> ({safe_kpi['target']})</div>
            </div>
            <div class="surv-kpi-card optimal" style="border-left-color: #00A6E6;">
                <div class="surv-kpi-label">{log_kpi['title']}</div>
                <div class="surv-kpi-val" style="color:#0284C7;">{log_kpi['value']}</div>
                <div class="surv-kpi-sub"><b>{log_kpi['delta']}</b> • {log_kpi['target']}</div>
            </div>
            <div class="surv-kpi-card optimal" style="border-left-color: #005BAA;">
                <div class="surv-kpi-label">{sap_kpi['title']}</div>
                <div class="surv-kpi-val" style="color:#005BAA;">{sap_kpi['value']}</div>
                <div class="surv-kpi-sub"><b>{sap_kpi['target']}</b> ({sap_kpi['delta']})</div>
            </div>
            <div class="surv-kpi-card optimal" style="border-left-color: #10B981;">
                <div class="surv-kpi-label">{clean_kpi['title']}</div>
                <div class="surv-kpi-val" style="color:#059669;">{clean_kpi['value']}</div>
                <div class="surv-kpi-sub"><b>{clean_kpi['delta']}</b> • {clean_kpi['target']}</div>
            </div>
            <div class="surv-kpi-card optimal" style="border-left-color: #00A6E6;">
                <div class="surv-kpi-label">{ai_kpi['title']}</div>
                <div class="surv-kpi-val" style="color:#0284C7;">{ai_kpi['value']}</div>
                <div class="surv-kpi-sub"><b>{ai_kpi['delta']}</b> ({ai_kpi['target']})</div>
            </div>
        </div>
        """
    )

    # 3. Operational Video Showcase Reel (2x2 Grid with Video & Telemetry Overlays)
    st.markdown("### 🎥 Key Plant Operational Video Telemetry")
    st.caption("Live video monitoring covering Heavy Metallurgy, Blast Furnace Tapping, Unmanned SAP Logistics, and 220kV Critical Perimeter.")

    row1_c1, row1_c2 = st.columns(2)
    with row1_c1:
        render_executive_video_item(videos[0], stream_format=stream_format)
    with row1_c2:
        render_executive_video_item(videos[1], stream_format=stream_format)

    row2_c1, row2_c2 = st.columns(2)
    with row2_c1:
        render_executive_video_item(videos[2], stream_format=stream_format)
    with row2_c2:
        render_executive_video_item(videos[3], stream_format=stream_format)

    st.markdown("---")

    # 4. Interactive Analytical Graphics & Visualizations (Plotly)
    st.markdown("### 📈 Safety Intelligence, Threat Mitigation & Clean Energy Balance")
    st.caption("Real-time vision AI safety interventions, automated perimeter defense, and captive clean energy distribution.")

    col_g1, col_g2 = st.columns(2)

    with col_g1:
        st.markdown("##### 🛡️ Autonomous AI Safety & Anomaly Prevention Breakdown")
        fig_ai = render_ai_prevention_donut(ai_data)
        st.plotly_chart(fig_ai, use_container_width=True)

    with col_g2:
        st.markdown("##### ⚡ 24-Hour Captive Clean Energy Generation vs Complex Demand")
        fig_energy = render_energy_mix_chart(energy_data)
        st.plotly_chart(fig_energy, use_container_width=True)
