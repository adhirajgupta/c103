import pandas as pd
import plotly.express as px
df = pd.read_csv("csv files/line_chart.csv")
fig = px.histogram(df,x = 'Year',y = 'Per capita income',color = 'Country',title = 'Per Capita income')
fig.show()
#print(df)
