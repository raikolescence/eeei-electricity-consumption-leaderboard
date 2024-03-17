import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
import anvil.media

# import numpy as np
# from bokeh.plotting import figure, output_file, show


# This is a server module. It runs on the Anvil server,
# rather than in the user's browser.
#
# To allow anvil.server.call() to call functions here, we mark
# them with @anvil.server.callable.
# Here is an example - you can replace it with your own:
#
# @anvil.server.callable
# def say_hello(name):
#   print("Hello, " + name + "!")
#   return 42
#

#Return the contents of the Files data table. If this table included secure data, 
#we would only want to return the data that can be user visible
@anvil.server.callable
def return_table():
  return app_tables.labs.search()


@anvil.server.callable
def get_lab_row(lab_name):
  return app_tables.labs.get(name=lab_name)


@anvil.server.callable
def get_leaderboard_order():
  data = app_tables.labs.search()

  sorted_data = sorted(data, key=lambda x: x['TotalSavings'])

  lab_order = []
  for x in sorted_data:
    lab_order.append(x[4][1])

  return lab_order


@anvil.server.callable
def get_sorted_data():
    data = app_tables.labs.search()

    sorted_data = sorted(data, key=lambda x: x['TotalSavings'])
      
    return sorted_data

@anvil.server.callable
def get_match_data(lab_name):
    data = app_tables.matches.search(q.any_of(participant1=lab_name, participant2=lab_name))
    return data



@anvil.server.callable
def make_plot():
  # Point Bokeh at a file
  output_file("/tmp/bokeh.html")

  # Make a nice wiggle
  x = np.arange(0.0, 5.0, 0.02)
  y = np.exp(-x) * np.cos(2*np.pi*x)

  # Plot it in the usual Bokeh way
  p = figure(width=600, height=300)
  p.line(x, y)

  # Save the plot  
  show(p)
  
  # Return this plot as HTML in a Media object
  return anvil.media.from_file('/tmp/bokeh.html', 'text/html')