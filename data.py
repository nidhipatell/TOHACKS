import pandas as pd
import plotly.graph_objs as go
import datetime

df = pd.read_csv("data/time_series_covid_19_confirmed.csv")
df = df.rename(columns={"Country/Region" : "Country", "Province/State": "Province"})
print(df.head())

date = datetime.datetime.now()
day = date.day
month = date.month
year = date.year

print("Year:",year,"month:",month,"day:",day)

StringDate = str(month)+"/"+str(day)+"/"+"20"
print(StringDate)

df['text'] = df['Country'] + " " + df["4/13/20"].astype(str)
fig = go.Figure(data = go.Scattergeo(
    lon = df["Long"],
    lat = df["Lat"],
    text = df["text"],
    mode = "markers",
    marker = dict(
        size = 12,
        opacity = 0.8,
        reversescale = True,
        autocolorscale = True,
        symbol = 'square',
        line = dict(
            width = 1,
            color = 'rgba(102, 102, 102)'
        ),
        cmin = 0,
        color = df['4/13/20'],
        cmax = df['4/13/20'].max(),
        colorbar_title = "COVID 19 Reported Cases"
    )
))

fig.update_layout(
    title = "Covid-19 Confirmed Cases Around the World",
    geo = dict(
        scope = "world",
        showland = True,
    )
)

fig.write_html('first_figure.html', auto_open=True)