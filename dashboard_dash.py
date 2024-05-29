import pandas as pd
import dash
from dash import dcc
from dash import html
import plotly.express as px

df = pd.read_csv('./notebooks/Life Expectancy Data.csv')

app = dash.Dash(__name__)

fig_histograma = px.histogram(df, x='Life expectancy ', nbins=30, title='Distribución de la Esperanza de Vida')

fig_dispersion_1 = px.scatter(df, x="Adult Mortality", y="Life expectancy ",
                 title="Relación entre Esperanza de Vida y Mortalidad en Adultos")

fig_dispersion_2 = px.scatter(df, x="Life expectancy ", y="percentage expenditure",
                            title="Relación entre Esperanza de Vida y Gasto Sanitario",
                            labels={"Life expectancy ": "Esperanza de Vida (años)", "percentage expenditure": "Gasto Sanitario (%)"},
                            template="plotly_white").update_traces(textposition="top center")

num_data = df.select_dtypes(include=['float64', 'int64'])
corr_matrix = num_data.corr()

fig_corr = px.imshow(corr_matrix, 
                     labels=dict(x="Variables", y="Variables", color="Correlación"),
                     x=corr_matrix.columns,
                     y=corr_matrix.columns,
                     color_continuous_scale='RdBu_r',
                     zmin=-1, zmax=1)
fig_corr.update_layout(
    autosize=False,
    width=800,
    height=800,
    margin=dict(l=50, r=50, b=50, t=50, pad=4)
)

app.layout = html.Div(children=[
    html.H1(children='Life Expectancy Dashboard'),
    
    dcc.Graph(figure=fig_histograma),
    
    dcc.Graph(figure=fig_dispersion_1),
    
    dcc.Graph(figure=fig_dispersion_2),
    
    dcc.Graph(figure=fig_corr)
])

if __name__ == '__main__':
    app.run_server(debug=True)