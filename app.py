import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import plotly.express as px
import dash_bootstrap_components as dbc

import pandas as pd

########### Define your variables
mytitle='FPL DB'
tabtitle='FPL DB!'

data = pd.read_csv(r'player_data.csv')
data.set_index(['id'])
data.head()

########### Initiate the app
app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server
app.title=tabtitle

########### Modify dataset
data['Total Cards'] = data['yellow_cards'] + data['red_cards']
data['GW Transfers'] = data['transfers_in_event'] - data['transfers_out_event']
data['Points per mil'] = data['total_points']*10.0 / data['now_cost']
data['now_cost'] = data['now_cost']/10.0

# Getting Team Names
team_dt = pd.DataFrame ({'team_code':[3, 7, 36, 90, 8, 31, 11, 54, 2, 13, 14, 43, 4, 49, 20, 6, 35, 21, 39, 1],
                         'team_name':['Arsenal', 'Aston Villa', 'Brighton & Howe Albion', 'Burnley', 'Chelsea', 
                                      'Crystal Palace', 'Everton', 'Fulham', 'Leeds United', 'Leicester City', 
                                      'Liverpool', 'Manchester City', 'Newcastle United', 'Sheffield United', 
                                      'Southampton', 'Spurs', 'West Brom', 'West Ham United', 'Wolves', 'Manchester United']})
df1 = data.merge(team_dt, on='team_code', how='left')
# df1.columns

# Getting player positions
pos_dt = pd.DataFrame ({'element_type':[1,2,3,4],
                         'position':['Goalkeepers', 'Defenders', 'Midfielders', 'Forwards']})
df = df1.merge(pos_dt, on='element_type', how='left')
# df.head()

df = df[['assists', 'bonus', 'bps', 'clean_sheets', 'code', 'cost_change_event', 'cost_change_start', 'creativity',
         'dreamteam_count', 'element_type', 'ep_next', 'ep_this', 'event_points', 'first_name', 'form', 'goals_conceded',
         'goals_scored', 'ict_index', 'id', 'influence', 'minutes', 'now_cost', 'own_goals', 'penalties_missed',
         'penalties_saved', 'photo', 'points_per_game', 'red_cards', 'saves', 'second_name', 'selected_by_percent',
         'threat', 'total_points', 'transfers_in', 'transfers_in_event', 'transfers_out', 'transfers_out_event',
         'web_name', 'yellow_cards', 'Total Cards', 'team_name', 'position', 'Points per mil']]
df = df.set_axis(['Assists', 'Bonus', 'BPS', 'Clean sheets', 'Code','Cost change event', 'Cost change start',
                  'Creativity', 'No. of times in Dreamteam', 'Element Type', 'EP next', 'EP this', 'GW Points',
                  'First Name', 'Form', 'Goals Conceded', 'Goals Scored', 'ICT Index', 'ID', 'Influence', 'Minutes',
                  'Cost', 'Own Goals', 'Penalties Missed', 'Penalties saved', 'Photo', 'Points per Game', 'Red Cards',
                  'Saves', 'Second Name', 'Selected by Percent', 'Threat', 'Total Points', 'Transfers In',
                  'Transfers in GW', 'Transfers out', 'Transfers out GW', 'Web Name', 'Yellow cards', 'Total Cards',
                  'Team Name', 'Position', 'Points per mil'],
            axis=1, inplace=False)
df.columns

# X/Y axis list
xycol = ['Total Points', 'Points per Game', 'Points per mil', 'Goals Scored', 'Assists', 'Goals Conceded', 'Minutes', 'Cost', 
         'Bonus', 'BPS', 'Clean sheets', 'Saves', 'Selected by Percent', 'ICT Index', 'Influence', 'Creativity', 'Threat',
         'Form', 'No. of times in Dreamteam', 'Yellow cards', 'Red Cards', 'Total Cards']

