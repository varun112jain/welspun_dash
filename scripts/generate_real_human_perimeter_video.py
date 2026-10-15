"""
Generates high-realism CCTV video of a real human crossing the virtual perimeter tripwire.
Composites photographic human cutout with realistic walking gait, scaling perspective,
ground shadow, floodlight tinting, dynamic AI bounding boxes, and breach alarms.
"""
import os
import cv2
import numpy as np
import subprocess

ASSETS_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "assets"))
BRAIN_DIR = r"C:\Users\0231304\.gemini\antigravity-ide\brain\eecaddaa-0620-4207-bd68-b2628b06b6ae"

bg_path = os.path.join(ASSETS_DIR, "cctv_perimeter_fence.jpg")
person_path = os.path.join(ASSETS_DIR, "human_intruder_transparent.png")

bg_img = cv2.imread(bg_path)
bg_img = cv2.resize(bg_img, (960, 540))
h_bg, w_bg, _ = bg_img.shape

person_rgba = cv2.imread(person_path, cv2.IMREAD_UNCHANGED)
h_p, w_p, _ = person_rgba.shape

num_frames = 90
fps = 15
temp_raw_mp4 = os.path.join(ASSETS_DIR, "temp_perimeter_raw.mp4")
final_h264_mp4 = os.path.join(ASSETS_DIR, "video_perimeter_breach.mp4")
final_gif = os.path.join(ASSETS_DIR, "video_perimeter_breach.gif")

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(temp_raw_mp4, fourcc, fps, (w_bg, h_bg))

# Tripwire line from mid-fence through gravel road
tripwire_pt1 = (170, 240)
tripwire_pt2 = (390, 480)

# Movement trajectory of the person along the road (start in distance, walk towards camera)
start_x, start_y = 190, 250
end_x, end_y = 310, 340

start_scale = 0.16
end_scale = 0.27

