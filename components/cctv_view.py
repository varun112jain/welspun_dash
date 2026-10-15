"""
CCTV Surveillance Video Wall & Multi-Screen Camera Components
Renders continuous synthetic live video streams with HUD and AI overlays.
"""
import os
import streamlit as st

def render_cctv_video_card(feed: dict, stream_format: str = "Live Stream"):
    """Renders a single CCTV feed card with continuous animated streaming, HUD, and AI overlays."""
    badge_color = "#EF4444" if "CRITICAL" in feed["status"] else ("#005BAA" if "READY" in feed["status"] else "#10B981")
    pulse_dot = '<span class="pulse-dot-red"></span>' if "CRITICAL" in feed["status"] else '<span class="pulse-dot-green"></span>'
    
    with st.container(border=True):
        # 1. Camera Header HUD
        st.markdown(
            f"""
            <div style="background:#020617; color:#E2E8F0; padding:6px 10px; border-radius:6px; margin-bottom:8px; display:flex; justify-content:space-between; align-items:center; font-family:monospace; font-size:0.85rem; border:1px solid #1E293B;">
                <div>
                    <span style="color:#00A6E6; font-weight:bold;">{feed["id"]}</span> | 
                    <span>{feed["name"]}</span>
                </div>
                <div style="display:flex; align-items:center; gap:8px;">
                    <span class="cctv-live-tag">{pulse_dot} LIVE STREAM</span>
                    <span style="color:#94A3B8; font-size:0.75rem;">{feed["fps"]} FPS</span>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )
        
        # 2. Continuous Video Feed Display
        gif_path = feed.get("gif", "")
        vid_path = feed.get("video", "")
        img_path = feed.get("image", "")
        
        rendered = False
        
        # If user explicitly selected MP4 player
        if stream_format == "MP4" and vid_path and os.path.exists(vid_path):
            try:
                st.video(vid_path, loop=True, autoplay=True, muted=True)
                rendered = True
            except Exception:
                rendered = False
                
        # Primary live stream: Animated loop (guaranteed 100% visible, zero black screens)
        if not rendered and gif_path and os.path.exists(gif_path):
            st.image(gif_path, use_container_width=True)
            rendered = True
            
        # Fallback to static snapshot if needed
        if not rendered and img_path and os.path.exists(img_path):
            st.image(img_path, use_container_width=True)
            rendered = True
            
        if not rendered:
            st.error(f"Feed stream offline for {feed['id']}")
            
        # 3. Camera Metadata & AI Detections Footer
        ai_tags_html = " ".join([f"<span style='background:#1E293B; color:#38BDF8; padding:2px 7px; border-radius:4px; font-size:0.72rem; border:1px solid #334155;'>{feat}</span>" for feat in feed.get("ai_features", [])])
        
        st.markdown(
            f"""
            <div style="background:#0F172A; border-radius:6px; padding:8px 10px; margin-top:8px; border:1px solid #1E293B;">
                <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:5px;">
                    <span style="color:#E2E8F0; font-weight:600; font-size:0.78rem;">📍 <span style="color:#93C5FD;">{feed['sector']}</span></span>
                    <span style="background:{badge_color}; color:#fff; font-size:0.72rem; font-weight:bold; padding:2px 8px; border-radius:4px;">{feed['alert_badge']}</span>
                </div>
                <div style="margin-bottom:6px;">{ai_tags_html}</div>
                <div style="font-size:0.76rem; color:#CBD5E1; background:rgba(0,0,0,0.4); padding:5px 8px; border-radius:4px; border-left:3px solid {badge_color};">
                    <b>AI Intel:</b> {feed['ai_summary']}
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

# Backward-compatibility alias
render_cctv_card = render_cctv_video_card

__all__ = ["render_cctv_video_card", "render_cctv_card"]
