"""
Logistics, Truck Entry/Exit, Unmanned Weighbridge, and SAP S/4HANA Telemetry Data
Models automated truck check-in, manless weighbridge load cells, ANPR, and real-time SAP ERP MIGO/PGI sync.
"""
import os
from datetime import datetime, timedelta

def get_weighbridge_kpis():
    """Returns top-level KPIs for plant logistics gates and unmanned weighbridges."""
    return {
        "trucks_today": {"value": "248 Trucks", "sub": "164 Inbound • 84 Outbound", "status": "optimal"},
        "unmanned_pct": {"value": "100% Manless", "sub": "Zero Manual Scale Operators", "status": "optimal"},
        "avg_turnaround_min": {"value": "4.2 Mins", "sub": "Reduced from 18.5m manual", "status": "optimal"},
        "active_weighbridges": {"value": "3 / 3 Online", "sub": "Gate 1, Gate 3, Gate 6", "status": "optimal"}
    }

def get_weighbridge_feeds():
    """Returns the dedicated CCTV and Dashcam video feeds for logistics & weighbridge."""
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "assets"))
    return [
        {
            "id": "CAM-WB01",
            "name": "Gate 1 Unmanned Automated Weighbridge (Steel Coils & Heavy Pipes)",
            "zone": "Logistics Gate 1 - Heavy Inbound / Outbound",
            "sector": "Weighbridge Platform 1 (100 Metric Ton Capacity)",
            "video": os.path.join(base_dir, "video_unmanned_weighbridge.mp4"),
            "gif": os.path.join(base_dir, "video_unmanned_weighbridge.gif"),
            "image": os.path.join(base_dir, "cctv_unmanned_weighbridge.jpg"),
            "status": "UNMANNED AUTOMATION ACTIVE",
            "status_color": "#10B981",
            "activity_rank": 1,
            "fps": 12,
            "bitrate": "4.5 Mbps",
            "ai_features": ["ANPR License Plate Lock", "Digital Load Cell Auto-Capture", "SAP S/4HANA MIGO Sync", "IR Anti-Overhang Radar"],
            "ai_summary": "Scania Multi-Axle (GJ-12-BW-9842) positioned 100% on platform. Gross Weight: 42,850 kg stabilized. SAP PO #450098231 verified. Automated boom barrier lifted.",
            "thermal_temp": "23.8°C",
            "alert_badge": "WEIGHMENT COMPLETE • BOOM OPEN"
        },
        {
            "id": "CAM-DC01",
            "name": "Heavy Trailer Inbound Dashcam & Undercarriage Scanner",
            "zone": "Logistics Gate 1 Approach Lane",
            "sector": "Driver Cabin Perspective & UVIS Inspection",
            "video": os.path.join(base_dir, "video_truck_dashcam.mp4"),
            "gif": os.path.join(base_dir, "video_truck_dashcam.gif"),
            "image": os.path.join(base_dir, "cctv_truck_dashcam.jpg"),
            "status": "DASHCAM TELEMETRY ONLINE",
            "status_color": "#005BAA",
            "activity_rank": 2,
            "fps": 12,
            "bitrate": "4.2 Mbps",
            "ai_features": ["Forward Collision Radar", "RFID FASTag Gateway", "GPS Geofenced Entry", "Driver Face Validation"],
            "ai_summary": "Inbound truck approaching Gate 1 at 8 km/h. FASTag RFID detected. Automatic gate clearance token #TK-8842 issued. Driver verified via face match.",
            "thermal_temp": "24.2°C",
            "alert_badge": "GATE PASS #GP-8842 VALID"
        }
    ]

