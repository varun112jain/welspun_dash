"""
Surveillance, Fire Safety, and Networked Fire Station Data for Welspun Anjar Plant & City
Expanded 8-Camera Multi-Screen Video Wall Matrix with Dual H.264 MP4 and Animated Stream Support.
"""
import os

def get_safety_incident_stats():
    """Returns safety milestone and days since last incident statistics."""
    return {
        "days_since_last_incident": 148,
        "last_incident_date": "2026-05-20",
        "last_incident_desc": "Sector 2 Conveyor Roller Friction Warning (Zero LTI, Zero Property Loss)",
        "safe_man_hours": "4,824,650 Hours",
        "yearly_safety_record": "99.8% Incident-Free",
        "target_days": 365
    }

def get_sensor_health_telemetry():
    """Returns detailed health metrics for networked smoke and fire detection sensors."""
    return {
        "summary": {
            "total_sensors": 3420,
            "operational_sensors": 3398,
            "overall_health_pct": 99.4,
            "loop_voltage_vdc": 24.2,
            "communication_bus_status": "DUAL REDUNDANT FIBER MESH (OPTIMAL)"
        },
        "sensor_categories": [
            {
                "type": "Optical Smoke & Ionization Detectors",
                "total": 2180,
                "healthy": 2168,
                "drift_warning": 12,
                "offline": 0,
                "health_pct": 99.4,
                "calibration_due": 3
            },
            {
                "type": "Radiometric Thermal & IR Flame Detectors",
                "total": 840,
                "healthy": 831,
                "drift_warning": 8,
                "offline": 1,
                "health_pct": 98.9,
                "calibration_due": 1
            },
            {
                "type": "Linear Heat Detection (LHD) Cable Loops",
                "total": 400,
                "healthy": 399,
                "drift_warning": 1,
                "offline": 0,
                "health_pct": 99.8,
                "calibration_due": 0
            }
        ],
        "sector_breakdown": [
            {"sector": "WCL: LSAW & Spiral (HSAW) Pipe Mills", "sensors": 850, "health": "99.8%", "status": "Optimal", "last_test": "Today, 06:00"},
            {"sector": "WDI: 500k TPA Blast Furnace, Sinter & DI Pipe Foundry", "sensors": 640, "health": "99.4%", "status": "Optimal", "last_test": "Today, 06:10"},
            {"sector": "WLL: Home Textiles & Advanced Spunlace Facility", "sensors": 1020, "health": "99.1%", "status": "Optimal", "last_test": "Today, 06:15"},
            {"sector": "Energy: 123 MW Captive Thermal Plant & 42 MW Solar", "sensors": 380, "health": "97.4%", "status": "Alert Active", "last_test": "Continuous"},
            {"sector": "Welspun City: Township, Vidya Mandir & Health Centre", "sensors": 530, "health": "100.0%", "status": "Optimal", "last_test": "Today, 07:00"}
        ]
    }

def get_camera_network_telemetry():
    """Returns detailed online/total statistics for the entire CCTV camera network across Welspun City."""
    return {
        "total_cameras": 1438,
        "online_cameras": 1424,
        "offline_cameras": 14,
        "uptime_pct": 99.03,
        "wcl_pipes": {"online": 410, "total": 414, "pct": 99.0},
        "wdi_ductile": {"online": 402, "total": 406, "pct": 99.0},
        "wll_textiles": {"online": 390, "total": 392, "pct": 99.5},
        "cpp_solar": {"online": 124, "total": 126, "pct": 98.4},
        "welspun_city": {"online": 348, "total": 350, "pct": 99.4},
        "perimeter_gates": {"online": 216, "total": 218, "pct": 99.1},
        "emergency_fire": {"online": 48, "total": 50, "pct": 96.0}
    }

def get_surveillance_kpis():
    """Returns top-level KPIs for Welspun City, Anjar surveillance."""
    return {
        "cameras_online": {"value": "1,424 / 1,438", "sub": "99.0% Active • 14 Maint.", "status": "optimal", "label": "Active CCTV Feeds"},
        "days_incident_free": {"value": "148 Days", "sub": "4.82M Safe Man-Hours", "status": "optimal", "label": "Safety Milestone"},
        "perimeter_crossings": {"value": "1 Breach", "sub": "220kV Yard Perimeter", "status": "critical", "label": "Perimeter Crossing"},
        "active_fire_alarms": {"value": "1 Alert", "sub": "123MW CPP Steam Header", "status": "critical", "label": "Active Fire & Alarms"},
        "sensor_health": {"value": "99.4%", "sub": "3,398 / 3,420 Detectors", "status": "optimal", "label": "Smoke & Fire Sensors"},
        "fire_station_readiness": {"value": "Station Alpha & Bravo", "sub": "5 Tenders • Hydrant 8.6 Bar", "status": "optimal", "label": "Fire Command Hub"}
    }

