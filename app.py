import pandas as pd
from dash import Dash, html, dcc
import plotly.express as px

# Read cleaned data from Task 2
df = pd.read_csv("formatted_output.csv")

# Convert Date column to datetime
df["Date"] = pd.to_datetime(df["Date"])

# Group sales by date
daily_sales = df.groupby("Date", as_index=False)["Sales"].sum()

# Sort by date
daily_sales = daily_sales.sort_values("Date")

# Create line chart
fig = px.line(
    daily_sales,
    x="Date",
    y="Sales",
    title="Pink Morsel Sales Over Time"
)

fig.update_layout(
    xaxis_title="Date",
    yaxis_title="Sales"
)

# Build Dash app
app = Dash(__name__)

app.layout = html.Div(children=[
    html.H1("Pink Morsel Sales Visualizer"),
    dcc.Graph(
        id="sales-line-chart",
        figure=fig
    )
])

if __name__ == "__main__":
    app.run(debug=True)