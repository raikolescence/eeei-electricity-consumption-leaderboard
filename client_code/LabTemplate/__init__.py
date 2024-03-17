from ._anvil_designer import LabTemplateTemplate
from anvil import *
import plotly.graph_objects as go
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class LabTemplate(LabTemplateTemplate):
  def __init__(self, which_lab, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    # Any code you write here will run before the form opens.

    # # iFrame, plot thing
    # media_obj = anvil.server.call('make_plot')
    # self.iframe_1.url = media_obj.get_url(True)

    
    lab_row = anvil.server.call('get_lab_row', which_lab)
    print(which_lab)

    
    match_data = anvil.server.call('get_match_data', which_lab)
    self.match_history_panel.items = match_data

    
    self.lab_name.text = lab_row["name"]
    self.lab_acronym.text = lab_row["acronym"]
    self.lab_description.content = lab_row["description"]
    self.lab_image.source = lab_row["logo"]

    
    self.main_stats.text = "Main Stats"
    self.match_history.text = "Match History"
    self.laboratory_details.visible = True
    self.laboratory_history.visible = False

    
    self.main_stats.background = app.theme_colors['Primary Container']
    self.match_history.background = "transparent"
    
    

  def main_stats_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.laboratory_details.visible = True
    self.laboratory_history.visible = False

    self.main_stats.background = app.theme_colors['Primary Container']
    self.match_history.background = "transparent"

  def match_history_click(self, **event_args):
    """This method is called when the button is clicked"""
    
    self.laboratory_details.visible = False
    self.laboratory_history.visible = True
    
    self.match_history.background = app.theme_colors['Primary Container']
    self.main_stats.background = "transparent"
