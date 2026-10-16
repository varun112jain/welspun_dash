"""
Executive Summary & Boardroom Intelligence Data Service for Welspun City, Anjar
Consolidates high-level strategic telemetry across Heavy Industry (WCL, WDI, WLL),
Logistics Automation, Workforce Transit, Plant Safety, and Sustainability.
"""
from typing import Dict, List, Any

def get_executive_kpis() -> Dict[str, Dict[str, Any]]:
    """Returns top-level executive KPIs with delta trends and status."""
    return {
        "complex_output": {
            "title": "Daily Finished Production",
            "value": "18,450 MT",
            "target": "Target: 18,000 MT",
            "delta": "+2.5% vs Plan",
            "status": "optimal",
            "sub": "WCL Pipes • WDI Blast Furnace • WLL Spunlace"
        },
        "safe_man_hours": {
            "title": "Safety & LTI Streak",
            "value": "1,420 DAYS",
            "target": "18.4M Safe Hours",
            "delta": "Zero Fatalities / LTI",
            "status": "optimal",
            "sub": "ISO 45001 & British Safety Council 5-Star"
        },
        "logistics_automation": {
            "title": "Weighbridge Automation",
            "value": "99.4%",
            "target": "1,842 Trucks Handled",
            "delta": "100% Paperless MIGO",
            "status": "optimal",
            "sub": "Avg Gate Turnaround: 4.8 min (Target < 6 min)"
        },
        "sap_transacted_value": {
            "title": "Automated SAP Velocity",
            "value": "₹42.8 Cr",
            "target": "Daily Inbound/Outbound",
            "delta": "+12ms RFC Latency",
            "status": "optimal",
            "sub": "Direct SAP S/4HANA PO/MIGO Settlement"
        },
        "clean_energy_share": {
            "title": "Green Energy & Self-Reliance",
            "value": "100%",
            "target": "165 MW Total Generation",
            "delta": "14 MW Export to Grid",
            "status": "optimal",
            "sub": "123MW CPP + 42MW Rooftop & Ground Solar"
        },
        "ai_threat_prevention": {
            "title": "AI Autonomous Interceptions",
            "value": "148 Events",
            "target": "100% Mitigated",
            "delta": "Zero Asset Loss",
            "status": "optimal",
            "sub": "Perimeter • Thermal Hotspots • Driver Fatigue"
        }
    }

def get_executive_video_showcases() -> List[Dict[str, Any]]:
    """Returns 4 premier video streams highlighting key strategic operational zones."""
    return [
        {
            "id": "EXEC-01",
            "sector": "Heavy Metallurgy & Pipes",
            "title": "WCL LSAW & Spiral Pipe Manufacturing Mill",
            "camera_id": "CAM-06",
            "video": "assets/video_wcl_pipe_mill.mp4",
            "gif": "assets/video_wcl_pipe_mill.gif",
            "image": "assets/cctv_wcl_pipe_mill.jpg",
            "status": "● 100% OPERATIONAL",
            "kpi_label": "Mill Run Rate",
            "kpi_value": "42.5 Pipes / Hr",
            "telemetry": "Grade X70 API 5L High-Pressure Pipeline Coils",
            "strategic_impact": "Supplying critical national energy gas grid infrastructure."
        },
        {
            "id": "EXEC-02",
            "sector": "Primary Ironmaking & Casting",
            "title": "WDI 500k TPA Blast Furnace & DI Plant",
            "camera_id": "CAM-07",
            "video": "assets/video_wdi_blast_furnace.mp4",
            "gif": "assets/video_wdi_blast_furnace.gif",
            "image": "assets/cctv_blast_furnace.jpg",
            "status": "● NOMINAL TAPPING",
            "kpi_label": "Hot Metal Temp",
            "kpi_value": "1,485°C (Stable)",
            "telemetry": "Blast Volume 1,820 Nm³/min • Tuyere Pressure 2.4 Bar",
            "strategic_impact": "Direct feed to Ductile Iron (DI) water transmission pipes."
        },
        {
            "id": "EXEC-03",
            "sector": "Logistics & Autonomous Inbound",
            "title": "Unmanned Weighbridge Gate 1 (SAP S/4HANA)",
            "camera_id": "CAM-WB01",
            "video": "assets/video_unmanned_weighbridge.mp4",
            "gif": "assets/video_unmanned_weighbridge.gif",
            "image": "assets/cctv_unmanned_weighbridge.jpg",
            "status": "● ZERO SCALEMASTER",
            "kpi_label": "Cycle Clearance",
            "kpi_value": "142 Sec / Truck",
            "telemetry": "ANPR Plate Read • IR Deck Positioning • Auto-MIGO",
            "strategic_impact": "Zero gate congestion with multi-loadcell tamper prevention."
        },
        {
            "id": "EXEC-04",
            "sector": "Critical Infrastructure & Security",
            "title": "220kV Switchyard AI Perimeter Tripwire",
            "camera_id": "CAM-04",
            "video": "assets/video_perimeter_breach.mp4",
            "gif": "assets/video_perimeter_breach.gif",
            "image": "assets/cctv_perimeter_fence.jpg",
            "status": "⚠️ PATROL INTERCEPT",
            "kpi_label": "Threat Level",
            "kpi_value": "CONTAINED",
            "telemetry": "Thermal Optical AI • Target Tracking • Patrol Car #02 On-Scene",
            "strategic_impact": "Guarding the 220kV primary power feed to all manufacturing mills."
        }
    ]