def get_cctv_feeds():
    """Returns 8 active CCTV screens across Welspun City (WCL, WDI, WLL, 123MW CPP, Solar, and Township)."""
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "assets"))
    
    return [
        {
            "id": "CAM-04",
            "name": "220kV Grid Substation & Hazmat Yard",
            "zone": "Welspun City Perimeter & 220kV Grid",
            "sector": "Captive Power Grid - West Boundary",
            "video": os.path.join(base_dir, "video_perimeter_breach.mp4"),
            "gif": os.path.join(base_dir, "video_perimeter_breach.gif"),
            "image": os.path.join(base_dir, "cctv_perimeter_fence.jpg"),
            "status": "CRITICAL BREACH",
            "status_color": "#EF4444",
            "activity_rank": 1,
            "fps": 15,
            "bitrate": "4.8 Mbps",
            "ai_features": ["Virtual Laser Tripwire", "220kV Substation Radar", "Photographic Intruder AI"],
            "ai_summary": "🚨 INTRUSION ALERT: Subject crossed Virtual Tripwire near 220kV switchyard feeding WCL mills, WDI Blast Furnace & WLL plant. Security QRT dispatched.",
            "thermal_temp": "24.6°C",
            "alert_badge": "PERIMETER CROSSING ACTIVE"
        },
        {
            "id": "CAM-02",
            "name": "123 MW Captive Thermal Plant & Solar Array",
            "zone": "123 MW Captive Thermal Plant & Solar",
            "sector": "CPP Unit 2 - Steam Header & Boiler Loop",
            "video": os.path.join(base_dir, "video_thermal_hotspot.mp4"),
            "gif": os.path.join(base_dir, "video_thermal_hotspot.gif"),
            "image": os.path.join(base_dir, "cctv_thermal_hotspot.jpg"),
            "status": "CRITICAL ANOMALY",
            "status_color": "#EF4444",
            "activity_rank": 2,
            "fps": 15,
            "bitrate": "3.8 Mbps",
            "ai_features": ["FLIR Radiometric Heatmap", "123MW Steam Header Sensor", "42MW Solar Inverter Sync"],
            "ai_summary": "🔥 DANGER: Hot spot on HP Steam Header HX-104 (98.4°C vs limit 85°C). 42 MW solar array delivering 38.6 MW.",
            "thermal_temp": "98.4°C (Limit: 85°C)",
            "alert_badge": "HOT SPOT DETECTED"
        },
        {
            "id": "CAM-01",
            "name": "WDI 500k TPA Blast Furnace & DI Casting Bay",
            "zone": "WDI Blast Furnace & Metallurgical Complex",
            "sector": "MBF Tap Hole, Tuyere Gallery & DI Centrifugal Casting",
            "video": os.path.join(base_dir, "video_plant_mill.mp4"),
            "gif": os.path.join(base_dir, "video_plant_mill.gif"),
            "image": os.path.join(base_dir, "cctv_plant_spinning.jpg"),
            "status": "OPTIMAL",
            "status_color": "#005BAA",
            "activity_rank": 4,
            "fps": 15,
            "bitrate": "4.2 Mbps",
            "ai_features": ["Tuyere & Tap Hole Thermal AI (1,480°C)", "BFG / CO Gas Sensor Network", "Hot Metal Ladle Car Clearance AI"],
            "ai_summary": "500k TPA Blast Furnace tapping hot metal at 1,480°C into ladle car. Sinter feed & PCI rates nominal. BFG gas scrubbers optimal. DN 600 DI centrifugal pipe casting active.",
            "thermal_temp": "1,480°C (Tap Hole) / 28.4°C Ambient",
            "alert_badge": "BLAST FURNACE & DI OPTIMAL"
        },
        {
            "id": "CAM-03",
            "name": "Fire Station Alpha (Heavy Industrial Core)",
            "zone": "Emergency Services Hub",
            "sector": "Station Alpha - Near WCL Mills, WDI Blast Furnace & CPP",
            "video": os.path.join(base_dir, "video_fire_station.mp4"),
            "gif": os.path.join(base_dir, "video_fire_station.gif"),
            "image": os.path.join(base_dir, "cctv_fire_station.jpg"),
            "status": "EMERGENCY READY",
            "status_color": "#005BAA",
            "activity_rank": 3,
            "fps": 15,
            "bitrate": "6.0 Mbps",
            "ai_features": ["Foam Tender Ready Beacon", "Hazmat Muster Console", "8.6 Bar Hydrant Ring Sync"],
            "ai_summary": "Foam Tender 01 & 04 armed for Blast Furnace, DI Foundry & Chemical lines. Ring hydrant loop at 8.6 Bar.",
            "thermal_temp": "24.1°C",
            "alert_badge": "DISPATCH READY"
        },
        {
            "id": "CAM-05",
            "name": "Welspun City Township - Aura Gardens & Quarters",
            "zone": "Welspun City Township",
            "sector": "Residential Block C & Main Boulevard",
            "video": os.path.join(base_dir, "video_township_quarters.mp4"),
            "gif": os.path.join(base_dir, "video_township_quarters.gif"),
            "image": os.path.join(base_dir, "cctv_township_quarters.jpg"),
            "status": "NORMAL",
            "status_color": "#10B981",
            "activity_rank": 5,
            "fps": 15,
            "bitrate": "5.4 Mbps",
            "ai_features": ["Township Crosswalk Radar", "Speed Radar (Limit: 30 km/h)", "Night Perimeter Beam"],
            "ai_summary": "Normal township movement. 5 residents tracked. Vehicle speed: 18 km/h (within 30 km/h limit). Zero violations.",
            "thermal_temp": "22.8°C",
            "alert_badge": "TOWNSHIP SECURE"
        },
        {
            "id": "CAM-06",
            "name": "WCL Line Pipe Mills: LSAW & Spiral (HSAW)",
            "zone": "WCL Large Diameter Pipe Mills",
            "sector": "WCL Mill 1 - Heavy LSAW & Spiral Seam Bay",
            "video": os.path.join(base_dir, "video_plant_mill.mp4"),
            "gif": os.path.join(base_dir, "video_plant_mill.gif"),
            "image": os.path.join(base_dir, "cctv_plant_spinning.jpg"),
            "status": "NORMAL",
            "status_color": "#10B981",
            "activity_rank": 6,
            "fps": 15,
            "bitrate": "4.5 Mbps",
            "ai_features": ["56\" LSAW Seam Ultrasonic AI", "Spiral/HSAW Forming Clearance", "Overhead Gantry Exclusion"],
            "ai_summary": "LSAW 56\" API line pipe submerged arc welding running. Hydrotester at 210 Bar. Gantry exclusion zone 100% clear.",
            "thermal_temp": "29.1°C",
            "alert_badge": "MILLS NORMAL"
        },
        {
            "id": "CAM-07",
            "name": "WLL Home Textiles & Advanced Spunlace Facility",
            "zone": "WLL Home & Advanced Textiles",
            "sector": "WLL Plant 3 - Terry Towels & Spunlace Non-Woven",
            "video": os.path.join(base_dir, "video_perimeter_breach.mp4"),
            "gif": os.path.join(base_dir, "video_perimeter_breach.gif"),
            "image": os.path.join(base_dir, "cctv_perimeter_fence.jpg"),
            "status": "NORMAL",
            "status_color": "#10B981",
            "activity_rank": 7,
            "fps": 15,
            "bitrate": "5.0 Mbps",
            "ai_features": ["Spunlace Hydro-Entangle AI", "Air-Jet Loom Lint Watchdog", "Worker PPE Compliance"],
            "ai_summary": "Advanced Spunlace line producing 50 GSM wipes fabric. All 48 air-jet looms running at 94% efficiency. Zero lint sparks.",
            "thermal_temp": "25.2°C",
            "alert_badge": "TEXTILES OPTIMAL"
        },
        {
            "id": "CAM-08",
            "name": "Welspun Vidya Mandir & Health Centre",
            "zone": "Welspun City Township",
            "sector": "Vidya Mandir Campus & Hospital Bay",
            "video": os.path.join(base_dir, "video_township_quarters.mp4"),
            "gif": os.path.join(base_dir, "video_township_quarters.gif"),
            "image": os.path.join(base_dir, "cctv_township_quarters.jpg"),
            "status": "OPTIMAL",
            "status_color": "#005BAA",
            "activity_rank": 8,
            "fps": 15,
            "bitrate": "4.1 Mbps",
            "ai_features": ["Vidya Mandir Safety Boundary", "Hospital Ambulance Priority", "Rooftop Solar PV Monitor"],
            "ai_summary": "Hospital ambulance slipway 100% unobstructed. Vidya Mandir school perimeter secured. 1.2 MW rooftop solar active.",
            "thermal_temp": "23.4°C",
            "alert_badge": "CAMPUS SECURE"
        }
    ]

