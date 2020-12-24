import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

a1 = html.Div(["Input: ",
              dcc.Input(id='my-input', value='initial value', type='text')])

app.layout = html.Div([
    html.H6("Change the value in the text box to see callbacks in action!"),
    a1,
    html.Br(),
    html.Div(id='my-output'),

])

b1 = Input(component_id='my-input', component_property='value')
@app.callback(
    Output(component_id='my-output', component_property='children'),
    b1
)
def update_output_div(input_value):
    return 'Output: {}'.format(input_value)


if __name__ == '__main__':
    app.run_server(debug=True)
