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
            {"sector": "Sector 1: Welspun Pipe & Steel Mill", "sensors": 850, "health": "99.8%", "status": "Optimal", "last_test": "Today, 06:00"},
            {"sector": "Sector 2: Welspun Textile & Spunlace", "sensors": 1120, "health": "99.1%", "status": "Optimal", "last_test": "Today, 06:15"},
            {"sector": "Sector 3: Advanced Flooring Unit", "sensors": 540, "health": "99.6%", "status": "Optimal", "last_test": "Today, 06:30"},
            {"sector": "Sector 4: Chemical & Thermal Utility Hub", "sensors": 380, "health": "97.4%", "status": "Alert Active", "last_test": "Continuous"},
            {"sector": "Welspun City: Residential Quarters & Hostels", "sensors": 530, "health": "100.0%", "status": "Optimal", "last_test": "Today, 07:00"}
        ]
    }

def get_camera_network_telemetry():
    """Returns detailed online/total statistics for the entire CCTV camera network."""
    return {
        "total_cameras": 1438,
        "online_cameras": 1424,
        "offline_cameras": 14,
        "uptime_pct": 99.03,
        "plant_core": {"online": 812, "total": 820, "pct": 99.0},
        "perimeter_gates": {"online": 216, "total": 218, "pct": 99.1},
        "welspun_city": {"online": 348, "total": 350, "pct": 99.4},
        "emergency_fire": {"online": 48, "total": 50, "pct": 96.0}
    }

def get_surveillance_kpis():
    """Returns top-level KPIs for Anjar Plant & City surveillance."""
    return {
        "cameras_online": {"value": "1,424 / 1,438", "sub": "99.0% Active • 14 Maint.", "status": "optimal", "label": "Active CCTV Feeds"},
        "days_incident_free": {"value": "148 Days", "sub": "4.82M Safe Man-Hours", "status": "optimal", "label": "Safety Milestone"},
        "perimeter_crossings": {"value": "1 Breach", "sub": "Sector 4 West Tripwire", "status": "critical", "label": "Perimeter Crossing"},
        "active_fire_alarms": {"value": "1 Alert", "sub": "Sector 4 Thermal Anomaly", "status": "critical", "label": "Active Fire & Alarms"},
        "sensor_health": {"value": "99.4%", "sub": "3,398 / 3,420 Detectors", "status": "optimal", "label": "Smoke & Fire Sensors"},
        "fire_station_readiness": {"value": "Station 01 & 02", "sub": "4 Tenders • Hydrant 8.6 Bar", "status": "optimal", "label": "Fire Command Hub"}
    }

