"""
Dash CRM Demo - Plotly's web framework for data science
Dash creates analytical web applications
"""

import dash
from dash import dcc, html, Input, Output, dash_table
import pandas as pd
import plotly.express as px

# Initialize the app
app = dash.Dash(__name__, title="Dash Ultimate CRM Demo")
app.config.suppress_callback_exceptions = True

# Sample customer data
def get_customer_data():
    data = []
    for i in range(1, 16):
        data.append({
            "ID": 100 + i,
            "Organization": f"Client {i} Corp",
            "Sector": "Tech",
            "Revenue": f"${i*10}k",
            "Score": f"{70+i}%"
        })
    return pd.DataFrame(data)

# App layout
app.layout = html.Div([
    html.H1("Enterprise CRM System", style={'textAlign': 'center', 'color': '#2c3e50'}),
    html.P("Built with Dash - Plotly's web framework", style={'textAlign': 'center'}),
    
    dcc.Tabs(id="tabs", value='dashboard', children=[
        dcc.Tab(label='Performance Dashboard', value='dashboard'),
        dcc.Tab(label='Customer Registry', value='customers'),
        dcc.Tab(label='System Administration', value='admin'),
    ]),
    
    html.Div(id='tab-content')
])

# Dashboard content
dashboard_layout = html.Div([
    html.H2("Enterprise Data Overview", style={'textAlign': 'center'}),
    
    html.Div([
        html.Div([
            html.H3("Global Sales", style={'color': 'blue'}),
            html.H2("$1.28M", style={'color': 'blue', 'fontSize': '2em'})
        ], style={'width': '30%', 'display': 'inline-block', 'textAlign': 'center', 'padding': '20px', 'backgroundColor': '#e3f2fd', 'margin': '10px', 'borderRadius': '8px'}),
        
        html.Div([
            html.H3("Conversion", style={'color': 'green'}),
            html.H2("18.4%", style={'color': 'green', 'fontSize': '2em'})
        ], style={'width': '30%', 'display': 'inline-block', 'textAlign': 'center', 'padding': '20px', 'backgroundColor': '#e8f5e9', 'margin': '10px', 'borderRadius': '8px'}),
        
        html.Div([
            html.H3("Pending Tasks", style={'color': 'red'}),
            html.H2("14", style={'color': 'red', 'fontSize': '2em'})
        ], style={'width': '30%', 'display': 'inline-block', 'textAlign': 'center', 'padding': '20px', 'backgroundColor': '#ffebee', 'margin': '10px', 'borderRadius': '8px'}),
    ]),
    
    html.H3("System Synchronization State"),
    dcc.Progress(value=72, id="sync-progress", style={'height': '30px'}),
    html.P("72% Complete", id="sync-label"),
    
    html.H3("Sales Trend"),
    dcc.Graph(
        figure=px.line(
            pd.DataFrame({'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May'], 'Sales': [120000, 135000, 128000, 142000, 128000]}),
            x='Month',
            y='Sales',
            title='Monthly Sales'
        )
    )
])

# Customers content
customers_layout = html.Div([
    html.H2("Customer Registry"),
    html.Div([
        dcc.Input(id='search-input', type='text', placeholder='Search customers...', style={'width': '100%', 'padding': '10px'}),
    ]),
    html.Div(id='customer-table-container')
])

# Admin content
admin_layout = html.Div([
    html.H2("System Administration"),
    html.H3("Global Client Registry Entry"),
    
    html.Div([
        html.Div([
            dcc.Input(id='org-name', type='text', placeholder='Organization Lead Name', style={'width': '100%', 'padding': '10px', 'margin': '5px'}),
            dcc.Textarea(id='notes', placeholder='Relationship History / Notes', style={'width': '100%', 'height': '100px', 'padding': '10px', 'margin': '5px'}),
            dcc.Dropdown(id='industry', options=['Finance', 'Healthcare', 'Tech', 'Education'], placeholder='Industry Vertical', style={'margin': '5px'}),
            dcc.RadioItems(id='strategy', options=['B2B (Enterprise)', 'B2C (Retail)'], value='B2B (Enterprise)', style={'margin': '5px'}),
            dcc.Checklist(id='billing', options=[{'label': 'Enable Advanced Billing Tier', 'value': 'billing'}], style={'margin': '5px'}),
            dcc.Checklist(id='web-visible', options=[{'label': 'ACCOUNT VISIBLE ON WEB PORTAL', 'value': 'visible'}], style={'margin': '5px'}),
        ], style={'width': '48%', 'display': 'inline-block', 'verticalAlign': 'top'}),
        
        html.Div([
            dcc.Slider(id='priority', min=0, max=100, value=50, marks={i: str(i) for i in range(0, 101, 20)}, tooltip={"placement": "bottom", "always_visible": True}),
            html.Label("Engagement Priority", style={'margin': '5px'}),
            dcc.Input(id='seats', type='number', placeholder='Dedicated Seat Count', value=10, style={'width': '100%', 'padding': '10px', 'margin': '5px'}),
            dcc.Input(id='contract-date', type='text', placeholder='Contract Start Date (YYYY-MM-DD)', style={'width': '100%', 'padding': '10px', 'margin': '5px'}),
            dcc.Input(id='meeting-time', type='text', placeholder='Preferred Meeting Time (HH:MM)', style={'width': '100%', 'padding': '10px', 'margin': '5px'}),
            html.Button('Submit Entry', id='submit-btn', n_clicks=0, style={'width': '100%', 'padding': '10px', 'margin': '5px', 'backgroundColor': '#4CAF50', 'color': 'white', 'border': 'none', 'borderRadius': '4px'}),
            html.Div(id='submit-result', style={'margin': '10px'})
        ], style={'width': '48%', 'display': 'inline-block', 'verticalAlign': 'top'}),
    ])
])

# Callback for tab content
@app.callback(Output('tab-content', 'children'), Input('tabs', 'value'))
def render_content(tab):
    if tab == 'dashboard':
        return dashboard_layout
    elif tab == 'customers':
        return customers_layout
    elif tab == 'admin':
        return admin_layout

# Callback for customer table
@app.callback(Output('customer-table-container', 'children'), Input('search-input', 'value'))
def update_customer_table(search_value):
    df = get_customer_data()
    if search_value:
        df = df[df['Organization'].str.contains(search_value, case=False, na=False)]
    
    return dash_table.DataTable(
        data=df.to_dict('records'),
        columns=[{"name": i, "id": i} for i in df.columns],
        style_cell={'textAlign': 'left'},
        style_header={'backgroundColor': 'rgb(230, 230, 230)', 'fontWeight': 'bold'}
    )

# Callback for form submission
@app.callback(
    Output('submit-result', 'children'),
    Input('submit-btn', 'n_clicks'),
    [Input('org-name', 'value'),
     Input('industry', 'value'),
     Input('strategy', 'value'),
     Input('priority', 'value')],
    prevent_initial_call=True
)
def submit_form(n_clicks, org_name, industry, strategy, priority):
    if n_clicks > 0:
        return html.Div([
            html.H4("Entry Submitted Successfully!", style={'color': 'green'}),
            html.P(f"Organization: {org_name}"),
            html.P(f"Industry: {industry}"),
            html.P(f"Strategy: {strategy}"),
            html.P(f"Priority: {priority}")
        ])
    return ""

if __name__ == '__main__':
    app.run_server(debug=False, host='127.0.0.1', port=8050)
