import pandas as pd
from dash import Dash, html, dcc, Input, Output
import plotly.express as px

# Read cleaned data
df = pd.read_csv("formatted_output.csv")

# Clean data types
df["Date"] = pd.to_datetime(df["Date"])
df["Region"] = df["Region"].astype(str).str.lower().str.strip()

# Create app
app = Dash(__name__)
app.title = "Pink Morsel Sales Dashboard"

app.layout = html.Div(
    className="container",
    children=[
        html.H1("Pink Morsel Sales Dashboard", className="main-title"),

        html.P(
            "Explore Pink Morsel sales over time and filter by region.",
            className="subtitle"
        ),

        html.Div(
            className="radio-container",
            children=[
                html.Label("Select Region:", className="radio-label"),
                dcc.RadioItems(
                    id="region-filter",
                    options=[
                        {"label": "All", "value": "all"},
                        {"label": "North", "value": "north"},
                        {"label": "East", "value": "east"},
                        {"label": "South", "value": "south"},
                        {"label": "West", "value": "west"},
                    ],
                    value="all",
                    inline=True,
                    className="radio-items"
                ),
            ]
        ),

        dcc.Graph(id="sales-line-chart")
    ]
)

@app.callback(
    Output("sales-line-chart", "figure"),
    Input("region-filter", "value")
)
def update_chart(selected_region):
    if selected_region == "all":
        filtered_df = df.copy()
    else:
        filtered_df = df[df["Region"] == selected_region]

    daily_sales = (
        filtered_df.groupby("Date", as_index=False)["Sales"]
        .sum()
        .sort_values("Date")
    )

    fig = px.line(
        daily_sales,
        x="Date",
        y="Sales",
        title=f"Sales Over Time - {selected_region.capitalize()}"
    )

    fig.update_layout(
        xaxis_title="Date",
        yaxis_title="Sales",
        template="plotly_white"
    )

    return fig

if __name__ == "__main__":
    app.run(debug=True)