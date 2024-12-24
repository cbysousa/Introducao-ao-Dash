from dash import Dash, html

#Inicializa o app
app = Dash(__name__)

#App layout: componentes do app que serão exibidos no navegador (is provided as a list but it could also be a Dash component)
app.layout = html.Div([
              html.Div(children='Hello World')
])

#Roda o app
if __name__ == '__main__':
    app.run_server(debug=True)