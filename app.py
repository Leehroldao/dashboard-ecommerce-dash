import pandas as pd
import dash
from dash import dcc, html
import plotly.express as px

# ==========================
# Ler os dados
# ==========================
df = pd.read_csv("ecommerce_estatistica.csv")

# ==========================
# Criar gráficos
# ==========================

fig_hist = px.histogram(df, x=df.columns[0], title="Histograma")

fig_scatter = px.scatter(
    df,
    x=df.columns[0],
    y=df.columns[1],
    title="Gráfico de Dispersão"
)

fig_heatmap = px.imshow(
    df.corr(numeric_only=True),
    text_auto=True,
    title="Mapa de Calor"
)

fig_bar = px.bar(
    df,
    x=df.columns[0],
    y=df.columns[1],
    title="Gráfico de Barras"
)

fig_pie = px.pie(
    df,
    names=df.columns[0],
    title="Gráfico de Pizza"
)

fig_density = px.density_contour(
    df,
    x=df.columns[0],
    y=df.columns[1],
    title="Gráfico de Densidade"
)

fig_reg = px.scatter(
    df,
    x=df.columns[0],
    y=df.columns[1],
    trendline="ols",
    title="Gráfico de Regressão"
)

# ==========================
# App Dash
# ==========================
app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("📊 Dashboard Ecommerce - Estatísticas", style={"textAlign": "center"}),

    dcc.Graph(figure=fig_hist),
    dcc.Graph(figure=fig_scatter),
    dcc.Graph(figure=fig_heatmap),
    dcc.Graph(figure=fig_bar),
    dcc.Graph(figure=fig_pie),
    dcc.Graph(figure=fig_density),
    dcc.Graph(figure=fig_reg),
])

if __name__ == "__main__":
    app.run_server(debug=True)
