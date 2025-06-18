import plotly.graph_objects as go
import plotly.io as pio

# Define a custom Plotly template (branding style)
pio.templates["custom_dark"] = go.layout.Template(
    layout=go.Layout(
        font=dict(family="Arial", size=14, color="#EAEAEA"),
        paper_bgcolor="#0F1C2E",
        plot_bgcolor="#0F1C2E",
        xaxis=dict(
            showgrid=True, gridcolor="#2A3F5F",
            linecolor="#2A3F5F", zeroline=False
        ),
        yaxis=dict(
            showgrid=True, gridcolor="#2A3F5F",
            linecolor="#2A3F5F", zeroline=False
        ),
        margin=dict(l=60, r=30, t=60, b=50),
        colorway=["#3DD6D0", "#FF6B6B", "#FFA07A", "#A9A9F5"]
    )
)

# Set this template as default
pio.templates.default = "custom_dark"

# A helper to plot time series with branded defaults
def plot_time_series(df, columns, title="", yaxis_title="Value"):
    fig = go.Figure()

    for col in columns:
        fig.add_trace(go.Scatter(
            x=df.index,
            y=df[col],
            mode='lines',
            name=col,
            line=dict(width=3)
        ))

    fig.update_layout(
        title=dict(text=title, x=0.5),
        yaxis_title=yaxis_title,
        hovermode="x unified"
    )

    return fig
