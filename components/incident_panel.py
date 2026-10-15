"""
Safety & Fire Alarm Incident Log Component with Perimeter Crossing Support
"""
import streamlit as st

def render_incident_panel(alarms: list):
    """Renders the interactive fire, safety, and perimeter alert stream."""
    st.markdown("### ⚠️ Live Alarms & Security Breaches")
    
    for alarm in alarms:
        sev = alarm["severity"].lower()
        badge_color = "#EF4444" if sev == "critical" else ("#F59E0B" if sev == "warning" else "#3B82F6")
        status_color = "#10B981" if alarm["status"] == "Resolved" else ("#EF4444" if alarm["status"] == "In Progress" else "#64748B")
        
        is_perimeter = "Perimeter" in alarm["type"] or "Intrusion" in alarm["type"]
        border_style = "border-left: 6px solid #EF4444;" if is_perimeter else f"border-left: 5px solid {badge_color};"
        bg_style = "background: #FFF5F5;" if is_perimeter else "background: #FFFFFF;"
        
        st.markdown(
            f"""
            <div class="alarm-item {sev}" style="{border_style} {bg_style}">
                <div class="alarm-header">
                    <div>
                        <span style="background:{badge_color}; color:#fff; padding:2px 8px; border-radius:4px; font-size:0.75rem; font-weight:bold;">{alarm['severity']}</span>
                        <span style="margin-left:8px; font-size:0.95rem; font-weight:700;">{alarm['type']}</span>
                    </div>
                    <div class="alarm-meta">
                        🕒 {alarm['time']} | 📍 {alarm['zone']}
                    </div>
                </div>
                <div class="alarm-desc">
                    <b>Location:</b> {alarm['location']}<br>
                    {alarm['details']}
                </div>
                <div style="font-size:0.8rem; background:rgba(0,0,0,0.03); padding:6px 10px; border-radius:4px; border:1px solid #E2E8F0; display:flex; justify-content:space-between; align-items:center;">
                    <span><b>Protocol Action:</b> {alarm['action_taken']}</span>
                    <span style="color:{status_color}; font-weight:700;">● {alarm['status']}</span>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )
