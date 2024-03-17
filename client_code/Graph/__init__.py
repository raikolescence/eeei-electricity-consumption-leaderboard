from ._anvil_designer import GraphTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

from plotly import graph_objs as go

class Graph(GraphTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

    #plot 
    day = []
    for row in app_tables.weeklydata.search():
      day.append(row['timestamp'].date())

    weekly_data_labs = {
        "Microlab": [],
        "SSL": [],
        "RAL": [],
        "CNL": []
    }

    
    for row in app_tables.weeklydata.search():
        for column, value in row:
            if column in weekly_data_labs:
                weekly_data_labs[column].append(value)

    
    microlab_data = weekly_data_labs["Microlab"]
    ssl_data = weekly_data_labs["SSL"]
    ral_data = weekly_data_labs["RAL"]
    cnl_data = weekly_data_labs["CNL"]

        
    # Create and style traces
    trace0 = go.Scatter(
        x = day,
        y = ssl_data,
        name = 'SSL',
        line = dict(
            color = ('rgb(255, 0, 0)'),
            width = 1)
    )
    trace1 = go.Scatter(
        x = day,
        y = ral_data,
        name = 'RAL',
        line = dict(
            color = ('rgb(0, 255, 0)'),
            width = 1,)
    )
    trace2 = go.Scatter(
        x = day,
        y = microlab_data,
        name = 'Microlab',
        line = dict(
            color = ('rgb(0, 0, 255)'),
            width = 1) # dash options include 'dash', 'dot', and 'dashdot'
    )
    trace3 = go.Scatter(
        x = day,
        y = cnl_data,
        name = 'CNL',
        line = dict(
            color = ('rgb(0, 0, 0)'),
            width = 1)
    )
    
    self.lab_plot.data = [trace0, trace1, trace2, trace3]
    
    self.lab_plot.layout = dict(title = 'Test',
                  xaxis = dict(title = 'day'),
                  yaxis = dict(title = 'energy'),
    )    
    
    # end plot
