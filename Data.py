import csv 
import pandas as pd 
import plotly.figure_factory as ff
df = pd.read_csv('data.csv')
graph = ff.create_distplot([df['Height'].tolist()],['Height'])
graph.show()