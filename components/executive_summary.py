"""
Executive Summary & Boardroom Intelligence Screen Component for Welspun City, Anjar
Delivers an interactive high-level briefing featuring multi-feed strategic video reels,
Plotly analytics graphics, autonomous AI mitigation metrics, and leadership directives.
"""
import os
import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from styles.welspun_theme import WELSPUN_COLORS
from data.executive_data import (
    get_executive_kpis,
    get_executive_video_showcases,
    get_hourly_production_series,
    get_ai_prevention_breakdown,
    get_energy_generation_mix,
    get_strategic_milestones
)

def render_production_velocity_chart(prod_data: dict) -> go.Figure:
    """Builds an executive-grade production velocity chart with hourly breakdown and target line."""
    fig = go.Figure()
    
    # Division bars
    fig.add_trace(go.Bar(
        x=prod_data["hours"],
        y=prod_data["wcl_pipes"],
        name="WCL LSAW/Spiral Pipes",
        marker_color="#005BAA"
    ))
    fig.add_trace(go.Bar(
        x=prod_data["hours"],
        y=prod_data["wdi_iron"],
        name="WDI Blast Furnace & DI",
        marker_color="#00A6E6"
    ))
    fig.add_trace(go.Bar(
        x=prod_data["hours"],
        y=prod_data["wll_textiles"],
        name="WLL Spunlace Textiles",
        marker_color="#10B981"
    ))
    
    # Target benchmark line
    fig.add_trace(go.Scatter(
        x=prod_data["hours"],
        y=prod_data["target_hourly"],
        name="Complex Target (650 MT/h)",
        mode="lines",
        line=dict(color="#EF4444", width=2.5, dash="dash")
    ))

    fig.update_layout(
        barmode="stack",
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
            title=dict(text="Operating Hour", font=dict(size=11, color="#64748B")),
            showgrid=False,
            color="#334155"
        ),
        yaxis=dict(
            title=dict(text="Output (Metric Tons)", font=dict(size=11, color="#64748B")),
            gridcolor="#F1F5F9",
            color="#334155"
        ),
        hovermode="x unified"
    )
    return fig

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
        # Header HUD
        badge_color = "#EF4444" if "PATROL" in video_info["status"] or "CRITICAL" in video_info["status"] else "#10B981"
        pulse_dot = '<span class="pulse-dot-red"></span>' if "PATROL" in video_info["status"] else '<span class="pulse-dot-green"></span>'

        st.html(
            f"""
            <div style="background:#020617; color:#FFFFFF; padding:8px 12px; border-radius:6px; margin-bottom:8px; border:1px solid #1E293B; display:flex; justify-content:space-between; align-items:center;">
                <div>
                    <span style="font-size:0.70rem; color:#38BDF8; text-transform:uppercase; font-weight:700; letter-spacing:0.06em;">{video_info['sector']}</span><br>
                    <b style="font-size:0.90rem; color:#F8FAFC;">{video_info['title']}</b>
                </div>
                <div style="text-align:right;">
                    <span style="background:{badge_color}; color:#FFFFFF; font-size:0.70rem; font-weight:800; padding:2px 7px; border-radius:4px;">
                        {pulse_dot} {video_info['status']}
                    </span><br>
                    <span style="font-size:0.70rem; color:#94A3B8; font-family:monospace;">{video_info['camera_id']}</span>
                </div>
            </div>
            """
        )

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

        # Executive Strategic Metric Footer
        st.html(
            f"""
            <div style="background:#0F172A; border-radius:6px; padding:10px 12px; margin-top:8px; border:1px solid #1E293B; font-size:0.78rem;">
                <div style="display:flex; justify-content:space-between; align-items:center; border-bottom:1px solid #1E293B; padding-bottom:6px; margin-bottom:6px;">
                    <span style="color:#94A3B8; text-transform:uppercase; font-size:0.70rem; font-weight:700;">{video_info['kpi_label']}</span>
                    <b style="color:#38BDF8; font-size:1.02rem; font-family:monospace;">{video_info['kpi_value']}</b>
                </div>
                <div style="color:#CBD5E1; margin-bottom:4px;">
                    <b>Telemetry:</b> {video_info['telemetry']}
                </div>
                <div style="color:#34D399; font-size:0.74rem;">
                    <b>Strategic Impact:</b> {video_info['strategic_impact']}
                </div>
            </div>
            """
        )

