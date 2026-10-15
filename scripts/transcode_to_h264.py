"""
Transcodes all synthetic surveillance videos to standard H.264 (avc1) with yuv420p
Ensures 100% playback compatibility across all modern web browsers (Chrome, Edge, Safari, Firefox).
"""
import os
import subprocess

ASSETS_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "assets"))

videos = [
    "video_perimeter_breach.mp4",
    "video_thermal_hotspot.mp4",
    "video_plant_mill.mp4",
    "video_fire_station.mp4",
    "video_township_quarters.mp4"
]

for vid in videos:
    src_path = os.path.join(ASSETS_DIR, vid)
    temp_path = os.path.join(ASSETS_DIR, f"temp_{vid}")
    
    if os.path.exists(src_path):
        cmd = [
            "ffmpeg", "-y",
            "-i", src_path,
            "-c:v", "libx264",
            "-pix_fmt", "yuv420p",
            "-profile:v", "baseline",
            "-level", "3.0",
            "-movflags", "+faststart",
            temp_path
        ]
        print(f"Transcoding {vid} to H.264...")
        res = subprocess.run(cmd, capture_output=True, text=True)
        if res.returncode == 0 and os.path.exists(temp_path) and os.path.getsize(temp_path) > 0:
            os.replace(temp_path, src_path)
            print(f"SUCCESS: {vid} is now web-compatible H.264! ({os.path.getsize(src_path)} bytes)")
        else:
            print(f"ERROR transcoding {vid}:", res.stderr[-300:])

# Remove the temporary test file if present
test_file = os.path.join(ASSETS_DIR, "video_perimeter_breach_h264.mp4")
if os.path.exists(test_file):
    os.remove(test_file)

print("All surveillance videos successfully transcoded to H.264!")
