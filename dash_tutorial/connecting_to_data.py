# Import packages
from dash import Dash, html, dash_table #dash_table vai exibir uma tabela de dados
import pandas as pd

# Incorporate data
df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv')

# Initialize the app
app = Dash(__name__)

# App layout
app.layout = [
    html.Div(children='My First App with Data'),
    dash_table.DataTable(data=df.to_dict('records'), page_size=10) #Lendo o dataframe dentro da tabela do dash
]

# Run the app
if __name__ == '__main__':
    app.run(debug=True)