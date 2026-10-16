"""
Employee Transit, Commuter Bus Fleet, and Dashcam Telemetry Data
Models the commuter bus network carrying employees to and from Welspun City Township, Anjar, Gandhidham, and Adipur.
Includes live Dashcam cabin feeds, RFID tap-in counters, shift sync, and Driver Status Monitoring (DSM).
"""
import os
from datetime import datetime, timedelta

def get_bus_transit_kpis():
    """Returns executive KPIs for the employee commuter bus transit network."""
    return {
        "active_fleet": {"value": "12 / 12 Buses", "sub": "100% Operational Readiness", "status": "optimal"},
        "commuters_today": {"value": "3,840 Employees", "sub": "Shift A, B & General Shift", "status": "optimal"},
        "on_time_departure": {"value": "98.6% On-Time", "sub": "Avg Delay: 1.2 Mins", "status": "optimal"},
        "driver_alertness": {"value": "99.4% Alert", "sub": "AI DSM Active • Zero Drowsiness", "status": "optimal"},
        "seat_occupancy": {"value": "89.2% Avg", "sub": "Optimized Route Allocation", "status": "optimal"},
        "safety_index": {"value": "Zero Violations", "sub": "Speed Governor Locked (50 km/h)", "status": "optimal"}
    }

def get_bus_transit_feeds():
    """Returns CCTV and Dashcam video feeds for employee transit & bus fleet."""
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "assets"))
    return [
        {
            "id": "CAM-BUS01",
            "name": "Welspun Shuttle & Employee Transit Terminal (Bays 1 - 4)",
            "zone": "Employee Transit Hub - Central Terminal",
            "sector": "Bus Staging & Turnstile Passenger Boarding Bays",
            "video": os.path.join(base_dir, "video_employee_bus_fleet.mp4"),
            "gif": os.path.join(base_dir, "video_employee_bus_fleet.gif"),
            "image": os.path.join(base_dir, "cctv_employee_bus_fleet.jpg"),
            "status": "BOARDING DISPATCH ACTIVE",
            "status_color": "#005BAA",
            "activity_rank": 1,
            "fps": 12,
            "bitrate": "4.8 Mbps",
            "ai_features": ["RFID Turnstile Gate Tap", "AI Queue Headcount", "Digital Departure LED Sync", "Shift Rostering AI"],
            "ai_summary": "Bay 2 (Anjar City Express) boarding active: 38/42 seats filled. Average contactless tap speed: 0.8 seconds. On-time departure countdown: 3 mins.",
            "thermal_temp": "23.5°C",
            "alert_badge": "BOARDING: BAY 2 (ANJAR CITY)"
        },
        {
            "id": "CAM-BUS02",
            "name": "Commuter Bus WB-04: Forward Dashcam & Passenger Cabin View",
            "zone": "Expressway Transit Corridor (Anjar - Welspun City)",
            "sector": "Bus WB-04 In-Cabin & Forward Road Perspective",
            "video": os.path.join(base_dir, "video_bus_cabin_dashcam.mp4"),
            "gif": os.path.join(base_dir, "video_bus_cabin_dashcam.gif"),
            "image": os.path.join(base_dir, "cctv_bus_dashcam.jpg"),
            "status": "TRANSIT CRUISE OPTIMAL",
            "status_color": "#10B981",
            "activity_rank": 2,
            "fps": 12,
            "bitrate": "4.6 Mbps",
            "ai_features": ["Driver Status Monitor (DSM)", "Lane Keeping Assist", "Cabin Seat Occupancy AI", "GPS Speed Governor (50 km/h)"],
            "ai_summary": "Cruising at 42.4 km/h towards Welspun City Township (7.4 km remaining). Driver alertness 99.4% (Zero fatigue/drowsiness). Cabin occupancy 38/42 seats.",
            "thermal_temp": "22.6°C Ambient",
            "alert_badge": "DSM: 100% ATTENTIVE • 42 KM/H"
        }
    ]

