"""
Video Generator for Welspun Logistics, Unmanned Weighbridge, and Employee Transit Bus Fleet
Generates H.264 MP4 and animated GIF streams with AI HUD overlays for the new surveillance screens.
"""
import os
import cv2
import numpy as np
import subprocess

ASSETS_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "assets"))

def save_mp4_and_gif(temp_raw_path, final_mp4_path, final_gif_path, fps=12):
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
        "-vf", f"fps={fps},scale=720:-1:flags=lanczos,split[s0][s1];[s0]palettegen[p];[s1][p]paletteuse",
        final_gif_path
    ]
    subprocess.run(cmd_gif, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    
    if os.path.exists(temp_raw_path):
        os.remove(temp_raw_path)

def generate_unmanned_weighbridge_video(num_frames=60, fps=12):
    """CAM-WB01: Unmanned Automated Weighbridge with Load Cell & SAP S/4HANA Sync."""
    bg_path = os.path.join(ASSETS_DIR, "cctv_unmanned_weighbridge.jpg")
    base_img = cv2.resize(cv2.imread(bg_path), (960, 540))
    h, w, _ = base_img.shape
    
    temp_raw = os.path.join(ASSETS_DIR, "temp_wb.mp4")
    out = cv2.VideoWriter(temp_raw, cv2.VideoWriter_fourcc(*'mp4v'), fps, (w, h))
    
    for i in range(num_frames):
        frame = base_img.copy()
        
        # 1. Pulsing LED on Weighbridge Display
        pulse = int(np.abs(np.sin(i * 0.25)) * 30)
        overlay = frame.copy()
        cv2.rectangle(overlay, (530, 70), (670, 150), (0, 200 + pulse, 100), -1)
        cv2.addWeighted(overlay, 0.22, frame, 0.78, 0, frame)
        
        # 2. ANPR Target Lock Box on Truck Number Plate
        cv2.rectangle(frame, (250, 470), (320, 500), (0, 255, 255), 2)
        cv2.rectangle(frame, (250, 445), (420, 468), (15, 23, 42), -1)
        cv2.putText(frame, "ANPR: GJ-12-BW-9842 [MATCH]", (255, 462), cv2.FONT_HERSHEY_SIMPLEX, 0.38, (0, 255, 255), 1)
        
        # 3. IR Laser Alignment Sensors (Positioning check)
        sensor_color = (0, 255, 0)
        cv2.line(frame, (170, 480), (740, 520), (0, 255, 0), 1, cv2.LINE_AA)
        cv2.putText(frame, "[IR POSITION SENSOR: 100% ALIGNED - NO OVERHANG]", (180, 532), cv2.FONT_HERSHEY_SIMPLEX, 0.36, sensor_color, 1)
        
        # 4. Digital Load Cell & SAP Sync HUD
        weight_fluct = 42850 + int(2 * np.sin(i * 0.4))
        cv2.rectangle(frame, (20, 20), (460, 75), (15, 23, 42), -1)
        cv2.rectangle(frame, (20, 20), (460, 75), (0, 166, 230), 1)
        cv2.putText(frame, f"DIGITAL LOAD CELL: {weight_fluct:,} KG (GROSS WT)", (30, 42), cv2.FONT_HERSHEY_SIMPLEX, 0.44, (0, 255, 120), 1)
        cv2.putText(frame, "SAP S/4HANA PO #450098231 • MIGO AUTO-POST OK", (30, 64), cv2.FONT_HERSHEY_SIMPLEX, 0.38, (220, 220, 220), 1)
        
        # 5. Boom Barrier Status
        if i % 16 < 12:
            cv2.circle(frame, (w - 180, 40), 7, (0, 255, 0), -1)
            cv2.putText(frame, "BOOM: AUTO-AUTHORIZED", (w - 165, 44), cv2.FONT_HERSHEY_SIMPLEX, 0.38, (0, 255, 0), 1)
        else:
            cv2.circle(frame, (w - 180, 40), 7, (0, 180, 255), -1)
            cv2.putText(frame, "BOOM: CLEARING VEHICLE", (w - 165, 44), cv2.FONT_HERSHEY_SIMPLEX, 0.38, (0, 180, 255), 1)
            
        out.write(frame)
        
    out.release()
    save_mp4_and_gif(temp_raw, os.path.join(ASSETS_DIR, "video_unmanned_weighbridge.mp4"), os.path.join(ASSETS_DIR, "video_unmanned_weighbridge.gif"), fps)
    print("CAM-WB01 Unmanned Weighbridge video generated.")

def generate_truck_dashcam_video(num_frames=60, fps=12):
    """CAM-DC01: Inbound Heavy Logistics Truck Forward Dashcam."""
    bg_path = os.path.join(ASSETS_DIR, "cctv_truck_dashcam.jpg")
    base_img = cv2.resize(cv2.imread(bg_path), (960, 540))
    h, w, _ = base_img.shape
    
    temp_raw = os.path.join(ASSETS_DIR, "temp_dc.mp4")
    out = cv2.VideoWriter(temp_raw, cv2.VideoWriter_fourcc(*'mp4v'), fps, (w, h))
    
    for i in range(num_frames):
        frame = base_img.copy()
        
        # 1. Subtle road vibration jitter
        dy = int(np.sin(i * 0.8) * 1)
        if dy != 0:
            M = np.float32([[1, 0, 0], [0, 1, dy]])
            frame = cv2.warpAffine(frame, M, (w, h))
            
        # 2. Target lock pulse on Gate Barrier
        barrier_box_pulse = int(np.sin(i * 0.3) * 4)
        cv2.rectangle(frame, (570 - barrier_box_pulse, 190), (625 + barrier_box_pulse, 350), (0, 0, 255), 2)
        cv2.putText(frame, "[RFID FASTAG: DETECTED]", (520, 180), cv2.FONT_HERSHEY_SIMPLEX, 0.38, (0, 255, 255), 1)
        
        # 3. Real-time Inbound Speed Sensor
        speed = max(0.0, 8.2 - (i / 60.0) * 3.5 + np.sin(i * 0.4) * 0.3)
        cv2.rectangle(frame, (40, 95), (280, 122), (15, 23, 42), -1)
        cv2.putText(frame, f"TELEMETRY SPEED: {speed:.1f} KM/H", (45, 114), cv2.FONT_HERSHEY_SIMPLEX, 0.42, (0, 255, 120), 1)
        
        # 4. Flashing REC indicator
        if i % 14 < 9:
            cv2.circle(frame, (55, 142), 6, (0, 0, 255), -1)
            cv2.putText(frame, "LIVE DASHCAM STREAM", (70, 146), cv2.FONT_HERSHEY_SIMPLEX, 0.38, (255, 255, 255), 1)
            
        # 5. SAP Gate Pass Authorization
        cv2.rectangle(frame, (w - 320, 20), (w - 20, 60), (15, 23, 42), -1)
        cv2.rectangle(frame, (w - 320, 20), (w - 20, 60), (0, 255, 0), 1)
        cv2.putText(frame, "SAP GATE PASS: #GP-8842 VALID", (w - 310, 45), cv2.FONT_HERSHEY_SIMPLEX, 0.38, (0, 255, 120), 1)
        
        out.write(frame)
        
    out.release()
    save_mp4_and_gif(temp_raw, os.path.join(ASSETS_DIR, "video_truck_dashcam.mp4"), os.path.join(ASSETS_DIR, "video_truck_dashcam.gif"), fps)
    print("CAM-DC01 Truck Dashcam video generated.")

def generate_employee_bus_fleet_video(num_frames=60, fps=12):
    """CAM-BUS01: Welspun Employee Transit Terminal & Shuttle Fleet."""
    bg_path = os.path.join(ASSETS_DIR, "cctv_employee_bus_fleet.jpg")
    base_img = cv2.resize(cv2.imread(bg_path), (960, 540))
    h, w, _ = base_img.shape
    
    temp_raw = os.path.join(ASSETS_DIR, "temp_bus01.mp4")
    out = cv2.VideoWriter(temp_raw, cv2.VideoWriter_fourcc(*'mp4v'), fps, (w, h))
    
    for i in range(num_frames):
        frame = base_img.copy()
        
        # 1. Departure Board Flashing Status
        glow = int(np.abs(np.sin(i * 0.2)) * 25)
        overlay = frame.copy()
        cv2.rectangle(overlay, (540, 100), (710, 175), (0, 180 + glow, 50), -1)
        cv2.addWeighted(overlay, 0.25, frame, 0.75, 0, frame)
        
        # 2. Queue AI headcount tracker
        cv2.rectangle(frame, (430, 320), (820, 490), (0, 166, 230), 1)
        cv2.rectangle(frame, (430, 298), (660, 318), (15, 23, 42), -1)
        cv2.putText(frame, "AI BOARDING QUEUE: 24 COMMUTERS", (435, 312), cv2.FONT_HERSHEY_SIMPLEX, 0.38, (0, 166, 230), 1)
        
        # 3. RFID Tap-in Terminal Active
        tap_num = 32 + (i // 15)
        cv2.rectangle(frame, (20, 20), (380, 75), (15, 23, 42), -1)
        cv2.rectangle(frame, (20, 20), (380, 75), (0, 255, 120), 1)
        cv2.putText(frame, f"BUS WB-02 (ANJAR CITY): {tap_num}/42 SEATS", (30, 42), cv2.FONT_HERSHEY_SIMPLEX, 0.44, (0, 255, 120), 1)
        cv2.putText(frame, "RFID TAP-IN SPEED: 0.8s / COMMUTER • ON TIME", (30, 64), cv2.FONT_HERSHEY_SIMPLEX, 0.36, (200, 200, 200), 1)
        
        # 4. Status Indicator
        if i % 14 < 10:
            cv2.circle(frame, (w - 180, 35), 6, (0, 255, 0), -1)
            cv2.putText(frame, "BAY 2: BOARDING ACTIVE", (w - 165, 39), cv2.FONT_HERSHEY_SIMPLEX, 0.38, (0, 255, 0), 1)
            
        out.write(frame)
        
    out.release()
    save_mp4_and_gif(temp_raw, os.path.join(ASSETS_DIR, "video_employee_bus_fleet.mp4"), os.path.join(ASSETS_DIR, "video_employee_bus_fleet.gif"), fps)
    print("CAM-BUS01 Employee Transit video generated.")

def generate_bus_cabin_dashcam_video(num_frames=60, fps=12):
    """CAM-BUS02: Commuter Bus Highway Dashcam & In-Cabin Passenger View."""
    bg_path = os.path.join(ASSETS_DIR, "cctv_bus_dashcam.jpg")
    base_img = cv2.resize(cv2.imread(bg_path), (960, 540))
    h, w, _ = base_img.shape
    
    temp_raw = os.path.join(ASSETS_DIR, "temp_bus02.mp4")
    out = cv2.VideoWriter(temp_raw, cv2.VideoWriter_fourcc(*'mp4v'), fps, (w, h))
    
    for i in range(num_frames):
        frame = base_img.copy()
        
        # 1. Driver Status Monitoring (DSM) AI bounding box
        cv2.rectangle(frame, (620, 170), (715, 290), (0, 255, 120), 2)
        cv2.rectangle(frame, (620, 145), (860, 168), (15, 23, 42), -1)
        cv2.putText(frame, "[DSM: 99.4% ALERT - ZERO FATIGUE]", (625, 161), cv2.FONT_HERSHEY_SIMPLEX, 0.36, (0, 255, 120), 1)
        
        # 2. Highway Speed & Distance Telemetry
        bus_speed = 42.0 + np.sin(i * 0.3) * 1.5
        cv2.rectangle(frame, (20, 60), (390, 105), (15, 23, 42), -1)
        cv2.rectangle(frame, (20, 60), (390, 105), (0, 166, 230), 1)
        cv2.putText(frame, f"HIGHWAY CRUISE SPEED: {bus_speed:.1f} KM/H (LIMIT 50)", (30, 80), cv2.FONT_HERSHEY_SIMPLEX, 0.40, (0, 255, 255), 1)
        cv2.putText(frame, "DESTINATION: WELSPUN CITY TOWNSHIP • 7.4 KM", (30, 98), cv2.FONT_HERSHEY_SIMPLEX, 0.36, (200, 200, 200), 1)
        
        # 3. Passenger Cabin Inset Status
        cv2.rectangle(frame, (10, h - 35), (320, h - 8), (15, 23, 42), -1)
        cv2.putText(frame, "CABIN CCTV: 38/42 SEATS OCCUPIED (90%)", (15, h - 18), cv2.FONT_HERSHEY_SIMPLEX, 0.38, (0, 255, 120), 1)
        
        out.write(frame)
        
    out.release()
    save_mp4_and_gif(temp_raw, os.path.join(ASSETS_DIR, "video_bus_cabin_dashcam.mp4"), os.path.join(ASSETS_DIR, "video_bus_cabin_dashcam.gif"), fps)
    print("CAM-BUS02 Bus Dashcam video generated.")

if __name__ == "__main__":
    print("Generating 4 new logistics and employee transit videos/GIFs...")
    generate_unmanned_weighbridge_video()
    generate_truck_dashcam_video()
    generate_employee_bus_fleet_video()
    generate_bus_cabin_dashcam_video()
    print("All 4 new videos and GIFs successfully generated!")