def get_cctv_feeds():
    """Returns 8 active CCTV screens across Welspun Anjar Plant, Perimeter, and Living Quarters."""
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "assets"))
    
    return [
        {
            "id": "CAM-04",
            "name": "Restricted Perimeter & Substation Fence",
            "zone": "Plant Perimeter (Restricted)",
            "sector": "Sector 4 - West Tripwire Boundary",
            "video": os.path.join(base_dir, "video_perimeter_breach.mp4"),
            "gif": os.path.join(base_dir, "video_perimeter_breach.gif"),
            "image": os.path.join(base_dir, "cctv_perimeter_fence.jpg"),
            "status": "CRITICAL BREACH",
            "status_color": "#EF4444",
            "activity_rank": 1,
            "fps": 15,
            "bitrate": "4.8 Mbps",
            "ai_features": ["Virtual Laser Tripwire", "Unauthorized Person Intrusion", "Night IR Motion"],
            "ai_summary": "🚨 INTRUSION ALERT: Subject crossed Virtual Tripwire Line into high-voltage yard. Horn sounded.",
            "thermal_temp": "24.6°C",
            "alert_badge": "PERIMETER CROSSING ACTIVE"
        },
        {
            "id": "CAM-02",
            "name": "Chemical & Thermal Pipeline Grid",
            "zone": "Plant Core (Industrial)",
            "sector": "Sector 4 - Utility Hub",
            "video": os.path.join(base_dir, "video_thermal_hotspot.mp4"),
            "gif": os.path.join(base_dir, "video_thermal_hotspot.gif"),
            "image": os.path.join(base_dir, "cctv_thermal_hotspot.jpg"),
            "status": "CRITICAL ANOMALY",
            "status_color": "#EF4444",
            "activity_rank": 2,
            "fps": 15,
            "bitrate": "3.8 Mbps",
            "ai_features": ["FLIR Radiometric Heatmap", "Hot Spot Alarm (>90°C)", "Line Pressure Sync"],
            "ai_summary": "🔥 DANGER: Hot spot on Valve HX-104 (98.4°C vs threshold 85°C). Cooling mitigation dispatched.",
            "thermal_temp": "98.4°C (Limit: 85°C)",
            "alert_badge": "HOT SPOT DETECTED"
        },
        {
            "id": "CAM-01",
            "name": "Textile Weaving & Spinning Mill",
            "zone": "Plant Core (Industrial)",
            "sector": "Sector 2 - Textile Bay 3",
            "video": os.path.join(base_dir, "video_plant_mill.mp4"),
            "gif": os.path.join(base_dir, "video_plant_mill.gif"),
            "image": os.path.join(base_dir, "cctv_plant_spinning.jpg"),
            "status": "NORMAL",
            "status_color": "#10B981",
            "activity_rank": 4,
            "fps": 15,
            "bitrate": "4.2 Mbps",
            "ai_features": ["AI PPE Helmet/Vest Compliance", "Forklift Lane Safety", "Loom Smoke Sensor"],
            "ai_summary": "All personnel 100% PPE compliant. Forklift speed: 6 km/h. Zero safety violations.",
            "thermal_temp": "28.4°C",
            "alert_badge": "ZONE NORMAL"
        },
        {
            "id": "CAM-03",
            "name": "Networked Fire Station Bay 01",
            "zone": "Emergency Services",
            "sector": "Central Command Station Alpha",
            "video": os.path.join(base_dir, "video_fire_station.mp4"),
            "gif": os.path.join(base_dir, "video_fire_station.gif"),
            "image": os.path.join(base_dir, "cctv_fire_station.jpg"),
            "status": "EMERGENCY READY",
            "status_color": "#005BAA",
            "activity_rank": 3,
            "fps": 15,
            "bitrate": "6.0 Mbps",
            "ai_features": ["Tender Ready Beacon", "Crew Muster Telemetry", "Dispatch Console Active"],
            "ai_summary": "Tender 01 & 04 armed and running. Emergency command console manned 24/7.",
            "thermal_temp": "24.1°C",
            "alert_badge": "DISPATCH READY"
        },
        {
            "id": "CAM-05",
            "name": "Welspun City Living Quarters - Aura Gardens",
            "zone": "Welspun City (Living Quarters)",
            "sector": "Residential Block C & Main Boulevard",
            "video": os.path.join(base_dir, "video_township_quarters.mp4"),
            "gif": os.path.join(base_dir, "video_township_quarters.gif"),
            "image": os.path.join(base_dir, "cctv_township_quarters.jpg"),
            "status": "NORMAL",
            "status_color": "#10B981",
            "activity_rank": 5,
            "fps": 15,
            "bitrate": "5.4 Mbps",
            "ai_features": ["Pedestrian Crosswalk Radar", "Speed Radar (Limit: 30 km/h)", "Night Perimeter Beam"],
            "ai_summary": "Normal residential movement. 5 pedestrians detected. Vehicle speed: 18 km/h (compliant).",
            "thermal_temp": "22.8°C",
            "alert_badge": "TOWNSHIP NORMAL"
        },
        {
            "id": "CAM-06",
            "name": "Pipe & Steel Mill Gantry Crane Zone",
            "zone": "Plant Core (Industrial)",
            "sector": "Sector 1 - Heavy Pipe Bay Alpha",
            "video": os.path.join(base_dir, "video_plant_mill.mp4"),
            "gif": os.path.join(base_dir, "video_plant_mill.gif"),
            "image": os.path.join(base_dir, "cctv_plant_spinning.jpg"),
            "status": "NORMAL",
            "status_color": "#10B981",
            "activity_rank": 6,
            "fps": 15,
            "bitrate": "4.5 Mbps",
            "ai_features": ["Overhead Crane Zone Clearance", "Suspended Load Proximity", "Worker Exclusions"],
            "ai_summary": "Gantry crane active. Red exclusion zone 100% clear of floor workers.",
            "thermal_temp": "29.1°C",
            "alert_badge": "ZONE NORMAL"
        },
        {
            "id": "CAM-07",
            "name": "Anjar Main Gate 1 & Weighbridge",
            "zone": "Logistics & Perimeter",
            "sector": "North Perimeter Gate",
            "video": os.path.join(base_dir, "video_perimeter_breach.mp4"),
            "gif": os.path.join(base_dir, "video_perimeter_breach.gif"),
            "image": os.path.join(base_dir, "cctv_perimeter_fence.jpg"),
            "status": "NORMAL",
            "status_color": "#10B981",
            "activity_rank": 7,
            "fps": 15,
            "bitrate": "5.0 Mbps",
            "ai_features": ["Automated Number Plate ANPR", "Cargo Hazmat Tag Reader", "Driver Facial Muster"],
            "ai_summary": "Trailer GJ-12-BV-9021 cleared at weighbridge. Zero unauthorized vehicles.",
            "thermal_temp": "25.2°C",
            "alert_badge": "GATE CLEAR"
        },
        {
            "id": "CAM-08",
            "name": "Welspun City Health Centre & Vidya Mandir",
            "zone": "Welspun City (Living Quarters)",
            "sector": "Community Campus Hub",
            "video": os.path.join(base_dir, "video_township_quarters.mp4"),
            "gif": os.path.join(base_dir, "video_township_quarters.gif"),
            "image": os.path.join(base_dir, "cctv_township_quarters.jpg"),
            "status": "OPTIMAL",
            "status_color": "#005BAA",
            "activity_rank": 8,
            "fps": 15,
            "bitrate": "4.1 Mbps",
            "ai_features": ["Child Safety Perimeter", "Ambulance Bay Keep-Clear", "Smoke Sensor Sync"],
            "ai_summary": "Ambulance emergency bay 100% unobstructed. School perimeter fence secure.",
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
                "name": "Station Alpha (Plant Industrial Hub)",
                "readiness": "100% OPERATIONAL",
                "crew_on_duty": 16,
                "coverage": "Pipe Mill, Textile Division, Steel Fabrication, Warehouses",
                "distance_to_core": "0.4 km"
            },
            {
                "id": "FS-02",
                "name": "Station Bravo (Welspun City Hub)",
                "readiness": "100% OPERATIONAL",
                "crew_on_duty": 10,
                "coverage": "Residential Township, School, Hospital, Commercial Plaza",
                "distance_to_core": "1.2 km"
            }
        ],
        "fleet": [
            {"id": "WF-01", "name": "Heavy Water Bowser (12,000L)", "station": "Station Alpha", "status": "Ready", "fuel": "98%", "foam_lvl": "100%"},
            {"id": "WF-02", "name": "Industrial Foam Crash Tender", "station": "Station Alpha", "status": "Ready", "fuel": "95%", "foam_lvl": "94%"},
            {"id": "WF-03", "name": "Hydraulic Sky-Lift & Rescue (32m)", "station": "Station Bravo", "status": "Ready", "fuel": "92%", "foam_lvl": "N/A"},
            {"id": "WF-04", "name": "Quick Response Vehicle (QRV)", "station": "Station Alpha", "status": "Dispatched (Sector 4)", "fuel": "88%", "foam_lvl": "100%"}
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
    """Returns active and recent safety/fire incidents in Anjar Plant & City."""
    from datetime import datetime, timedelta
    now = datetime.now()
    return [
        {
            "id": "ALM-9025",
            "time": (now - timedelta(minutes=1)).strftime("%H:%M:%S"),
            "location": "Sector 4 - West Substation Tripwire Line",
            "zone": "Plant Restricted Perimeter",
            "type": "🚷 Perimeter Crossing (Unauthorized Area Intrusion)",
            "severity": "CRITICAL",
            "details": "AI Camera CAM-04 detected unauthorized subject crossing virtual laser parameter boundary into high-voltage chemical yard.",
            "action_taken": "Security Quick Response Patrol dispatched; audible boundary warning siren triggered.",
            "status": "In Progress"
        },
        {
            "id": "ALM-9021",
            "time": (now - timedelta(minutes=5)).strftime("%H:%M:%S"),
            "location": "Sector 4 - Chemical Valve Hub HX-104",
            "zone": "Plant Core",
            "type": "🔥 Thermal Anomaly (Hot Spot >90°C)",
            "severity": "CRITICAL",
            "details": "FLIR camera detected surface temperature reaching 98.4°C on thermal oil line.",
            "action_taken": "QRV Unit WF-04 dispatched for thermal mitigation & isolation check.",
            "status": "In Progress"
        },
        {
            "id": "ALM-9018",
            "time": (now - timedelta(minutes=27)).strftime("%H:%M:%S"),
            "location": "Spinning Unit 2 - Lint Collection Filter",
            "zone": "Textile Plant",
            "type": "💨 Smoke Ionization Drift",
            "severity": "WARNING",
            "details": "Particulate density increased above baseline threshold. Auto-ventilation cycled.",
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