def get_commuter_bus_roster():
    """Returns active roster of employee buses with live routes, drivers, and occupancy."""
    return [
        {
            "bus_id": "WB-01",
            "route_name": "Township Shuttle (Aura Gardens & Hostels)",
            "driver": "Ramesh Solanki",
            "shift": "Shift B (14:00 - 22:00)",
            "capacity": 42,
            "occupied": 41,
            "speed_kmh": 38.5,
            "status": "In Transit",
            "dsm_status": "Optimal (100% Alert)",
            "eta_mins": 4,
            "destination": "Township Quarters Gate"
        },
        {
            "bus_id": "WB-02",
            "route_name": "Anjar City Express (Ganga Naka & Devaliya)",
            "driver": "Hitesh Patel",
            "shift": "General Shift Departure",
            "capacity": 45,
            "occupied": 38,
            "speed_kmh": 0.0,
            "status": "Boarding (Bay 2)",
            "dsm_status": "Ready Standby",
            "eta_mins": 25,
            "destination": "Anjar Bus Station"
        },
        {
            "bus_id": "WB-03",
            "route_name": "Gandhidham Junction Express (Sectors 1-5)",
            "driver": "Mukesh Jadeja",
            "shift": "Shift B (14:00 - 22:00)",
            "capacity": 45,
            "occupied": 44,
            "speed_kmh": 44.0,
            "status": "In Transit",
            "dsm_status": "Optimal (99% Alert)",
            "eta_mins": 18,
            "destination": "Gandhidham Rotary Circle"
        },
        {
            "bus_id": "WB-04",
            "route_name": "Township Shuttle (Staff Hostels & Vidya Mandir)",
            "driver": "Dilip Varma",
            "shift": "General Shift Departure",
            "capacity": 42,
            "occupied": 38,
            "speed_kmh": 42.4,
            "status": "In Transit (Dashcam Active)",
            "dsm_status": "Optimal (100% Alert)",
            "eta_mins": 8,
            "destination": "Welspun City Township"
        },
        {
            "bus_id": "WB-05",
            "route_name": "Adipur City Corridor (Maitri Mandal & Shinay)",
            "driver": "Kailash Giri",
            "shift": "Shift B (14:00 - 22:00)",
            "capacity": 45,
            "occupied": 42,
            "speed_kmh": 41.2,
            "status": "In Transit",
            "dsm_status": "Optimal (98% Alert)",
            "eta_mins": 22,
            "destination": "Adipur Railway Colony"
        },
        {
            "bus_id": "WB-06",
            "route_name": "WCL Pipe Mills & WDI Metallurgical Hub Intra-Plant Shuttle",
            "driver": "Chetan Sharma",
            "shift": "Continuous Loop",
            "capacity": 32,
            "occupied": 24,
            "speed_kmh": 22.0,
            "status": "Internal Loop",
            "dsm_status": "Optimal (100% Alert)",
            "eta_mins": 5,
            "destination": "Blast Furnace Tap Gate"
        },
        {
            "bus_id": "WB-07",
            "route_name": "WLL Textiles & 123MW Energy Campus Shuttle",
            "driver": "Pravin Rawat",
            "shift": "Continuous Loop",
            "capacity": 32,
            "occupied": 28,
            "speed_kmh": 24.5,
            "status": "Internal Loop",
            "dsm_status": "Optimal (100% Alert)",
            "eta_mins": 3,
            "destination": "Spunlace Plant Gate"
        },
        {
            "bus_id": "WB-08",
            "route_name": "Welspun Vidya Mandir School & Campus Bus",
            "driver": "Suresh Rathod",
            "shift": "School Day Shift",
            "capacity": 42,
            "occupied": 0,
            "speed_kmh": 0.0,
            "status": "Staged (Bay 4)",
            "dsm_status": "Ready Standby",
            "eta_mins": 45,
            "destination": "Vidya Mandir Campus"
        }
    ]

def get_shift_schedule():
    """Returns shift schedule and bus transit timetable."""
    return [
        {"shift": "Shift A (Morning)", "timing": "06:00 - 14:00", "buses": 10, "workers_moved": 1420, "on_time_pct": "99.1%"},
        {"shift": "General Shift (Corporate)", "timing": "08:30 - 17:30", "buses": 8, "workers_moved": 860, "on_time_pct": "98.8%"},
        {"shift": "Shift B (Evening)", "timing": "14:00 - 22:00", "buses": 10, "workers_moved": 1180, "on_time_pct": "98.4%"},
        {"shift": "Shift C (Night)", "timing": "22:00 - 06:00", "buses": 6, "workers_moved": 380, "on_time_pct": "99.5%"}
    ]
