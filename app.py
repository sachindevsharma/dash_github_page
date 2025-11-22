import dash
from dash import dcc, html, Input, Output
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

# Sample data
df = pd.DataFrame({
    'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
    'Sales': [100, 150, 120, 200, 180, 220],
    'Profit': [20, 30, 25, 40, 35, 45],
    'Region': ['North', 'North', 'South', 'North', 'South', 'South']
})

# Initialize Dash app
app = dash.Dash(__name__)
server = app.server

# App layout
app.layout = html.Div([
    html.Div([
        html.H1("📊 Sales Dashboard", style={'textAlign': 'center', 'marginBottom': 30, 'color': '#2c3e50'}),
        
        html.Div([
            html.Div([
                html.Label("Select Region:", style={'fontWeight': 'bold', 'marginBottom': 10}),
                dcc.Dropdown(
                    id='region-dropdown',
                    options=[
                        {'label': 'All Regions', 'value': 'All'},
                        {'label': 'North', 'value': 'North'},
                        {'label': 'South', 'value': 'South'}
                    ],
                    value='All',
                    style={'width': '100%'}
                )
            ], style={'width': '100%', 'marginBottom': 20}),
        ], style={'width': '100%'}),
        
        html.Div(id='graph-container')
    ], style={'padding': '30px', 'fontFamily': 'Arial, sans-serif', 'maxWidth': '1200px', 'margin': '0 auto'})
], style={'backgroundColor': '#ecf0f1', 'minHeight': '100vh', 'padding': '20px'})

# Callback to update graph
@app.callback(
    Output('graph-container', 'children'),
    Input('region-dropdown', 'value')
)
def update_graph(selected_region):
    if selected_region == 'All':
        filtered_df = df
        title = 'Sales & Profit by Month - All Regions'
    else:
        filtered_df = df[df['Region'] == selected_region]
        title = f'Sales & Profit by Month - {selected_region}'
    
    fig = go.Figure(data=[
        go.Bar(name='Sales', x=filtered_df['Month'], y=filtered_df['Sales'], marker_color='#3498db'),
        go.Bar(name='Profit', x=filtered_df['Month'], y=filtered_df['Profit'], marker_color='#2ecc71')
    ])
    
    fig.update_layout(
        title=title,
        barmode='group',
        xaxis_title='Month',
        yaxis_title='Amount ($)',
        hovermode='x unified',
        template='plotly_white',
        height=500
    )
    
    return dcc.Graph(figure=fig, style={'boxShadow': '0 4px 6px rgba(0,0,0,0.1)', 'borderRadius': '8px', 'marginTop': '20px'})

if __name__ == '__main__':
    app.run(debug=False)