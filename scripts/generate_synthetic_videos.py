"""
Synthetic Video Generator for Welspun Anjar Surveillance Dashboard
Generates lightweight, seamless looping MP4 surveillance video clips using OpenCV.
"""
import os
import cv2
import numpy as np

ASSETS_DIR = os.path.join(os.path.dirname(__file__), "..", "assets")

def create_perimeter_breach_video(output_path, num_frames=90, fps=15):
    """Generates synthetic video of perimeter crossing and unauthorized intruder detection."""
    bg_path = os.path.join(ASSETS_DIR, "cctv_perimeter_fence.jpg")
    if os.path.exists(bg_path):
        base_img = cv2.imread(bg_path)
    else:
        base_img = np.zeros((540, 960, 3), dtype=np.uint8)
        
    base_img = cv2.resize(base_img, (960, 540))
    h, w, _ = base_img.shape
    
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(output_path, fourcc, fps, (w, h))
    
    # Tripwire coordinates across the path
    line_pt1 = (180, 220)
    line_pt2 = (420, 500)
    
    for i in range(num_frames):
        frame = base_img.copy()
        t = i / float(num_frames)
        
        # Intruder movement across the gravel road crossing the tripwire
        # Start at (200, 260) -> End at (380, 440)
        person_x = int(210 + t * 180)
        person_y = int(280 + t * 140)
        box_w = 45
        box_h = 80
        
        # Check if crossed tripwire (threshold around frame 30)
        is_breached = i > 30
        
        # 1. Draw Tripwire laser line
        line_color = (0, 0, 255) if is_breached and (i % 6 < 3) else (255, 200, 0)
        cv2.line(frame, line_pt1, line_pt2, line_color, 2, cv2.LINE_AA)
        cv2.putText(frame, "[VIRTUAL TRIPWIRE SECTOR-4]", (line_pt1[0] - 30, line_pt1[1] - 10), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.45, line_color, 1, cv2.LINE_AA)
        
        # 2. Draw person silhouette
        overlay = frame.copy()
        # Head
        cv2.circle(overlay, (person_x + box_w // 2, person_y + 15), 12, (20, 20, 30), -1)
        # Body
        cv2.rectangle(overlay, (person_x + 10, person_y + 27), (person_x + box_w - 10, person_y + box_h), (30, 30, 45), -1)
        # Blend silhouette into scene
        cv2.addWeighted(overlay, 0.7, frame, 0.3, 0, frame)
        
        # 3. AI Bounding Box around intruder
        box_color = (0, 0, 255) if is_breached else (0, 255, 255)
        cv2.rectangle(frame, (person_x, person_y), (person_x + box_w, person_y + box_h), box_color, 2)
        
        # Corner brackets
        c_len = 10
        cv2.line(frame, (person_x, person_y), (person_x + c_len, person_y), box_color, 3)
        cv2.line(frame, (person_x, person_y), (person_x, person_y + c_len), box_color, 3)
        cv2.line(frame, (person_x + box_w, person_y), (person_x + box_w - c_len, person_y), box_color, 3)
        cv2.line(frame, (person_x + box_w, person_y), (person_x + box_w, person_y + c_len), box_color, 3)
        
        # AI Label
        if is_breached:
            label = "ALM: UNAUTHORIZED INTRUDER"
            sub_label = "PERIMETER CROSSING DETECTED"
            # Flashing banner
            if i % 10 < 6:
                cv2.rectangle(frame, (250, 40), (710, 85), (0, 0, 200), -1)
                cv2.putText(frame, "CRITICAL: UNAUTHORIZED AREA BREACH", (265, 70), 
                            cv2.FONT_HERSHEY_DUPLEX, 0.65, (255, 255, 255), 2, cv2.LINE_AA)
        else:
            label = "TARGET DETECTED"
            sub_label = "APPROACHING BOUNDARY"
            
        cv2.rectangle(frame, (person_x - 10, person_y - 30), (person_x + box_w + 100, person_y - 5), (10, 10, 20), -1)
        cv2.putText(frame, label, (person_x - 5, person_y - 18), cv2.FONT_HERSHEY_SIMPLEX, 0.38, box_color, 1, cv2.LINE_AA)
        cv2.putText(frame, sub_label, (person_x - 5, person_y - 8), cv2.FONT_HERSHEY_SIMPLEX, 0.32, (200, 200, 200), 1, cv2.LINE_AA)
        
        # HUD Overlays
        cv2.putText(frame, f"CAM-04 PERIMETER WEST | FPS: 15 | AI: ACTIVE", (20, 30), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 255), 1, cv2.LINE_AA)
        sec_str = f"23:48:{20 + (i // 15):02d}.{int((i % 15) * 6.6):02d}"
        cv2.putText(frame, f"TIME: {sec_str}", (w - 220, 30), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1, cv2.LINE_AA)
                    
        # Blinking REC dot
        if i % 12 < 8:
            cv2.circle(frame, (35, h - 25), 7, (0, 0, 255), -1)
            cv2.putText(frame, "REC [LIVE STREAM]", (50, h - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.45, (255, 255, 255), 1)
            
        out.write(frame)
        
    out.release()
    print("Generated perimeter breach video:", output_path)

def create_thermal_hotspot_video(output_path, num_frames=75, fps=15):
    """Generates synthetic video of thermal hotspot fluctuation and alarm triggering."""
    bg_path = os.path.join(ASSETS_DIR, "cctv_thermal_hotspot.jpg")
    if os.path.exists(bg_path):
        base_img = cv2.imread(bg_path)
    else:
        base_img = np.zeros((540, 960, 3), dtype=np.uint8)
    base_img = cv2.resize(base_img, (960, 540))
    h, w, _ = base_img.shape
    
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(output_path, fourcc, fps, (w, h))
    
    valve_x, valve_y = 210, 200
    
    for i in range(num_frames):
        frame = base_img.copy()
        
        # Temperature oscillation
        temp = 97.0 + 2.5 * np.sin(i * 0.25) + (i % 3) * 0.2
        
        # Pulsing heat glow on valve
        glow_radius = int(50 + 10 * np.sin(i * 0.3))
        overlay = frame.copy()
        cv2.circle(overlay, (valve_x, valve_y), glow_radius, (0, 80, 255), -1)
        cv2.addWeighted(overlay, 0.35, frame, 0.65, 0, frame)
        
        # FLIR reticle crosshair
        cv2.circle(frame, (valve_x, valve_y), 16, (255, 255, 255), 1)
        cv2.line(frame, (valve_x - 24, valve_y), (valve_x + 24, valve_y), (255, 255, 255), 1)
        cv2.line(frame, (valve_x, valve_y - 24), (valve_x, valve_y + 24), (255, 255, 255), 1)
        
        # Flashing alarm text box
        box_color = (0, 0, 255) if i % 8 < 5 else (0, 140, 255)
        cv2.rectangle(frame, (valve_x + 30, valve_y - 45), (valve_x + 230, valve_y + 15), (10, 10, 30), -1)
        cv2.rectangle(frame, (valve_x + 30, valve_y - 45), (valve_x + 230, valve_y + 15), box_color, 2)
        cv2.putText(frame, f"HOT SPOT: {temp:.1f} C", (valve_x + 40, valve_y - 20), 
                    cv2.FONT_HERSHEY_DUPLEX, 0.55, box_color, 1, cv2.LINE_AA)
        cv2.putText(frame, "VALVE HX-104 (CRITICAL)", (valve_x + 40, valve_y + 3), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.4, (200, 200, 200), 1, cv2.LINE_AA)
        
        # Scanlines effect
        for y in range(0, h, 6):
            cv2.line(frame, (0, y), (w, y), (0, 0, 0), 1)
            
        # Top HUD
        cv2.putText(frame, "FLIR RADIOMETRIC A700 | SECTOR 4 UTILITY HUB", (20, 30), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 255), 1)
        cv2.putText(frame, f"MAX TEMP: {temp:.1f} C (LIMIT: 85.0 C)", (w - 320, 30), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
                    
        out.write(frame)
        
    out.release()
    print("Generated thermal hotspot video:", output_path)

def create_plant_mill_video(output_path, num_frames=75, fps=15):
    """Generates synthetic video of active manufacturing plant floor."""
    bg_path = os.path.join(ASSETS_DIR, "cctv_plant_spinning.jpg")
    if os.path.exists(bg_path):
        base_img = cv2.imread(bg_path)
    else:
        base_img = np.zeros((540, 960, 3), dtype=np.uint8)
    base_img = cv2.resize(base_img, (960, 540))
    h, w, _ = base_img.shape
    
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(output_path, fourcc, fps, (w, h))
    
    for i in range(num_frames):
        frame = base_img.copy()
        
        # Forklift movement tracking
        fk_x = int(680 + 15 * np.sin(i * 0.15))
        fk_y = int(320 + 8 * np.cos(i * 0.15))
        cv2.rectangle(frame, (fk_x, fk_y), (fk_x + 85, fk_y + 70), (0, 255, 0), 2)
        cv2.putText(frame, "[T-03: FORKLIFT SPEED: 6 KM/H]", (fk_x - 20, fk_y - 8), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.38, (0, 255, 0), 1)
        
        # Workers AI boxes with green PPE Compliant badge
        w1_x = int(500 + 4 * np.sin(i * 0.3))
        w1_y = int(250 + 2 * np.cos(i * 0.3))
        cv2.rectangle(frame, (w1_x, w1_y), (w1_x + 35, w1_y + 75), (0, 255, 120), 2)
        cv2.putText(frame, "[PPE OK: HELMET/VEST 100%]", (w1_x - 30, w1_y - 6), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.34, (0, 255, 120), 1)
                    
        # Camera HUD
        cv2.putText(frame, "CAM-01 TEXTILE & SPINNING MILL 3 | AI PPE MONITOR", (20, 30), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 255), 1)
        cv2.putText(frame, "SAFETY COMPLIANCE: 100%", (w - 240, 30), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)
                    
        # Blinking green operational indicator
        if i % 14 < 10:
            cv2.circle(frame, (35, h - 25), 6, (0, 255, 0), -1)
            cv2.putText(frame, "ALL ZONES SECURE", (50, h - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.42, (255, 255, 255), 1)
            
        out.write(frame)
        
    out.release()
    print("Generated plant mill video:", output_path)

def create_fire_station_video(output_path, num_frames=75, fps=15):
    """Generates synthetic video of fire station bay with flashing emergency beacons."""
    bg_path = os.path.join(ASSETS_DIR, "cctv_fire_station.jpg")
    if os.path.exists(bg_path):
        base_img = cv2.imread(bg_path)
    else:
        base_img = np.zeros((540, 960, 3), dtype=np.uint8)
    base_img = cv2.resize(base_img, (960, 540))
    h, w, _ = base_img.shape
    
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(output_path, fourcc, fps, (w, h))
    
    for i in range(num_frames):
        frame = base_img.copy()
        
        # Flashing emergency beacon lights atop fire engines
        if i % 8 < 4:
            overlay = frame.copy()
            # Strobe on Engine 7
            cv2.circle(overlay, (310, 200), 40, (0, 0, 255), -1)
            # Strobe on Engine 4
            cv2.circle(overlay, (560, 230), 40, (0, 180, 255), -1)
            cv2.addWeighted(overlay, 0.45, frame, 0.55, 0, frame)
            
        # Console status
        cv2.rectangle(frame, (530, 480), (750, 520), (10, 20, 40), -1)
        cv2.rectangle(frame, (530, 480), (750, 520), (0, 200, 255), 1)
        cv2.putText(frame, "FIRE NET: DUAL LINK OK", (540, 505), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.42, (0, 255, 255), 1)
                    
        # Camera HUD
        cv2.putText(frame, "CAM-03 ANJAR CENTRAL FIRE STATION BAY | READY", (20, 30), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 255), 1)
        cv2.putText(frame, "STATION ALPHA - READY", (w - 220, 30), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)
                    
        out.write(frame)
        
    out.release()
    print("Generated fire station video:", output_path)

def create_township_quarters_video(output_path, num_frames=75, fps=15):
    """Generates synthetic video of Welspun City living quarters with pedestrian & vehicle tracking."""
    bg_path = os.path.join(ASSETS_DIR, "cctv_township_quarters.jpg")
    if os.path.exists(bg_path):
        base_img = cv2.imread(bg_path)
    else:
        base_img = np.zeros((540, 960, 3), dtype=np.uint8)
    base_img = cv2.resize(base_img, (960, 540))
    h, w, _ = base_img.shape
    
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(output_path, fourcc, fps, (w, h))
    
    for i in range(num_frames):
        frame = base_img.copy()
        t = i / float(num_frames)
        
        # Pedestrian 1 moving along the sidewalk
        ped1_x = int(220 + t * 40)
        ped1_y = int(370 - t * 20)
        cv2.rectangle(frame, (ped1_x, ped1_y), (ped1_x + 35, ped1_y + 80), (0, 255, 255), 2)
        cv2.putText(frame, "[PEDESTRIAN 04]", (ped1_x - 10, ped1_y - 6), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.35, (0, 255, 255), 1)
        
        # Car radar box tracking on road
        car_x = int(720 - t * 25)
        car_y = int(320 + t * 30)
        cv2.rectangle(frame, (car_x, car_y), (car_x + 70, car_y + 60), (0, 255, 100), 2)
        speed = int(18 + 2 * np.sin(i * 0.2))
        cv2.putText(frame, f"[VEHICLE: {speed} KM/H - OK]", (car_x - 15, car_y - 8), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.35, (0, 255, 100), 1)
        
        # HUD Overlays
        cv2.putText(frame, "CAM-05 WELSPUN CITY TOWNSHIP | AURA GARDENS", (20, 30), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 255), 1)
        cv2.putText(frame, "MOTION DETECT: ACTIVE | ALL COMPLIANT", (w - 360, 30), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.48, (0, 255, 120), 1)
                    
        out.write(frame)
    out.release()
    print("Generated township quarters video:", output_path)

if __name__ == "__main__":
    os.makedirs(ASSETS_DIR, exist_ok=True)
    create_perimeter_breach_video(os.path.join(ASSETS_DIR, "video_perimeter_breach.mp4"))
    create_thermal_hotspot_video(os.path.join(ASSETS_DIR, "video_thermal_hotspot.mp4"))
    create_plant_mill_video(os.path.join(ASSETS_DIR, "video_plant_mill.mp4"))
    create_fire_station_video(os.path.join(ASSETS_DIR, "video_fire_station.mp4"))
    create_township_quarters_video(os.path.join(ASSETS_DIR, "video_township_quarters.mp4"))
    print("All synthetic surveillance videos generated successfully!")
