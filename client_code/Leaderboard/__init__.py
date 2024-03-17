from ._anvil_designer import LeaderboardTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Leaderboard(LeaderboardTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # get sorted data
    sorted_data = anvil.server.call('get_sorted_data')
    count = 0
    for i in sorted_data:
      # Update place text
      getattr(self, f"{['first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh', 'eighth', 'ninth', 'tenth', 'eleventh', 'twelfth', 'thirteenth', 'fourteenth'][count]}_place").text = i["name"]
      # Update image source
      getattr(self, f"{['first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh', 'eighth', 'ninth', 'tenth', 'eleventh', 'twelfth', 'thirteenth', 'fourteenth'][count]}_image").source = i["logo"]
      # Update savings text
      getattr(self, f"{['first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh', 'eighth', 'ninth', 'tenth', 'eleventh', 'twelfth', 'thirteenth', 'fourteenth'][count]}_savings").text = i["TotalSavings"]
      # Update lastupdated text
      getattr(self, f"{['first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh', 'eighth', 'ninth', 'tenth', 'eleventh', 'twelfth', 'thirteenth', 'fourteenth'][count]}_updated").text = i["TotalSavingsLastUpdated"]
      
      count += 1

      
      
  # # lab order in array
  #   order = anvil.server.call('get_leaderboard_order')

  #   # Iterate over the 12 places
  #   for i in range(12):
  #     lab_row = anvil.server.call('get_lab_row', order[i])
  #     # Update place text
  #     getattr(self, f"{['first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh', 'eighth', 'ninth', 'tenth', 'eleventh', 'twelfth'][i]}_place").text = lab_row["name"]
  #     # Update image source
  #     getattr(self, f"{['first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh', 'eighth', 'ninth', 'tenth', 'eleventh', 'twelfth'][i]}_image").source = lab_row["logo"]
  #     # Update savings text
  #     getattr(self, f"{['first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh', 'eighth', 'ninth', 'tenth', 'eleventh', 'twelfth'][i]}_savings").text = lab_row["TotalSavings"]