def get_fire_network_status():
    """Returns networked fire station telemetry, fleet readiness, and water ring telemetry."""
    return {
        "stations": [
            {
                "id": "FS-01",
                "name": "Station Alpha (Heavy Industrial Core)",
                "readiness": "100% OPERATIONAL",
                "crew_on_duty": 16,
                "coverage": "WCL (LSAW & Spiral Mills), WDI (500k TPA Blast Furnace, Sinter Plant & DI Foundry), 123 MW Captive Power Plant",
                "distance_to_core": "0.3 km"
            },
            {
                "id": "FS-02",
                "name": "Station Bravo (Welspun City Township Hub)",
                "readiness": "100% OPERATIONAL",
                "crew_on_duty": 10,
                "coverage": "Welspun City Quarters, Vidya Mandir School, Health Centre & 42 MW Solar Array",
                "distance_to_core": "1.2 km"
            }
        ],
        "fleet": [
            {"id": "WF-01", "name": "Heavy Water Bowser (12,000L)", "station": "Station Alpha", "status": "Ready", "fuel": "98%", "foam_lvl": "100%"},
            {"id": "WF-02", "name": "Industrial Foam Crash Tender", "station": "Station Alpha", "status": "Ready", "fuel": "95%", "foam_lvl": "94%"},
            {"id": "WF-03", "name": "Hydraulic Sky-Lift & Rescue (32m)", "station": "Station Bravo", "status": "Ready", "fuel": "92%", "foam_lvl": "N/A"},
            {"id": "WF-04", "name": "Quick Response Vehicle (QRV)", "station": "Station Alpha", "status": "Dispatched (CPP)", "fuel": "88%", "foam_lvl": "100%"}
        ],
        "hydrant_telemetry": {
            "main_ring_pressure_bar": 8.6,
            "target_pressure_bar": 8.0,
            "static_water_reserves_litres": "4,250,000 L (96.4%)",
            "active_hydrant_posts": 348,
            "jockey_pump_status": "AUTO STANDBY",
            "diesel_main_pump_status": "READY / AUTO-START",
            "network_connectivity": "FIBER OPTIC MESH (100% DUAL-LINK)"
        }
    }

