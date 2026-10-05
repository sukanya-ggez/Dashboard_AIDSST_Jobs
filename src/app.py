import dash
from dash import dcc, html, Input, Output
import dash_bootstrap_components as dbc

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
                    html.P("Filters (Year, Country, Domain, etc.) will go here.")
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
    Input("tabs", "active_tab")
)
def render_tab_content(active_tab):
    if active_tab == "tab-1":
        return html.Div([
            html.H3("Graduate Supply & Curriculum Skills"),
            html.P("KPI Cards and Charts related to Graduate Supply will be displayed here.")
        ])
    elif active_tab == "tab-2":
        return html.Div([
            html.H3("Job Demand & Required Skills"),
            html.P("KPI Cards and Charts related to Job Demand will be displayed here.")
        ])
    elif active_tab == "tab-3":
        return html.Div([
            html.H3("Skills Mismatch Analysis"),
            html.P("Analysis comparing Supply and Demand will be displayed here.")
        ])
    return html.P("This shouldn't ever be displayed...")

if __name__ == "__main__":
    app.run_server(debug=True)
