import dash
from dash import dcc, html, Input, Output
import dash_bootstrap_components as dbc
import plotly.graph_objects as go
import pandas as pd
import duckdb
import os

DB_PATH = "data/processed/dashboard.duckdb"

def get_db_connection():
    if os.path.exists(DB_PATH):
        return duckdb.connect(DB_PATH, read_only=True)
    return None

# Initialize App
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP], suppress_callback_exceptions=True)
app.title = "AI/DS/Stats Dashboard"

# ----------------- UI COMPONENTS -----------------

sidebar = html.Div([
    html.Div([
        html.H4("Antigravity", className="serif-text", style={"fontWeight": "bold", "marginBottom": "2rem"})
    ]),
    html.Div([
        # User profile mock
        html.Div(style={"width": "60px", "height": "60px", "borderRadius": "50%", "background": "#ff9e80", "margin": "0 auto"}),
        html.H5("User Profile", className="text-center mt-3 serif-text", style={"fontWeight": "bold"}),
        html.P("Project Lead", className="text-center text-muted", style={"fontSize": "0.8rem"})
    ], className="mb-5"),
    
    html.Div([
        html.A("Graduate Supply", href="#", className="nav-link active"),
        html.A("Job Demand", href="#", className="nav-link"),
        html.A("Skills Mismatch", href="#", className="nav-link"),
    ])
], className="sidebar")

def create_kpi_card(title, value, color="#4caf50"):
    return html.Div([
        html.P(title, className="kpi-title"),
        html.H4(value, className="kpi-value")
    ], style={"flex": "1"})

def create_empty_state():
    return html.Div([
        html.H3("Database not found", className="serif-text"),
        html.P("Please run data ingestion pipeline (Real Data Edition) to populate the charts.")
    ], className="custom-card text-center py-5")

# ----------------- LAYOUT -----------------

app.layout = html.Div([
    sidebar,
    html.Div([
        # Header Row
        dbc.Row([
            dbc.Col([
                html.H1("Dashboard", className="serif-text", style={"fontWeight": "bold", "fontSize": "2.5rem"}),
            ], width=8),
            dbc.Col([
                dcc.Dropdown(id="filter-domain", options=["AI", "DS", "STAT"], placeholder="Select Domain", style={"borderRadius": "10px"})
            ], width=4)
        ], className="mb-4 align-items-center"),
        
        html.Div(id="main-dashboard-content")
        
    ], className="main-content")
], className="dashboard-container")


# ----------------- CALLBACKS -----------------

@app.callback(
    Output("main-dashboard-content", "children"),
    Input("filter-domain", "value")
)
def update_dashboard(domain_filter):
    conn = get_db_connection()
    if not conn:
        return create_empty_state()
    
    # Example queries based on the DB (will return empty/error if tables don't exist yet, so we wrap in try-except)
    try:
        where_clause = f"WHERE domain = '{domain_filter}'" if domain_filter else ""
        
        # We will render a beautifully styled layout using Plotly Go for spline charts
        df_supply = conn.execute(f"SELECT year, sum(graduates) as total FROM graduate_supply {where_clause} GROUP BY year ORDER BY year").df()
        
        # Create beautiful spline chart
        fig = go.Figure()
        if not df_supply.empty:
            fig.add_trace(go.Scatter(
                x=df_supply["year"], y=df_supply["total"],
                mode="lines",
                line=dict(shape="spline", smoothing=1.3, width=4, color="#f5b041"),
                fill='tozeroy',
                fillcolor='rgba(245, 176, 65, 0.1)'
            ))
            
        fig.update_layout(
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            margin=dict(l=0, r=0, t=30, b=0),
            xaxis=dict(showgrid=False, zeroline=False),
            yaxis=dict(showgrid=True, gridcolor='#f0f0f0', zeroline=False),
            height=250
        )
        
        # Build layout
        return html.Div([
            # KPIs
            dbc.Row([
                dbc.Col(create_kpi_card("Total Graduates", f"{df_supply['total'].sum() if not df_supply.empty else 'N/A'}", "#e74c3c"), width=4),
                dbc.Col(create_kpi_card("Employment (Y1)", "N/A", "#3498db"), width=4),
                dbc.Col(create_kpi_card("Active Programs", "N/A", "#2ecc71"), width=4),
            ], className="mb-5"),
            
            # Chart & Top Performers
            dbc.Row([
                dbc.Col([
                    html.Div([
                        html.H4("Graduate Supply Trend", className="serif-text mb-4"),
                        dcc.Graph(figure=fig, config={'displayModeBar': False})
                    ], className="custom-card")
                ], width=8),
                dbc.Col([
                    html.Div([
                        html.H4("Top Skills", className="serif-text mb-4"),
                        html.P("1. Python (66%)", className="mb-2"),
                        html.P("2. SQL (51%)", className="mb-2"),
                        html.P("3. Machine Learning (45%)", className="mb-2"),
                        html.A("View More >", href="#", style={"color": "#888", "fontSize": "0.85rem", "textDecoration": "none"})
                    ], className="custom-card", style={"height": "100%"})
                ], width=4)
            ]),
            
            # Bottom colored row (similar to image)
            html.Div([
                html.Div([
                    html.H4("Domains", className="serif-text mb-1"),
                    html.P("Distribution statistics", style={"fontSize": "0.85rem", "color": "#666", "maxWidth": "150px"})
                ]),
                html.Div([html.H5("AI", className="serif-text mb-0"), html.P("35%", className="mb-0 text-success")], className="colored-card"),
                html.Div([html.H5("DS", className="serif-text mb-0"), html.P("50%", className="mb-0 text-success")], className="colored-card"),
                html.Div([html.H5("STAT", className="serif-text mb-0"), html.P("15%", className="mb-0 text-danger")], className="colored-card"),
                html.Div("View Stats", style={"background": "#4db6ac", "color": "white", "padding": "1.5rem", "borderRadius": "15px", "fontWeight": "bold", "cursor": "pointer"})
            ], className="colored-card-container mt-2")
            
        ])
    except Exception as e:
        return html.Div([
            html.H3("Awaiting Real Data...", className="serif-text"),
            html.P("The UI is ready, but the real data tables (graduate_supply, job_demand) are not fully populated yet. Error: " + str(e))
        ], className="custom-card text-center py-5")

if __name__ == "__main__":
    app.run_server(debug=True)
