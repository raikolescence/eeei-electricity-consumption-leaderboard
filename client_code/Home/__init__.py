from ._anvil_designer import HomeTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Home(HomeTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

    # # lab order in array
    # order = anvil.server.call('get_leaderboard_order')
    
    # #first place
    # lab_row = anvil.server.call('get_lab_row', order[0])
    # self.first_place.text = lab_row["name"]
    # self.first_image.source = lab_row["logo"]

    # #second place
    # lab_row = anvil.server.call('get_lab_row', order[1])
    # self.second_place.text = lab_row["name"]
    # self.second_image.source = lab_row["logo"]

    # #third place
    # lab_row = anvil.server.call('get_lab_row', order[2])
    # self.third_place.text = lab_row["name"]
    # self.third_image.source = lab_row["logo"]

    # #fourth place
    # lab_row = anvil.server.call('get_lab_row', order[3])
    # self.fourth_place.text = lab_row["name"]
    # self.fourth_image.source = lab_row["logo"]

    # #fifth place
    # lab_row = anvil.server.call('get_lab_row', order[4])
    # self.fifth_place.text = lab_row["name"]
    # self.fifth_image.source = lab_row["logo"]
    
  # # lab order in array
  #   order = anvil.server.call('get_leaderboard_order')
    
  #   # Iterate over the 12 places
  #   for i in range(12):
  #     lab_row = anvil.server.call('get_lab_row', order[i])
  #     # Update place text
  #     getattr(self, f"{['first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh', 'eighth', 'ninth', 'tenth', 'eleventh', 'twelfth'][i]}_place").text = lab_row["name"]
  #     # Update image source
  #     getattr(self, f"{['first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh', 'eighth', 'ninth', 'tenth', 'eleventh', 'twelfth'][i]}_image").source = lab_row["logo"]