tbl_col=[
        {'name': 'First Name', 'id': 'First Name', 'deletable': False, 'selectable': False}, 
        {'name': 'Second Name', 'id': 'Second Name', 'deletable': False, 'selectable': False},
        {'name': 'Team Name', 'id': 'Team Name', 'deletable': False, 'selectable': False}, 
        {'name': 'Position', 'id': 'Position', 'deletable': False, 'selectable': False},
        {'name': 'Cost', 'id': 'Cost', 'deletable': False, 'selectable': False}, 
        {'name': 'Total Points', 'id': 'Total Points', 'deletable': False, 'selectable': False}, 
        {'name': 'Minutes', 'id': 'Minutes', 'deletable': False, 'selectable': False}, 
        {'name': 'Selected by Percent', 'id': 'Selected by Percent', 'deletable': False, 'selectable': False}, 
        {'name': 'Points per Game', 'id': 'Points per Game', 'deletable': False, 'selectable': False}, 
        {'name': 'Points per mil', 'id': 'Points per mil', 'deletable': False, 'selectable': False}, 
        {'name': 'GW Transfers', 'id': 'GW Transfers', 'deletable': False, 'selectable': False},
        {'name': 'Goals Scored', 'id': 'Goals Scored', 'deletable': False, 'selectable': False}, 
        {'name': 'Assists', 'id': 'Assists', 'deletable': False, 'selectable': False}, 
        {'name': 'Goals Conceded', 'id': 'Goals Conceded', 'deletable': False, 'selectable': False}, 
        {'name': 'Saves', 'id': 'Saves', 'deletable': False, 'selectable': False}, 
        {'name': 'Bonus', 'id': 'Bonus', 'deletable': False, 'selectable': False}, 
        {'name': 'BPS', 'id': 'BPS', 'deletable': False, 'selectable': False},
        {'name': 'ICT Index', 'id': 'ICT Index', 'deletable': False, 'selectable': False}, 
        {'name': 'Influence', 'id': 'Influence', 'deletable': False, 'selectable': False}, 
        {'name': 'Creativity', 'id': 'Creativity', 'deletable': False, 'selectable': False}, 
        {'name': 'Threat', 'id': 'Threat', 'deletable': False, 'selectable': False}, 
        {'name': 'Form', 'id': 'Form', 'deletable': False, 'selectable': False}, 
        {'name': 'Clean sheets', 'id': 'Clean sheets', 'deletable': False, 'selectable': False}, 
        {'name': 'Total Cards', 'id': 'Total Cards', 'deletable': False, 'selectable': False},
        {'name': 'Red Cards', 'id': 'Red Cards', 'deletable': False, 'selectable': False}, 
        {'name': 'Yellow cards', 'id': 'Yellow cards', 'deletable': False, 'selectable': False}, 
        {'name': 'Cost change event', 'id': 'Cost change event', 'deletable': False, 'selectable': False},
        {'name': 'Penalties Missed', 'id': 'Penalties Missed', 'deletable': False, 'selectable': False},
        {'name': 'Penalties saved', 'id': 'Penalties saved', 'deletable': False, 'selectable': False}, 
        {'name': 'EP next', 'id': 'EP next', 'deletable': False, 'selectable': False},
        {'name': 'EP this', 'id': 'EP this', 'deletable': False, 'selectable': False},
        {'name': 'Own Goals', 'id': 'Own Goals', 'deletable': False, 'selectable': False}, 
        {'name': 'No. of times in Dreamteam', 'id': 'No. of times in Dreamteam', 'deletable': False, 'selectable': False}
    ]

# the style arguments for the sidebar. We use position:fixed and a fixed width
TOPBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "100rem",
    # "padding": "10px 10px",
}

