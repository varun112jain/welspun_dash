"""
Synthetic Data Generator for Welspun Dashboard Templates
"""
import numpy as np
import pandas as pd
from datetime import datetime, timedelta

def get_kpi_summary_data():
    """Returns top-level executive KPI numbers."""
    return {
        "production_volume": {"value": "248.5K MT", "delta": "+8.4%", "positive": True, "label": "Production Output"},
        "capacity_utilization": {"value": "91.2%", "delta": "+2.8%", "positive": True, "label": "Plant Capacity"},
        "quality_yield": {"value": "98.7%", "delta": "+0.6%", "positive": True, "label": "First Pass Yield"},
        "on_time_delivery": {"value": "96.4%", "delta": "-1.1%", "positive": False, "label": "OTIF Delivery"},
        "energy_efficiency": {"value": "412 kWh/T", "delta": "-5.2%", "positive": True, "label": "Specific Power Cons."}
    }

def get_timeseries_performance(days: int = 30):
    """Generates multi-variable daily operational time-series data."""
    np.random.seed(42)
    end_date = datetime.today()
    dates = [end_date - timedelta(days=i) for i in range(days)][::-1]
    
    trend = np.linspace(100, 130, days)
    noise_prod = np.random.normal(0, 5, days)
    noise_yield = np.random.normal(0, 0.4, days)
    
    df = pd.DataFrame({
        "Date": dates,
        "Production_Output_MT": np.round(trend * 25 + noise_prod * 15, 1),
        "Target_MT": np.round(trend * 25 + 50, 1),
        "Yield_Pct": np.clip(np.round(98.2 + noise_yield, 2), 95.0, 100.0),
        "Defect_Rate_PPM": np.random.randint(120, 280, days),
        "Energy_Intensity_MWh": np.round(trend * 1.8 + np.random.normal(0, 3, days), 2)
    })
    return df

def get_division_breakdown():
    """Generates synthetic breakdown across key Welspun businesses."""
    divisions = [
        {"Division": "Welspun Corp (Pipes & Steel)", "Revenue_Cr": 1240, "Volume_MT": 94500, "Plants": 6, "Efficiency": 93.4},
        {"Division": "Welspun Advanced Textiles & Home", "Revenue_Cr": 980, "Volume_MT": 68000, "Plants": 4, "Efficiency": 91.8},
        {"Division": "Welspun Enterprises (Infra)", "Revenue_Cr": 720, "Volume_MT": 45000, "Plants": 3, "Efficiency": 89.6},
        {"Division": "Welspun Flooring", "Revenue_Cr": 390, "Volume_MT": 24000, "Plants": 2, "Efficiency": 94.1},
        {"Division": "Welspun New Energy", "Revenue_Cr": 280, "Volume_MT": 16500, "Plants": 2, "Efficiency": 96.0}
    ]
    return pd.DataFrame(divisions)

def get_plant_locations_data():
    """Synthetic operational status across key Welspun manufacturing hubs."""
    plants = [
        {"Plant": "Anjar Mega Facility (Gujarat)", "State": "Gujarat", "Status": "Optimal", "Capacity": 94.2, "Yield": 99.1, "Alerts": 0},
        {"Plant": "Vapi Industrial Complex", "State": "Gujarat", "Status": "Optimal", "Capacity": 92.0, "Yield": 98.4, "Alerts": 1},
        {"Plant": "Bhopal Flooring & Steel Hub", "State": "Madhya Pradesh", "Status": "Normal", "Capacity": 88.5, "Yield": 97.9, "Alerts": 2},
        {"Plant": "Mandya High-Tech Unit", "State": "Karnataka", "Status": "Optimal", "Capacity": 93.1, "Yield": 98.8, "Alerts": 0},
        {"Plant": "Little Rock (USA Tubular Facility)", "State": "Arkansas (US)", "Status": "Optimal", "Capacity": 90.6, "Yield": 98.2, "Alerts": 1},
        {"Plant": "Dammam GCC Facility", "State": "Saudi Arabia", "Status": "Maintenance", "Capacity": 76.4, "Yield": 96.5, "Alerts": 3}
    ]
    return pd.DataFrame(plants)