def get_hourly_production_series() -> Dict[str, Any]:
    """Hourly production data across mills for Plotly charting."""
    hours = [f"{h:02d}:00" for h in range(6, 23)]
    wcl_pipes = [240, 260, 280, 275, 290, 285, 270, 295, 305, 310, 290, 285, 300, 315, 320, 310, 295]
    wdi_iron = [220, 235, 250, 245, 260, 255, 250, 265, 270, 275, 265, 260, 270, 280, 285, 275, 260]
    wll_textiles = [130, 140, 150, 145, 155, 150, 140, 160, 165, 170, 160, 155, 165, 170, 175, 165, 155]
    total_hourly = [a + b + c for a, b, c in zip(wcl_pipes, wdi_iron, wll_textiles)]
    target_hourly = [650] * len(hours)
    
    return {
        "hours": hours,
        "wcl_pipes": wcl_pipes,
        "wdi_iron": wdi_iron,
        "wll_textiles": wll_textiles,
        "total_hourly": total_hourly,
        "target_hourly": target_hourly
    }

def get_ai_prevention_breakdown() -> Dict[str, Any]:
    """Breakdown of autonomous AI security and safety preventions today."""
    return {
        "categories": [
            "Thermal Hotspot Pre-Ignition",
            "Perimeter Tripwire Crossings",
            "Driver Status / Fatigue Alerts",
            "Weighbridge Tare Discrepancies",
            "PPE & Red-Zone Exclusion Violations",
            "Unscheduled Equipment Vibration"
        ],
        "counts": [48, 32, 28, 22, 14, 4],
        "colors": ["#EF4444", "#F59E0B", "#005BAA", "#10B981", "#8B5CF6", "#06B6D4"]
    }

def get_energy_generation_mix() -> Dict[str, Any]:
    """Energy telemetry showing captive thermal + solar vs complex demand."""
    hours = [f"{h:02d}:00" for h in range(0, 24)]
    # Solar bell curve
    solar = [0, 0, 0, 0, 0, 0, 5, 14, 25, 36, 42, 42, 40, 35, 24, 12, 3, 0, 0, 0, 0, 0, 0, 0]
    cpp_thermal = [115, 115, 114, 114, 115, 115, 112, 105, 98, 92, 88, 88, 90, 95, 104, 110, 114, 115, 115, 116, 116, 115, 115, 115]
    demand = [110, 108, 106, 107, 112, 118, 122, 126, 130, 132, 134, 133, 131, 132, 130, 128, 126, 125, 124, 122, 120, 116, 114, 112]
    
    return {
        "hours": hours,
        "solar_mw": solar,
        "cpp_thermal_mw": cpp_thermal,
        "demand_mw": demand
    }