def render_executive_summary_screen(stream_format: str = "Live Stream"):
    """Renders the comprehensive Executive Summary & Boardroom Intelligence Screen."""
    kpis = get_executive_kpis()
    videos = get_executive_video_showcases()
    prod_data = get_hourly_production_series()
    ai_data = get_ai_prevention_breakdown()
    energy_data = get_energy_generation_mix()
    milestones = get_strategic_milestones()

    # 1. Executive Boardroom Banner
    st.html(
        """
        <div style="background:linear-gradient(135deg, #0A192F 0%, #005BAA 60%, #00A6E6 100%); color:#FFFFFF; padding:16px 20px; border-radius:10px; margin-bottom:14px; box-shadow:0 4px 18px rgba(0, 91, 170, 0.25); display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:12px;">
            <div>
                <div style="font-size:0.72rem; text-transform:uppercase; letter-spacing:0.12em; color:#BAE6FD; font-weight:700;">
                    WELSPUN GROUP • LEADERSHIP COMMAND BRIEFING
                </div>
                <div style="font-size:1.45rem; font-weight:800; letter-spacing:0.02em; margin-top:2px;">
                    Executive Operations, Safety &amp; Production Intelligence
                </div>
                <div style="font-size:0.82rem; color:#E0F2FE; margin-top:2px;">
                    Consolidated 24/7 strategic overview across the 2,500-Acre Anjar Mega Manufacturing Hub.
                </div>
            </div>
            <div style="display:flex; gap:10px; align-items:center;">
                <div style="background:rgba(255,255,255,0.15); border:1px solid rgba(255,255,255,0.3); padding:8px 14px; border-radius:8px; text-align:center;">
                    <div style="font-size:0.68rem; color:#BAE6FD; text-transform:uppercase;">Overall Plant OEE</div>
                    <div style="font-size:1.25rem; font-weight:800; color:#34D399;">94.8%</div>
                </div>
                <div style="background:rgba(255,255,255,0.15); border:1px solid rgba(255,255,255,0.3); padding:8px 14px; border-radius:8px; text-align:center;">
                    <div style="font-size:0.68rem; color:#BAE6FD; text-transform:uppercase;">Workforce on Duty</div>
                    <div style="font-size:1.25rem; font-weight:800; color:#FFFFFF;">14,820</div>
                </div>
            </div>
        </div>
        """
    )

    # 2. Executive KPI Cards Row (6 Equal Responsive Cards)
    st.html(
        f"""
        <div class="kpi-grid" style="margin-bottom:1.2rem;">
            <div class="surv-kpi-card optimal" style="border-left-color: #005BAA;">
                <div class="surv-kpi-label">{kpis['complex_output']['title']}</div>
                <div class="surv-kpi-val" style="color:#005BAA;">{kpis['complex_output']['value']}</div>
                <div class="surv-kpi-sub"><b>{kpis['complex_output']['delta']}</b> • {kpis['complex_output']['target']}</div>
            </div>
            <div class="surv-kpi-card optimal" style="border-left-color: #10B981;">
                <div class="surv-kpi-label">{kpis['safe_man_hours']['title']}</div>
                <div class="surv-kpi-val" style="color:#059669;">{kpis['safe_man_hours']['value']}</div>
                <div class="surv-kpi-sub"><b>{kpis['safe_man_hours']['delta']}</b> ({kpis['safe_man_hours']['target']})</div>
            </div>
            <div class="surv-kpi-card optimal" style="border-left-color: #00A6E6;">
                <div class="surv-kpi-label">{kpis['logistics_automation']['title']}</div>
                <div class="surv-kpi-val" style="color:#0284C7;">{kpis['logistics_automation']['value']}</div>
                <div class="surv-kpi-sub"><b>{kpis['logistics_automation']['delta']}</b> • {kpis['logistics_automation']['target']}</div>
            </div>
            <div class="surv-kpi-card optimal" style="border-left-color: #005BAA;">
                <div class="surv-kpi-label">{kpis['sap_transacted_value']['title']}</div>
                <div class="surv-kpi-val" style="color:#005BAA;">{kpis['sap_transacted_value']['value']}</div>
                <div class="surv-kpi-sub"><b>{kpis['sap_transacted_value']['target']}</b> ({kpis['sap_transacted_value']['delta']})</div>
            </div>
            <div class="surv-kpi-card optimal" style="border-left-color: #10B981;">
                <div class="surv-kpi-label">{kpis['clean_energy_share']['title']}</div>
                <div class="surv-kpi-val" style="color:#059669;">{kpis['clean_energy_share']['value']}</div>
                <div class="surv-kpi-sub"><b>{kpis['clean_energy_share']['delta']}</b> • {kpis['clean_energy_share']['target']}</div>
            </div>
            <div class="surv-kpi-card optimal" style="border-left-color: #00A6E6;">
                <div class="surv-kpi-label">{kpis['ai_threat_prevention']['title']}</div>
                <div class="surv-kpi-val" style="color:#0284C7;">{kpis['ai_threat_prevention']['value']}</div>
                <div class="surv-kpi-sub"><b>{kpis['ai_threat_prevention']['delta']}</b> ({kpis['ai_threat_prevention']['target']})</div>
            </div>
        </div>
        """
    )

    # 3. Strategic Video Showcase Reel (2x2 Grid with Video & Telemetry Overlays)
    st.markdown("### 🎥 Strategic Video Intelligence Showcase")
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
    st.markdown("### 📈 Operational Velocity, Safety Intelligence & Energy Mix")
    st.caption("Real-time production tracking, autonomous safety interventions, and captive energy independence.")

    col_g1, col_g2 = st.columns([1.5, 1.1])

    with col_g1:
        st.markdown("##### 🏭 Hourly Production Velocity vs Plan (All Manufacturing Mills)")
        fig_prod = render_production_velocity_chart(prod_data)
        st.plotly_chart(fig_prod, use_container_width=True)

    with col_g2:
        st.markdown("##### 🛡️ Autonomous AI Safety & Anomaly Prevention Breakdown")
        fig_ai = render_ai_prevention_donut(ai_data)
        st.plotly_chart(fig_ai, use_container_width=True)

    # Clean Energy Balance Chart
    st.markdown("##### ⚡ 24-Hour Captive Clean Energy Generation vs Complex Demand")
    fig_energy = render_energy_mix_chart(energy_data)
    st.plotly_chart(fig_energy, use_container_width=True)

    st.markdown("---")

    # 5. Strategic Milestones & Leadership Directives
    st.markdown("### 🧭 Strategic Milestones & Boardroom Directives")
    st.caption("High-impact capacity expansions, ESG sustainability initiatives, and plant modernization deliverables.")

    milestone_cols = st.columns(2)
    for idx, item in enumerate(milestones):
        col = milestone_cols[idx % 2]
        with col:
            prio_color = "#005BAA" if item["priority"] == "HIGH" else ("#F59E0B" if item["priority"] == "ACTION REQUIRED" else "#10B981")
            st.html(
                f"""
                <div style="background:#FFFFFF; border:1px solid #CBD5E1; border-left:4px solid {prio_color}; border-radius:8px; padding:12px 14px; margin-bottom:10px; box-shadow:0 1px 4px rgba(0,0,0,0.04);">
                    <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:4px;">
                        <span style="font-size:0.72rem; color:#64748B; text-transform:uppercase; font-weight:700;">{item['domain']}</span>
                        <span style="background:rgba(0, 91, 170, 0.1); color:{prio_color}; font-size:0.70rem; font-weight:800; padding:2px 7px; border-radius:4px;">
                            {item['status']}
                        </span>
                    </div>
                    <div style="font-size:0.95rem; font-weight:700; color:#0F172A; margin-bottom:4px;">
                        {item['title']}
                    </div>
                    <div style="font-size:0.78rem; color:#475569; margin-bottom:6px; line-height:1.35;">
                        {item['impact']}
                    </div>
                    <div style="display:flex; justify-content:space-between; font-size:0.72rem; color:#64748B; border-top:1px solid #F1F5F9; padding-top:6px;">
                        <span>Lead: <b>{item['lead']}</b></span>
                        <span>Target: <b style="color:#0F172A;">{item['deadline']}</b></span>
                    </div>
                </div>
                """
            )
