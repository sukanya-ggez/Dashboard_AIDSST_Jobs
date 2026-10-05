import dash
from dash import dcc, html, Input, Output
import dash_bootstrap_components as dbc

import duckdb
import pandas as pd
import plotly.express as px

# Connect to DuckDB
DB_PATH = "data/processed/dashboard.duckdb"
def get_db_connection():
    import os
    if os.path.exists(DB_PATH):
        return duckdb.connect(DB_PATH, read_only=True)
    return None

# Initialize the Dash app with a Bootstrap theme
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.FLATLY])
app.title = "AI/DS/Stats Dashboard"

# Define the layout
app.layout = dbc.Container([
    dbc.Row([
        dbc.Col(html.H1("Dashboard: AI / Data Science / Statistics", className="text-center mb-4 mt-4"), width=12)
    ]),
    
    # Global Filters placeholder
    dbc.Row([
        dbc.Col(
            dbc.Card([
                dbc.CardHeader("Global Filters"),
                dbc.CardBody([
                    dbc.Row([
                        dbc.Col([
                            html.Label("Domain"),
                            dcc.Dropdown(id="filter-domain", options=["AI", "DS", "STAT"], multi=True, placeholder="Select Domain")
                        ], width=4),
                        dbc.Col([
                            html.Label("Year"),
                            dcc.Dropdown(id="filter-year", options=[2022, 2023, 2024, 2025], multi=True, placeholder="Select Year")
                        ], width=4)
                    ])
                ])
            ]),
            width=12, className="mb-4"
        )
    ]),
    
    # Tabs
    dbc.Tabs([
        dbc.Tab(label="Graduate Supply", tab_id="tab-1"),
        dbc.Tab(label="Job Demand", tab_id="tab-2"),
        dbc.Tab(label="Skills Mismatch", tab_id="tab-3"),
    ], id="tabs", active_tab="tab-1"),
    
    # Tab content placeholder
    html.Div(id="tab-content", className="p-4 border-start border-end border-bottom")
], fluid=True)

# Callback to render tab content
@app.callback(
    Output("tab-content", "children"),
    Input("tabs", "active_tab"),
    Input("filter-domain", "value"),
    Input("filter-year", "value")
)
def render_tab_content(active_tab, domains, years):
    conn = get_db_connection()
    if not conn:
        return html.Div([
            html.H3("Database not found!"),
            html.P("Please run src/data_pipeline.py first to generate data.")
        ])
    
    domain_filter = ""
    if domains:
        domain_list = "','".join(domains)
        domain_filter = f" WHERE domain IN ('{domain_list}')"
        
    if active_tab == "tab-1":
        # Fetch supply data
        query = f"SELECT year, domain, sum(graduates) as total_graduates FROM graduate_supply {domain_filter} GROUP BY year, domain ORDER BY year"
        df = conn.execute(query).df()
        
        fig = px.bar(df, x="year", y="total_graduates", color="domain", barmode="group", title="Total Graduates by Domain & Year")
        
        return html.Div([
            html.H3("Graduate Supply & Curriculum Skills"),
            dcc.Graph(figure=fig)
        ])
        
    elif active_tab == "tab-2":
        # Fetch demand data
        query = f"SELECT year, domain, sum(employment) as total_employment FROM job_demand {domain_filter} GROUP BY year, domain ORDER BY year"
        df = conn.execute(query).df()
        
        fig = px.line(df, x="year", y="total_employment", color="domain", title="Job Employment by Domain & Year")
        
        return html.Div([
            html.H3("Job Demand & Required Skills"),
            dcc.Graph(figure=fig)
        ])
        
    elif active_tab == "tab-3":
        return html.Div([
            html.H3("Skills Mismatch Analysis"),
            html.P("Analysis comparing Supply and Demand will be displayed here.")
        ])
    return html.P("This shouldn't ever be displayed...")

if __name__ == "__main__":
    app.run_server(debug=True)
