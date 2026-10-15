"""
Interactive Spatial Map Component for Welspun Anjar Plant & City
"""
import plotly.graph_objects as go
from styles.welspun_theme import WELSPUN_COLORS

def render_anjar_spatial_map() -> go.Figure:
    """Renders a spatial layout map of Welspun Anjar Complex with networked fire stations and safety zones."""
    fig = go.Figure()
    
    # 1. Fire Hydrant High-Pressure Ring Network (Connecting loop)
    ring_x = [2.0, 4.5, 7.5, 8.5, 6.0, 3.0, 1.5, 2.0]
    ring_y = [2.0, 1.5, 3.0, 6.5, 8.0, 7.5, 4.5, 2.0]
    
    fig.add_trace(go.Scatter(
        x=ring_x, y=ring_y,
        mode="lines",
        name="Fire Hydrant High-Pressure Ring (8.6 Bar)",
        line=dict(color="#005BAA", width=4, dash="dot"),
        hoverinfo="text",
        text=["Dual-Loop Hydrant Line - 8.6 Bar"] * len(ring_x)
    ))
    
    # 2. Industrial Plant Sectors
    plant_nodes = [
        {"name": "Sector 1: Welspun Pipe & Steel Mill", "x": 2.5, "y": 2.5, "type": "Industrial Plant", "status": "Normal", "cameras": 310, "temp": "27°C"},
        {"name": "Sector 2: Welspun Textile & Spunlace", "x": 4.5, "y": 3.0, "type": "Industrial Plant", "status": "Normal", "cameras": 420, "temp": "28°C"},
        {"name": "Sector 3: Advanced Flooring Unit", "x": 6.8, "y": 3.5, "type": "Industrial Plant", "status": "Normal", "cameras": 190, "temp": "26°C"},
        {"name": "Sector 4: Chemical & Thermal Utility Hub", "x": 3.5, "y": 4.2, "type": "Critical Utility", "status": "🔥 THERMAL ALERT", "cameras": 85, "temp": "98.4°C"}
    ]
    
    px_coords = [n["x"] for n in plant_nodes]
    py_coords = [n["y"] for n in plant_nodes]
    p_text = [
        f"<b>{n['name']}</b><br>Type: {n['type']}<br>Status: {n['status']}<br>Cameras: {n['cameras']}<br>Temp: {n['temp']}"
        for n in plant_nodes
    ]
    p_colors = ["#EF4444" if "ALERT" in n["status"] else "#005BAA" for n in plant_nodes]
    
    fig.add_trace(go.Scatter(
        x=px_coords, y=py_coords,
        mode="markers+text",
        name="Plant Manufacturing Sectors",
        text=["Pipe Mill", "Textile Mill", "Flooring Hub", "Sector 4 (Alert)"],
        textposition="bottom center",
        marker=dict(size=[18, 18, 16, 22], color=p_colors, symbol="square", line=dict(color="#FFFFFF", width=2)),
        hoverinfo="text",
        hovertext=p_text
    ))
    
    # 3. Welspun City Township (Township Quarters)
    city_nodes = [
        {"name": "Welspun City: Residential Quarters (Aura Gardens)", "x": 6.5, "y": 7.0, "type": "Township Quarters", "status": "Normal", "cameras": 140},
        {"name": "Welspun City: Senior & Staff Hostels", "x": 8.0, "y": 6.2, "type": "Township Quarters", "status": "Normal", "cameras": 95},
        {"name": "Welspun City: Multi-Speciality Health Centre", "x": 5.2, "y": 7.5, "type": "Community / Hospital", "status": "Optimal", "cameras": 45},
        {"name": "Welspun Vidya Mandir School Campus", "x": 7.2, "y": 8.2, "type": "Community / School", "status": "Optimal", "cameras": 60}
    ]
    
    cx_coords = [n["x"] for n in city_nodes]
    cy_coords = [n["y"] for n in city_nodes]
    c_text = [
        f"<b>{n['name']}</b><br>Zone: {n['type']}<br>Status: {n['status']}<br>CCTV Coverage: {n['cameras']} Feeds"
        for n in city_nodes
    ]
    
    fig.add_trace(go.Scatter(
        x=cx_coords, y=cy_coords,
        mode="markers+text",
        name="Welspun City (Township Quarters)",
        text=["Residential Quarters", "Staff Hostels", "Health Centre", "School"],
        textposition="top center",
        marker=dict(size=16, color="#00A6E6", symbol="circle", line=dict(color="#FFFFFF", width=2)),
        hoverinfo="text",
        hovertext=c_text
    ))
    
    # 4. Networked Fire Stations (Station Alpha & Station Bravo)
    fs_nodes = [
        {"name": "Fire Station Alpha (Plant Core)", "x": 3.8, "y": 2.2, "tenders": 3, "crew": 16, "status": "Active / QRV Dispatched"},
        {"name": "Fire Station Bravo (Welspun City Hub)", "x": 6.2, "y": 6.5, "tenders": 2, "crew": 10, "status": "Ready Standby"}
    ]
    
    fs_x = [n["x"] for n in fs_nodes]
    fs_y = [n["y"] for n in fs_nodes]
    fs_text = [
        f"<b>{n['name']}</b><br>Ready Tenders: {n['tenders']}<br>Crew On Duty: {n['crew']}<br>Status: {n['status']}"
        for n in fs_nodes
    ]
    
    fig.add_trace(go.Scatter(
        x=fs_x, y=fs_y,
        mode="markers+text",
        name="Networked Fire Stations",
        text=["🚒 Station Alpha (Plant)", "🚒 Station Bravo (City)"],
        textposition="bottom right",
        marker=dict(size=22, color="#EF4444", symbol="star", line=dict(color="#FED7AA", width=2)),
        hoverinfo="text",
        hovertext=fs_text
    ))
    
    # Styling layout
    fig.update_layout(
        title={
            "text": "Anjar Plant & Welspun City Surveillance & Emergency Topology",
            "font": {"size": 15, "color": WELSPUN_COLORS["deep_navy"], "weight": 700}
        },
        height=380,
        margin=dict(l=10, r=10, t=40, b=10),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="#F1F5F9",
        xaxis=dict(showgrid=True, gridcolor="#E2E8F0", zeroline=False, showticklabels=False),
        yaxis=dict(showgrid=True, gridcolor="#E2E8F0", zeroline=False, showticklabels=False),
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="center",
            x=0.5,
            bgcolor="rgba(255,255,255,0.85)"
        )
    )
    return fig