def get_current_weighment_state():
    """Returns active weighment load cell telemetry for the live platform display."""
    return {
        "weighbridge_id": "WB-01 (Gate 1 Heavy Logistics)",
        "truck_plate": "GJ-12-BW-9842",
        "transporter": "Welspun Logistics & Freight Corp",
        "material": "Hot Rolled Steel Coils (Grade X70 for LSAW Pipe Mill)",
        "gross_weight_kg": 42850,
        "tare_weight_kg": 14220,
        "net_weight_kg": 28630,
        "sap_po_number": "450098231",
        "sap_vendor_code": "V-100482 (Tata Steel / JSW Steel)",
        "sap_migo_doc": "5002918491",
        "weight_slip_no": "WS-2026-10492",
        "positioning_sensors": {
            "front_ir_beam": "ALIGNED (NO OVERHANG)",
            "rear_ir_beam": "ALIGNED (CLEAR)",
            "side_guidance_radar": "OPTIMAL (CENTERED)",
            "all_wheels_on_deck": True
        },
        "load_cells": [
            {"cell_id": "LC-1 (Front Left)", "weight_kg": 7140, "status": "Normal"},
            {"cell_id": "LC-2 (Front Right)", "weight_kg": 7150, "status": "Normal"},
            {"cell_id": "LC-3 (Mid Left)", "weight_kg": 7135, "status": "Normal"},
            {"cell_id": "LC-4 (Mid Right)", "weight_kg": 7145, "status": "Normal"},
            {"cell_id": "LC-5 (Rear Left)", "weight_kg": 7138, "status": "Normal"},
            {"cell_id": "LC-6 (Rear Right)", "weight_kg": 7142, "status": "Normal"}
        ],
        "boom_barrier_state": "OPEN (AUTOMATED CLEARANCE)",
        "traffic_light": "GREEN",
        "sap_sync_status": "COMMITTED TO SAP S/4HANA (RFC 200 OK)",
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

def get_logistics_truck_log():
    """Returns chronological log of today's truck entries, weighments, and SAP postings."""
    now = datetime.now()
    return [
        {
            "time": (now - timedelta(minutes=2)).strftime("%H:%M:%S"),
            "truck_no": "GJ-12-BW-9842",
            "type": "Inbound (Raw Material)",
            "material": "Hot Rolled Coils (API 5L X70)",
            "gate": "Gate 1 (WB-01)",
            "gross_kg": 42850,
            "tare_kg": 14220,
            "net_kg": 28630,
            "sap_po_so": "PO #450098231",
            "sap_doc": "MIGO #5002918491",
            "weight_slip": "WS-10492",
            "status": "Weighed & Posted"
        },
        {
            "time": (now - timedelta(minutes=14)).strftime("%H:%M:%S"),
            "truck_no": "GJ-12-AU-4512",
            "type": "Outbound (Finished Goods)",
            "material": "56\" LSAW Submerged Arc Pipes",
            "gate": "Gate 1 (WB-01)",
            "gross_kg": 38400,
            "tare_kg": 13950,
            "net_kg": 24450,
            "sap_po_so": "SO #700148293",
            "sap_doc": "PGI #800194820",
            "weight_slip": "WS-10491",
            "status": "Dispatched"
        },
        {
            "time": (now - timedelta(minutes=28)).strftime("%H:%M:%S"),
            "truck_no": "GJ-12-Z-7719",
            "type": "Inbound (Raw Material)",
            "material": "Scrap & Sponge Iron for WDI BF",
            "gate": "Gate 3 (WB-02)",
            "gross_kg": 45120,
            "tare_kg": 15100,
            "net_kg": 30020,
            "sap_po_so": "PO #450098190",
            "sap_doc": "MIGO #5002918480",
            "weight_slip": "WS-10490",
            "status": "Weighed & Posted"
        },
        {
            "time": (now - timedelta(minutes=42)).strftime("%H:%M:%S"),
            "truck_no": "MH-04-EB-3104",
            "type": "Outbound (Finished Goods)",
            "material": "DN 600 Ductile Iron (DI) Pipes",
            "gate": "Gate 3 (WB-02)",
            "gross_kg": 36900,
            "tare_kg": 14200,
            "net_kg": 22700,
            "sap_po_so": "SO #700148255",
            "sap_doc": "PGI #800194812",
            "weight_slip": "WS-10489",
            "status": "Dispatched"
        },
        {
            "time": (now - timedelta(minutes=58)).strftime("%H:%M:%S"),
            "truck_no": "GJ-01-CX-8890",
            "type": "Inbound (Raw Material)",
            "material": "Organic Cotton Bales for WLL Textiles",
            "gate": "Gate 6 (WB-03)",
            "gross_kg": 26800,
            "tare_kg": 11400,
            "net_kg": 15400,
            "sap_po_so": "PO #450098144",
            "sap_doc": "MIGO #5002918465",
            "weight_slip": "WS-10488",
            "status": "Weighed & Posted"
        },
        {
            "time": (now - timedelta(hours=1, minutes=15)).strftime("%H:%M:%S"),
            "truck_no": "GJ-12-Y-5532",
            "type": "Outbound (Finished Goods)",
            "material": "Welspun Living Terry Towels (Export)",
            "gate": "Gate 6 (WB-03)",
            "gross_kg": 28450,
            "tare_kg": 12100,
            "net_kg": 16350,
            "sap_po_so": "SO #700148210",
            "sap_doc": "PGI #800194801",
            "weight_slip": "WS-10487",
            "status": "Dispatched"
        }
    ]
