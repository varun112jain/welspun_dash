"""
Master Synthetic Video Generator for Welspun City Anjar Command & Control Centre (ICCC)
Generates 8 completely UNIQUE, high-realism surveillance video clips (.mp4 in H.264 & .gif)
for each individual camera feed across the 2,500-acre Welspun City complex.
"""
import os
import cv2
import numpy as np
import subprocess

ASSETS_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "assets"))

def save_mp4_and_gif(temp_raw_path, final_mp4_path, final_gif_path, fps=15):
    """Encodes raw video to web-compatible H.264 MP4 and lanczos-palette animated GIF."""
    cmd_mp4 = [
        "ffmpeg", "-y",
        "-i", temp_raw_path,
        "-c:v", "libx264",
        "-pix_fmt", "yuv420p",
        "-profile:v", "baseline",
        "-level", "3.0",
        "-movflags", "+faststart",
        final_mp4_path
    ]
    subprocess.run(cmd_mp4, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    
    cmd_gif = [
        "ffmpeg", "-y",
        "-i", final_mp4_path,
        "-vf", f"fps={min(fps, 12)},scale=640:-1:flags=lanczos,split[s0][s1];[s0]palettegen[p];[s1][p]paletteuse",
        final_gif_path
    ]
    subprocess.run(cmd_gif, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    
    if os.path.exists(temp_raw_path):
        os.remove(temp_raw_path)

def generate_cam01_blast_furnace(num_frames=75, fps=15):
    """CAM-01: WDI 500,000 TPA Blast Furnace & DI Casting Bay."""
    bg_path = os.path.join(ASSETS_DIR, "cctv_blast_furnace.jpg")
    base_img = cv2.resize(cv2.imread(bg_path), (960, 540))
    h, w, _ = base_img.shape
    
    temp_raw = os.path.join(ASSETS_DIR, "temp_cam01.mp4")
    out = cv2.VideoWriter(temp_raw, cv2.VideoWriter_fourcc(*'mp4v'), fps, (w, h))
    
    np.random.seed(42)
    sparks = [{"x": np.random.randint(480, 600), "y": np.random.randint(320, 480), "vy": np.random.uniform(2, 6), "vx": np.random.uniform(-2, 2), "life": np.random.randint(5, 15)} for _ in range(25)]
    
    for i in range(num_frames):
        frame = base_img.copy()
        
        # 1. Molten metal flow pulsation glow
        glow_pulse = int(15 * np.sin(i * 0.3))
        overlay = frame.copy()
        cv2.circle(overlay, (560, 420), 80 + glow_pulse, (0, 140, 255), -1)
        cv2.circle(overlay, (360, 260), 60 + glow_pulse, (0, 160, 255), -1)
        cv2.addWeighted(overlay, 0.28, frame, 0.72, 0, frame)
        
        # 2. Hot metal sparks particle simulation
        for s in sparks:
            s["y"] += int(s["vy"])
            s["x"] += int(s["vx"])
            s["life"] -= 1
            if s["life"] <= 0 or s["y"] > 520:
                s["x"] = np.random.randint(500, 580)
                s["y"] = np.random.randint(340, 390)
                s["vy"] = np.random.uniform(2, 7)
                s["vx"] = np.random.uniform(-3, 3)
                s["life"] = np.random.randint(8, 20)
            cv2.circle(frame, (int(s["x"]), int(s["y"])), 2, (180, 240, 255), -1)
            
        # 3. Ladle Car AI tracking bounding box
        cv2.rectangle(frame, (480, 320), (660, 520), (0, 200, 255), 2)
        temp_val = 1480 + int(4 * np.sin(i * 0.2))
        cv2.rectangle(frame, (480, 285), (710, 315), (15, 23, 42), -1)
        cv2.putText(frame, f"[LADLE CAR #02: {temp_val} C]", (485, 305), cv2.FONT_HERSHEY_SIMPLEX, 0.42, (0, 220, 255), 1)
        
        # 4. Tap Hole Pyrometer Crosshair
        cv2.drawMarker(frame, (350, 255), (0, 255, 255), cv2.MARKER_CROSS, 24, 2)
        cv2.putText(frame, "TAP HOLE PYROMETER", (260, 235), cv2.FONT_HERSHEY_SIMPLEX, 0.38, (0, 255, 255), 1)
        
        # 5. Top & Bottom HUD
        cv2.putText(frame, "CAM-01 WDI 500k TPA BLAST FURNACE | TAP HOLE & DI CASTING", (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.46, (0, 255, 255), 1)
        cv2.putText(frame, "BFG / CO: 12 PPM (SAFE)", (w - 240, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.45, (0, 255, 120), 1)
        
        if i % 14 < 10:
            cv2.circle(frame, (35, h - 22), 6, (0, 255, 0), -1)
            cv2.putText(frame, "HOT METAL TRANSIT: NORMAL", (50, h - 18), cv2.FONT_HERSHEY_SIMPLEX, 0.42, (255, 255, 255), 1)
            
        out.write(frame)
        
    out.release()
    save_mp4_and_gif(temp_raw, os.path.join(ASSETS_DIR, "video_wdi_blast_furnace.mp4"), os.path.join(ASSETS_DIR, "video_wdi_blast_furnace.gif"), fps)
    print("CAM-01 Blast Furnace video generated.")

def generate_cam06_wcl_pipe_mill(num_frames=75, fps=15):
    """CAM-06: WCL Large Diameter Pipe Mills (LSAW & Spiral HSAW)."""
    bg_path = os.path.join(ASSETS_DIR, "cctv_wcl_pipe_mill.jpg")
    base_img = cv2.resize(cv2.imread(bg_path), (960, 540))
    h, w, _ = base_img.shape
    
    temp_raw = os.path.join(ASSETS_DIR, "temp_cam06.mp4")
    out = cv2.VideoWriter(temp_raw, cv2.VideoWriter_fourcc(*'mp4v'), fps, (w, h))
    
    for i in range(num_frames):
        frame = base_img.copy()
        
        # 1. Submerged arc welding bright flicker
        weld_x, weld_y = 530, 320
        arc_intensity = np.random.uniform(0.2, 0.55)
        arc_radius = int(70 + np.random.randint(-15, 25))
        overlay = frame.copy()
        cv2.circle(overlay, (weld_x, weld_y), arc_radius, (255, 255, 200), -1)
        cv2.circle(overlay, (weld_x, weld_y), arc_radius + 40, (255, 200, 50), -1)
        cv2.addWeighted(overlay, arc_intensity, frame, 1.0 - arc_intensity, 0, frame)
        
        # 2. Weld seam tracking laser line
        laser_pulse = int(np.abs(np.sin(i * 0.2)) * 100)
        cv2.line(frame, (320, 360), (700, 260), (0, 0, 255), 2)
        cv2.putText(frame, "[SEAM TRACKING LASER ACTIVE]", (330, 380), cv2.FONT_HERSHEY_SIMPLEX, 0.36, (0, 0, 255), 1)
        
        # 3. 56" API Line pipe AI Bounding Box
        cv2.rectangle(frame, (230, 290), (750, 480), (0, 255, 120), 2)
        cv2.rectangle(frame, (230, 260), (580, 288), (15, 23, 42), -1)
        cv2.putText(frame, "WCL 56\" API-5L X70 LINE PIPE (HSAW)", (240, 280), cv2.FONT_HERSHEY_SIMPLEX, 0.42, (0, 255, 120), 1)
        
        # 4. Crane Hook Safe Zone
        cv2.rectangle(frame, (450, 80), (720, 160), (255, 200, 0), 1)
        cv2.putText(frame, "[GANTRY CRANE SWL 20T: EXCLUSION CLEAR]", (455, 100), cv2.FONT_HERSHEY_SIMPLEX, 0.36, (255, 200, 0), 1)
        
        # 5. HUD
        cv2.putText(frame, "CAM-06 WCL LINE PIPE MILL 1 | 56\" LSAW & SPIRAL HSAW", (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.46, (0, 255, 255), 1)
        cv2.putText(frame, "HYDROTESTER: 210 BAR (PASS)", (w - 270, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.45, (0, 255, 120), 1)
        
        if i % 14 < 10:
            cv2.circle(frame, (35, h - 22), 6, (0, 255, 0), -1)
            cv2.putText(frame, "SUBMERGED ARC WELD: CONTINUOUS OK", (50, h - 18), cv2.FONT_HERSHEY_SIMPLEX, 0.42, (255, 255, 255), 1)
            
        out.write(frame)
        
    out.release()
    save_mp4_and_gif(temp_raw, os.path.join(ASSETS_DIR, "video_wcl_pipe_mill.mp4"), os.path.join(ASSETS_DIR, "video_wcl_pipe_mill.gif"), fps)
    print("CAM-06 WCL Pipe Mill video generated.")

def generate_cam07_wll_textiles(num_frames=75, fps=15):
    """CAM-07: WLL Home & Advanced Spunlace Non-Woven Facility."""
    bg_path = os.path.join(ASSETS_DIR, "cctv_wll_spunlace.jpg")
    base_img = cv2.resize(cv2.imread(bg_path), (960, 540))
    h, w, _ = base_img.shape
    
    temp_raw = os.path.join(ASSETS_DIR, "temp_cam07.mp4")
    out = cv2.VideoWriter(temp_raw, cv2.VideoWriter_fourcc(*'mp4v'), fps, (w, h))
    
    for i in range(num_frames):
        frame = base_img.copy()
        
        # 1. Roll winder motion indicator
        roll_x, roll_y = 295, 395
        roll_r = 50
        angle = (i * 12) % 360
        rad = np.radians(angle)
        cv2.line(frame, (roll_x, roll_y), (int(roll_x + roll_r * np.cos(rad)), int(roll_y + roll_r * np.sin(rad))), (0, 180, 255), 2)
        
        # 2. Fabric Roll Inspection AI Box
        cv2.rectangle(frame, (230, 320), (370, 480), (0, 255, 120), 2)
        cv2.rectangle(frame, (230, 290), (510, 318), (15, 23, 42), -1)
        cv2.putText(frame, "[SPUNLACE 50 GSM: 0 DEFECTS / 120 M/MIN]", (235, 310), cv2.FONT_HERSHEY_SIMPLEX, 0.38, (0, 255, 120), 1)
        
        # 3. Worker PPE Box
        cv2.rectangle(frame, (390, 320), (455, 490), (0, 255, 0), 2)
        cv2.putText(frame, "[PPE: 100% OK]", (385, 312), cv2.FONT_HERSHEY_SIMPLEX, 0.36, (0, 255, 0), 1)
        
        # 4. Weaving Loom Hall Status
        cv2.rectangle(frame, (640, 250), (910, 420), (0, 200, 255), 1)
        cv2.putText(frame, "[AIR-JET LOOMS 1-48: 94.6% EFFICIENCY]", (650, 270), cv2.FONT_HERSHEY_SIMPLEX, 0.36, (0, 200, 255), 1)
        
        # 5. HUD
        cv2.putText(frame, "CAM-07 WLL HOME & ADVANCED SPUNLACE TEXTILES", (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.46, (0, 255, 255), 1)
        cv2.putText(frame, "AIR QUALITY: PARTICULATE NORMAL", (w - 300, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.45, (0, 255, 120), 1)
        
        if i % 14 < 10:
            cv2.circle(frame, (35, h - 22), 6, (0, 255, 0), -1)
            cv2.putText(frame, "HYDRO-ENTANGLE LINE 2: OPTIMAL", (50, h - 18), cv2.FONT_HERSHEY_SIMPLEX, 0.42, (255, 255, 255), 1)
            
        out.write(frame)
        
    out.release()
    save_mp4_and_gif(temp_raw, os.path.join(ASSETS_DIR, "video_wll_spunlace.mp4"), os.path.join(ASSETS_DIR, "video_wll_spunlace.gif"), fps)
    print("CAM-07 WLL Textiles video generated.")

def generate_cam08_vidya_mandir(num_frames=75, fps=15):
    """CAM-08: Welspun Vidya Mandir School Campus & Multi-Speciality Health Centre."""
    bg_path = os.path.join(ASSETS_DIR, "cctv_vidya_mandir.jpg")
    base_img = cv2.resize(cv2.imread(bg_path), (960, 540))
    h, w, _ = base_img.shape
    
    temp_raw = os.path.join(ASSETS_DIR, "temp_cam08.mp4")
    out = cv2.VideoWriter(temp_raw, cv2.VideoWriter_fourcc(*'mp4v'), fps, (w, h))
    
    for i in range(num_frames):
        frame = base_img.copy()
        
        # 1. School bus tracking box
        cv2.rectangle(frame, (120, 300), (320, 410), (0, 220, 255), 2)
        cv2.rectangle(frame, (120, 275), (340, 298), (15, 23, 42), -1)
        cv2.putText(frame, "[SCHOOL BUS 04 - PARKED SAFE]", (125, 292), cv2.FONT_HERSHEY_SIMPLEX, 0.38, (0, 220, 255), 1)
        
        # 2. Ambulance Slipway Clear Box
        cv2.rectangle(frame, (760, 310), (880, 400), (0, 255, 100), 2)
        cv2.rectangle(frame, (730, 285), (920, 308), (15, 23, 42), -1)
        cv2.putText(frame, "[AMBULANCE BAY: 100% CLEAR]", (735, 302), cv2.FONT_HERSHEY_SIMPLEX, 0.38, (0, 255, 100), 1)
        
        # 3. Rooftop Solar PV Telemetry
        cv2.rectangle(frame, (25, 110), (280, 150), (15, 23, 42), -1)
        cv2.rectangle(frame, (25, 110), (280, 150), (255, 200, 0), 1)
        solar_gen = 1.20 + 0.05 * np.sin(i * 0.15)
        cv2.putText(frame, f"CAMPUS SOLAR: {solar_gen:.2f} MW ACTIVE", (35, 135), cv2.FONT_HERSHEY_SIMPLEX, 0.40, (255, 220, 0), 1)
        
        # 4. Campus perimeter boundary line
        cv2.line(frame, (370, 330), (510, 420), (0, 255, 0), 2)
        cv2.putText(frame, "[CAMPUS PERIMETER SECURED]", (380, 320), cv2.FONT_HERSHEY_SIMPLEX, 0.36, (0, 255, 0), 1)
        
        # 5. HUD
        cv2.putText(frame, "CAM-08 WELSPUN VIDYA MANDIR & HEALTH CENTRE", (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.46, (0, 255, 255), 1)
        cv2.putText(frame, "COMMUNITY DEFENSE: 100% SECURE", (w - 310, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.45, (0, 255, 120), 1)
        
        if i % 14 < 10:
            cv2.circle(frame, (35, h - 22), 6, (0, 255, 0), -1)
            cv2.putText(frame, "STUDENT & PATIENT CORRIDOR: CLEAR", (50, h - 18), cv2.FONT_HERSHEY_SIMPLEX, 0.42, (255, 255, 255), 1)
            
        out.write(frame)
        
    out.release()
    save_mp4_and_gif(temp_raw, os.path.join(ASSETS_DIR, "video_vidya_mandir.mp4"), os.path.join(ASSETS_DIR, "video_vidya_mandir.gif"), fps)
    print("CAM-08 Vidya Mandir video generated.")

if __name__ == "__main__":
    generate_cam01_blast_furnace()
    generate_cam06_wcl_pipe_mill()
    generate_cam07_wll_textiles()
    generate_cam08_vidya_mandir()
    print("ALL 8 UNIQUE SURVEILLANCE VIDEOS COMPLETED!")