for i in range(num_frames):
    frame = bg_img.copy()
    t = i / float(num_frames)
    
    # Position and scale with perspective
    cur_x = int(start_x + t * (end_x - start_x))
    cur_y = int(start_y + t * (end_y - start_y))
    cur_scale = start_scale + t * (end_scale - start_scale)
    
    # Walking gait vertical bobbing (approx 2 steps per second)
    bob = int(np.abs(np.sin(i * 0.45)) * 4)
    cur_y -= bob
    
    # Scaled person dimensions
    p_w = int(w_p * cur_scale)
    p_h = int(h_p * cur_scale)
    resized_person = cv2.resize(person_rgba, (p_w, p_h), interpolation=cv2.INTER_AREA)
    
    # Check if crossed the virtual tripwire (around frame 32)
    feet_x = cur_x + p_w // 2
    feet_y = cur_y + p_h
    is_breached = (i >= 30)
    
    # 1. Draw Virtual Laser Tripwire on the ground
    line_color = (0, 0, 255) if is_breached and (i % 6 < 3) else (255, 200, 0)
    cv2.line(frame, tripwire_pt1, tripwire_pt2, line_color, 2, cv2.LINE_AA)
    
    # Tripwire sensor nodes
    cv2.circle(frame, tripwire_pt1, 4, line_color, -1)
    cv2.circle(frame, tripwire_pt2, 4, line_color, -1)
    cv2.putText(frame, "[VIRTUAL LASER TRIPWIRE - SECTOR 4]", (tripwire_pt1[0] - 20, tripwire_pt1[1] - 8),
                cv2.FONT_HERSHEY_SIMPLEX, 0.4, line_color, 1, cv2.LINE_AA)
    
    # 2. Draw ground contact drop shadow
    shadow_overlay = frame.copy()
    shadow_center = (cur_x + p_w // 2, cur_y + p_h - 4)
    shadow_axes = (int(p_w * 0.65), int(p_w * 0.25))
    cv2.ellipse(shadow_overlay, shadow_center, shadow_axes, 15, 0, 360, (10, 10, 15), -1)
    cv2.addWeighted(shadow_overlay, 0.55, frame, 0.45, 0, frame)
    
    # 3. Alpha blend real human onto frame
    p_bgr = resized_person[:, :, :3]
    p_alpha = resized_person[:, :, 3] / 255.0
    
    # Subtly match CCTV ambient night light tone (cool blue night tint)
    p_bgr_tinted = p_bgr.astype(np.float32)
    p_bgr_tinted[:, :, 0] = np.clip(p_bgr_tinted[:, :, 0] * 1.05 + 10, 0, 255) # Blue
    p_bgr_tinted[:, :, 1] = np.clip(p_bgr_tinted[:, :, 1] * 0.95, 0, 255)       # Green
    p_bgr_tinted[:, :, 2] = np.clip(p_bgr_tinted[:, :, 2] * 0.90, 0, 255)       # Red
    p_bgr_tinted = p_bgr_tinted.astype(np.uint8)
    
    y1, y2 = max(0, cur_y), min(h_bg, cur_y + p_h)
    x1, x2 = max(0, cur_x), min(w_bg, cur_x + p_w)
    
    crop_py1 = y1 - cur_y
    crop_py2 = crop_py1 + (y2 - y1)
    crop_px1 = x1 - cur_x
    crop_px2 = crop_px1 + (x2 - x1)
    
    for c in range(3):
        frame[y1:y2, x1:x2, c] = (
            p_alpha[crop_py1:crop_py2, crop_px1:crop_px2] * p_bgr_tinted[crop_py1:crop_py2, crop_px1:crop_px2, c] +
            (1.0 - p_alpha[crop_py1:crop_py2, crop_px1:crop_px2]) * frame[y1:y2, x1:x2, c]
        )
        
    # 4. AI Computer-Vision Bounding Box around Real Human
    box_color = (0, 0, 255) if is_breached else (0, 230, 255)
    pad = 4
    bx1, by1 = cur_x - pad, cur_y - pad
    bx2, by2 = cur_x + p_w + pad, cur_y + p_h + pad
    
    cv2.rectangle(frame, (bx1, by1), (bx2, by2), box_color, 2)
    
    # Corner brackets (HUD Style)
    b_len = 12
    cv2.line(frame, (bx1, by1), (bx1 + b_len, by1), box_color, 3)
    cv2.line(frame, (bx1, by1), (bx1, by1 + b_len), box_color, 3)
    cv2.line(frame, (bx2, by1), (bx2 - b_len, by1), box_color, 3)
    cv2.line(frame, (bx2, by1), (bx2, by1 + b_len), box_color, 3)
    cv2.line(frame, (bx1, by2), (bx1 + b_len, by2), box_color, 3)
    cv2.line(frame, (bx1, by2), (bx1, by2 - b_len), box_color, 3)
    cv2.line(frame, (bx2, by2), (bx2 - b_len, by2), box_color, 3)
    cv2.line(frame, (bx2, by2), (bx2, by2 - b_len), box_color, 3)
    
    # Target centroid reticle
    cen_x, cen_y = (bx1 + bx2) // 2, (by1 + by2) // 2
    cv2.drawMarker(frame, (cen_x, cen_y), box_color, cv2.MARKER_CROSS, 10, 1)
    
    # AI Metadata Badge above person
    if is_breached:
        badge_title = "ALERT: UNAUTHORIZED INTRUDER"
        badge_sub = "BREACH: PERIMETER TRIPWIRE CROSSED"
        conf = "CONF: 99.4% [HUMAN MALE]"
        # Top flashing alert banner
        if i % 8 < 5:
            cv2.rectangle(frame, (230, 35), (730, 80), (0, 0, 200), -1)
            cv2.rectangle(frame, (230, 35), (730, 80), (255, 255, 255), 1)
            cv2.putText(frame, "CRITICAL: UNAUTHORIZED AREA BREACH", (250, 65),
                        cv2.FONT_HERSHEY_DUPLEX, 0.65, (255, 255, 255), 2, cv2.LINE_AA)
    else:
        badge_title = "TRACKING TARGET: HUMAN"
        badge_sub = "APPROACHING RESTRICTED ZONE"
        conf = "CONF: 98.8% [MONITORING]"
        
    tag_w = 210
    tag_h = 38
    tag_x = bx1 - 10
    tag_y = max(10, by1 - tag_h - 4)
    cv2.rectangle(frame, (tag_x, tag_y), (tag_x + tag_w, tag_y + tag_h), (10, 15, 25), -1)
    cv2.rectangle(frame, (tag_x, tag_y), (tag_x + tag_w, tag_y + tag_h), box_color, 1)
    cv2.putText(frame, badge_title, (tag_x + 6, tag_y + 14), cv2.FONT_HERSHEY_SIMPLEX, 0.36, box_color, 1, cv2.LINE_AA)
    cv2.putText(frame, badge_sub, (tag_x + 6, tag_y + 25), cv2.FONT_HERSHEY_SIMPLEX, 0.30, (220, 220, 220), 1, cv2.LINE_AA)
    cv2.putText(frame, conf, (tag_x + 6, tag_y + 34), cv2.FONT_HERSHEY_SIMPLEX, 0.28, (0, 255, 120), 1, cv2.LINE_AA)
    
    # Top & Bottom HUD Overlays
    cv2.putText(frame, "CAM-04 PERIMETER WEST FENCE | 1080p | AI: MOTION+AI-HUMAN", (20, 25),
                cv2.FONT_HERSHEY_SIMPLEX, 0.45, (0, 255, 255), 1, cv2.LINE_AA)
                
    sec_str = f"23:48:{20 + (i // 15):02d}.{int((i % 15) * 6.6):02d} UTC"
    cv2.putText(frame, sec_str, (w_bg - 190, 25), cv2.FONT_HERSHEY_SIMPLEX, 0.45, (255, 255, 255), 1, cv2.LINE_AA)
    
    # Blinking REC dot
    if i % 12 < 8:
        cv2.circle(frame, (35, h_bg - 20), 6, (0, 0, 255), -1)
        cv2.putText(frame, "REC [OPTICAL + IR DUAL]", (48, h_bg - 16), cv2.FONT_HERSHEY_SIMPLEX, 0.40, (255, 255, 255), 1)

    out.write(frame)

out.release()
print("Raw video written to:", temp_raw_mp4)

# Transcode to standard web H.264
cmd_mp4 = [
    "ffmpeg", "-y",
    "-i", temp_raw_mp4,
    "-c:v", "libx264",
    "-pix_fmt", "yuv420p",
    "-profile:v", "baseline",
    "-level", "3.0",
    "-movflags", "+faststart",
    final_h264_mp4
]
subprocess.run(cmd_mp4, check=True)
print("Web H.264 video saved to:", final_h264_mp4)

# Generate high-quality looping animated GIF
cmd_gif = [
    "ffmpeg", "-y",
    "-i", final_h264_mp4,
    "-vf", "fps=12,scale=720:-1:flags=lanczos,split[s0][s1];[s0]palettegen[p];[s1][p]paletteuse",
    final_gif
]
subprocess.run(cmd_gif, check=True)
print("Animated GIF saved to:", final_gif)

# Clean up raw temp video
if os.path.exists(temp_raw_mp4):
    os.remove(temp_raw_mp4)

# Copy to brain artifact directory for direct chat preview
brain_gif = os.path.join(BRAIN_DIR, "perimeter_breach_clip.gif")
brain_mp4 = os.path.join(BRAIN_DIR, "perimeter_breach_clip.mp4")

import shutil
shutil.copy2(final_gif, brain_gif)
shutil.copy2(final_h264_mp4, brain_mp4)
print(f"Copied updated clips with real human to {BRAIN_DIR}")
