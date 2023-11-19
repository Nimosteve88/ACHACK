import pandas as pd
import dash
from dash import dcc, html
from dash.dependencies import Input, Output

# Assuming your dataset is stored in a CSV file named 'your_data.csv'
# Replace 'your_data.csv' with the actual file name or provide the DataFrame directly if you have it loaded
file_path = 'data1.csv'
df = pd.read_csv(file_path)

# Removing non-numeric characters and converting 'kWh' column to numeric
df['kWh'] = pd.to_numeric(df['kWh'].replace('[^\d.]', '', regex=True), errors='coerce')

# Convert 'kWh' to 'MWh'
df['MWh'] = df['kWh'] / 1000  # 1 MWh = 1000 kWh

# Rounding the 'MWh' values to 3 significant figures
df['MWh'] = df['MWh'].round(3)

# Remove 'London' data
df = df[df['Area'] != 'London']

# Create a Dash web application
app = dash.Dash(__name__)

# Define layout of the web application
app.layout = html.Div([
    html.H1("Energy Consumption Dashboard"),

    # Tabs for different pages
    dcc.Tabs([
        dcc.Tab(label='Borough Comparison', children=[
            # Dropdown for selecting the years
            dcc.Dropdown(
                id='year-dropdown',
                options=[
                    {'label': str(year), 'value': year} for year in df['LEGGI_Year'].unique()
                ],
                multi=True,
                value=list(df['LEGGI_Year'].unique()),  # Set the default to all years
                style={'width': '50%'}
            ),

            # Graph to display the comparison
            dcc.Graph(id='borough-comparison-graph'),
        ]),

        dcc.Tab(label='Sector Pie Chart', children=[
            # Dropdown for selecting the year
            dcc.Dropdown(
                id='pie-chart-year-dropdown',
                options=[
                    {'label': str(year), 'value': year} for year in df['LEGGI_Year'].unique()
                ],
                multi=False,
                value=df['LEGGI_Year'].min(),  # Set the default to the minimum year
                style={'width': '50%'}
            ),

            # Graph to display the pie chart
            dcc.Graph(id='pie-chart'),
        ]),

        dcc.Tab(label='Fuel-wise MWh per Year', children=[
            # Graph to display the fuel-wise MWh per year
            dcc.Graph(id='fuel-wise-mwh'),
        ]),
    ]),
])

# Define callback to update the borough comparison graph based on user input
@app.callback(
    Output('borough-comparison-graph', 'figure'),
    [Input('year-dropdown', 'value')]
)
def update_borough_comparison(selected_years):
    filtered_df = df[df['LEGGI_Year'].isin(selected_years)]

    borough_comparison_data = []

    for year in selected_years:
        year_data = filtered_df[filtered_df['LEGGI_Year'] == year]
        borough_comparison_data.append({'x': year_data['Area'], 'y': year_data['MWh'], 'type': 'bar', 'name': year})

    fig = {
        'data': borough_comparison_data,
        'layout': {
            'title': f'MWh Comparison ({", ".join(map(str, selected_years))})',
            'barmode': 'group'
        }
    }

    return fig

# Define callback to update the pie chart based on the selected year
@app.callback(
    Output('pie-chart', 'figure'),
    [Input('pie-chart-year-dropdown', 'value')]
)
def update_pie_chart(selected_year):
    filtered_df = df[df['LEGGI_Year'] == selected_year]

    # Exclude 'Total' from the pie chart
    filtered_df = filtered_df[filtered_df['Sector'] != 'Total']

    # Calculate total MWh for each sector
    total_mwh_per_sector = filtered_df.groupby('Sector')['MWh'].sum().reset_index()

    # Create the pie chart
    fig = {
        'data': [
            {
                'labels': total_mwh_per_sector['Sector'],
                'values': total_mwh_per_sector['MWh'],
                'type': 'pie',
                'name': 'MWh distribution'
            }
        ],
        'layout': {
            'title': f'MWh Distribution by Sector for {selected_year}'
        }
    }

    return fig

# Define callback to update the fuel-wise MWh per year graph
@app.callback(
    Output('fuel-wise-mwh', 'figure'),
    [Input('year-dropdown', 'value')]
)
def update_fuel_wise_mwh(selected_years):
    try:
        filtered_df = df[df['LEGGI_Year'].isin(selected_years)]

        fuel_wise_mwh_data = []

        max_y_per_fuel = {}  # Dictionary to store the maximum y-axis value for each fuel type

        for fuel_type in filtered_df['Fuel'].unique():
            # Exclude 'Total' from fuel types
            if fuel_type != 'Total':
                fuel_data = filtered_df[filtered_df['Fuel'] == fuel_type]
                max_y_per_fuel[fuel_type] = fuel_data['MWh'].max()  # Store the maximum value for the current fuel type
                fuel_wise_mwh_data.append({'x': selected_years, 'y': fuel_data['MWh'], 'type': 'bar', 'name': fuel_type})

        max_y = max(max_y_per_fuel.values(), default=0)  # Get the overall maximum y-axis value

        fig = {
            'data': fuel_wise_mwh_data,
            'layout': {
                'title': 'Fuel-wise MWh per Year',
                'xaxis': {'title': 'Year'},
                'yaxis': {'title': 'MWh', 'range': [0, max_y * 1.1]},  # Set the y-axis range based on max_y
                'shapes': [],  # Ensure shapes are defined to avoid potential issues
            }
        }

        # Add faint lines between different years
        for i in range(1, len(selected_years)):
            fig['layout']['shapes'].append({
                'type': 'line',
                'x0': selected_years[i],
                'y0': 0,
                'x1': selected_years[i],
                'y1': max_y,
                'line': {
                    'color': 'rgba(128, 128, 128, 0.5)',
                    'width': 2,
                    'dash': 'dash',
                },
            })

        return fig

    except Exception as e:
        print(e)
        return {'data': [], 'layout': {}}

# Run the web application
if __name__ == '__main__':
    app.run_server(debug=True)