########### Set up the layout
app.layout = html.Div(children=[
    html.H1(children = "FPL Dashboard",
           style = {
              'textAlign' : 'center',
              'color' : '#ffffff ',
              'background' : '#2376BD'
           }
           ),
    
    html.Div(children=[
        html.Div('Select Team(s):'),
        
        dcc.Dropdown(
            id='team_dd', 
            multi=True,
            options = [{'label': i, 'value': i} for i in sorted(df['Team Name'].unique())]
            ,value=['Arsenal', 'Aston Villa', 'Brighton & Howe Albion', 'Burnley', 'Chelsea', 'Crystal Palace',
                    'Everton', 'Fulham', 'Leeds United', 'Leicester City', 'Liverpool', 'Manchester City', 
                    'Newcastle United', 'Sheffield United', 'Southampton', 'Spurs', 'West Brom', 
                    'West Ham United', 'Wolves', 'Manchester United']
            )], style={"border":"2px black solid"}),
    
    html.Div([
        html.Div(children=[
        html.Div('Select Position(s):'),
        
        dcc.Dropdown(
            id='pos_dd', 
            multi=True,
            options = [{'label': i, 'value': i} for i in sorted(df['Position'].unique())]
            ,value=['Goalkeepers', 'Defenders', 'Midfielders', 'Forwards']
        )],
        style={'width': '33%', 'display': 'inline-block'}),
    
    html.Div(children=[
        html.Div('Select X-axis:'),
        
        dcc.Dropdown(
            id='x_dd', 
            multi=False,
            options = [{'label': i, 'value': i} for i in xycol]
            ,value='Minutes'
        )],
        style={'width': '33%', 'display': 'inline-block'}),
    
    html.Div(children=[
        html.Div('Select Y-axis:'),
        
        dcc.Dropdown(
            id='y_dd', 
            multi=False,
            options = [{'label': i, 'value': i} for i in xycol]
            ,value='Total Points'
        )],
        style={'width': '33%', 'display': 'inline-block'}),
    ], style={"border":"2px black solid"}),
    
    html.Div([
        html.Div(children=[
#         Min. Minutes played:
        html.Div('Total Minutes Played greater than:'),
        
        dcc.Input(id='min_mp', value='450', type='text')
    ],
        style={'width': '40%', 'display': 'inline-block'}),
    
    html.Div(children=[
#         Min. Minutes played:
        html.Div('Select Cost Range:'),
        
        html.Div([
            html.Div(['Min:'],style={'width': '48%', 'display': 'inline-block'}),
            dcc.Input(id='min_cost', value='4.5', type='text',style={'width': '48%', 'display': 'inline-block'})
        ],style={'width': '48%', 'display': 'inline-block'}),
        
        html.Div([
            html.Div('Max:',style={'width': '48%', 'display': 'inline-block'}),
            dcc.Input(id='max_cost', value='10.0', type='text',style={'width': '48%', 'display': 'inline-block'})
        ],style={'width': '48%', 'float':'right', 'display': 'inline-block'}),
    ],
        style={'width': '60%', 'float':'right', 'display': 'inline-block'}),
    ], style={"border":"2px black solid"}),
    
    dcc.Graph(
        id='plotter',
        config={
            'displayModeBar': False
        }
    ),
    
    html.Div(children=[
        html.Div(id='median_x'),
        html.Div(id='median_y'),
    ], style={"border":"2px black solid"}),
]
)

@app.callback(
    [dash.dependencies.Output('plotter', 'figure'), 
     dash.dependencies.Output('median_x', 'children'),
     dash.dependencies.Output('median_y', 'children')],
    [dash.dependencies.Input('team_dd', 'value'),
     dash.dependencies.Input('pos_dd', 'value'),
     dash.dependencies.Input('x_dd', 'value'),
     dash.dependencies.Input('y_dd', 'value'),
     dash.dependencies.Input('min_mp', 'value'),
     dash.dependencies.Input('min_cost', 'value'),
     dash.dependencies.Input('max_cost', 'value')])
def upadte_chart(team_dd_value, pos_dd_value, x_dd_value, y_dd_value, min_mp_value, min_cost_val, max_cost_val):
    
    x_dd_value = x_dd_value
    y_dd_value = y_dd_value
    
    print(team_dd_value, pos_dd_value, x_dd_value, y_dd_value, min_mp_value, min_cost_val, max_cost_val)
    
    data1 = df[df["Team Name"].isin(team_dd_value) & 
               df["Position"].isin(pos_dd_value) & 
               (df["Minutes"]>=int(min_mp_value)) &
              (df["Cost"]>=float(min_cost_val)) &
              (df["Cost"]<=float(max_cost_val))]
    
    beer_fig = px.scatter(
        data1,
        x=x_dd_value,
        y=y_dd_value,
        hover_name="Web Name",
        color="Team Name",
        labels={
          "Team Name": "Team Name"
        },
    )
    
    x_med = data1[x_dd_value].median()
    y_med = data1[y_dd_value].median()
    print(x_med,y_med)
    
    beer_fig.layout.update(hovermode='closest')
    beer_fig.update_layout(showlegend=False)
    
    beer_fig.layout.update(
        title = x_dd_value + " vs " + y_dd_value)
    
    r_xmed = "The median for " + str(x_dd_value) + " is: " + str(x_med)
    r_ymed = "The median for " + str(y_dd_value) + " is: " + str(y_med)
    
    return beer_fig, r_xmed, r_ymed
    
    if len(team_dd_value) == 0:
        raise dash.exceptions.PreventUpdate
        

if __name__ == '__main__':
    app.run_server()
    
