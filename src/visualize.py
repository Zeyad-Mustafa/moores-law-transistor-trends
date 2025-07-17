import pandas as pd
import plotly.graph_objects as go

def plot_interactive(df):
    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=df["Year"],
        y=df["Transistor Size (nm)"],
        mode="lines+markers",
        name="Transistor Size",
        line=dict(color="royalblue", dash="dash"),
        marker=dict(size=8)
    ))

    fig.update_layout(
        title="Transistor Size Shrinking Over Time (Moore's Law)",
        xaxis_title="Year",
        yaxis_title="Transistor Size (nm)",
        yaxis_type="log",
        template="plotly_white",
        hovermode="x unified",
        sliders=[{
            "steps": [{
                "method": "restyle",
                "label": str(year),
                "args": ["transforms[0].value", year]
            } for year in df["Year"]]
        }]
    )

    fig.show()