def get_active_alarms():
    """Returns active and recent safety/fire incidents in Welspun City, Anjar."""
    from datetime import datetime, timedelta
    now = datetime.now()
    return [
        {
            "id": "ALM-9025",
            "time": (now - timedelta(minutes=1)).strftime("%H:%M:%S"),
            "location": "220kV Grid Substation - West Tripwire Line",
            "zone": "Welspun City Substation Perimeter",
            "type": "🚷 Perimeter Crossing (Unauthorized Area Intrusion)",
            "severity": "CRITICAL",
            "details": "AI Camera CAM-04 detected unauthorized subject crossing virtual laser boundary near 220kV grid feeding WCL line pipe mills, WDI Blast Furnace & WLL textiles.",
            "action_taken": "Security Quick Response Patrol dispatched; audible boundary warning siren triggered.",
            "status": "In Progress"
        },
        {
            "id": "ALM-9021",
            "time": (now - timedelta(minutes=5)).strftime("%H:%M:%S"),
            "location": "123 MW Captive Thermal Plant - HP Steam Header HX-104",
            "zone": "Captive Power Generation (CPP)",
            "type": "🔥 Thermal Anomaly (Hot Spot >90°C)",
            "severity": "CRITICAL",
            "details": "FLIR camera detected surface temperature reaching 98.4°C on high-pressure steam distribution header.",
            "action_taken": "QRV Unit WF-04 dispatched for thermal mitigation & isolation check.",
            "status": "In Progress"
        },
        {
            "id": "ALM-9018",
            "time": (now - timedelta(minutes=27)).strftime("%H:%M:%S"),
            "location": "WLL Plant 3 - Advanced Spunlace Air Filtration Unit",
            "zone": "WLL Home & Advanced Textiles",
            "type": "💨 Smoke Ionization Drift",
            "severity": "WARNING",
            "details": "Particulate sensor detected micro-lint drift on hydro-entangling exhaust. Automated HEPA cycle purge cleared.",
            "action_taken": "Filter purge completed. Normal baseline restored.",
            "status": "Resolved"
        },
        {
            "id": "ALM-9010",
            "time": (now - timedelta(hours=2, minutes=12)).strftime("%H:%M:%S"),
            "location": "Pipe Coating Yard - Gantry 4",
            "zone": "Pipe Plant",
            "type": "👷 AI PPE Compliance Breach",
            "severity": "WARNING",
            "details": "2 contract maintenance workers detected without high-visibility vests.",
            "action_taken": "Floor supervisor alerted via mobile radio; PPE provided immediately.",
            "status": "Resolved"
        }
    ]
