from ._anvil_designer import FrameTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

from ..Home import Home
from ..Leaderboard import Leaderboard
from ..LabTemplate import LabTemplate
from ..About import About
from ..Graph import Graph

global which_lab
which_lab = ""

print(which_lab, "which lab")

class Frame(FrameTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    
    # Any code you write here will run before the form opens.
    #Clear the content panel and add the active Form
    self.content_panel.clear()
    self.content_panel.add_component(Home())
    #Change the color of the button to indicate that the page has been selected
    self.update_buttons(self.home_button)

  # update the color of the buttons, based on which button is currently active
  def update_buttons(self, active_button):
    buttons = [
      self.home_button,
      self.about_button,
      self.cnl_button,
      self.dspl_button,
      self.erml_button,
      self.microlab_button,
      self.pel_button,
      self.pssl_button,
      self.ral_button,
      self.sgrc_button,
      self.solar_button,
      self.ssl_button,
      self.ucl_button,
      self.wcel_button,
      self.leaderboard_button,
      self.graph_button,
      ]
    for button in buttons:
      button.background = "transparent"
    active_button.background = app.theme_colors['Primary Container']

  def home_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    #Clear the content panel and add the active Form
    self.content_panel.clear()
    self.content_panel.add_component(Home())
    #Change the color of the button to indicate that the page has been selected
    self.update_buttons(self.home_button)

  
  def leaderboard_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    #Clear the content panel and add the active Form
    self.content_panel.clear()
    self.content_panel.add_component(Leaderboard())
    #Change the color of the button to indicate that the page has been selected
    self.update_buttons(self.leaderboard_button)


  def graph_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    #Clear the content panel and add the active Form
    self.content_panel.clear()
    self.content_panel.add_component(Graph())
    #Change the color of the button to indicate that the page has been selected
    self.update_buttons(self.graph_button)


  def about_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    #Clear the content panel and add the active Form
    self.content_panel.clear()
    self.content_panel.add_component(About())
    self.update_buttons(self.about_button)

  def cnl_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    #Clear the content panel and add the active Form
    self.content_panel.clear()
    global which_lab
    which_lab = "COMPUTER NETWORKS LABORATORY"
    self.content_panel.add_component(LabTemplate(which_lab))
    self.update_buttons(self.cnl_button)

  def dspl_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    #Clear the content panel and add the active Form
    self.content_panel.clear()
    global which_lab
    which_lab = "Digital Signal Processing Laboratory"
    self.content_panel.add_component(LabTemplate(which_lab))
    self.update_buttons(self.dspl_button)

  def erml_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    #Clear the content panel and add the active Form
    self.content_panel.clear()
    global which_lab
    which_lab = "Electricity Market Research Laboratory"
    self.content_panel.add_component(LabTemplate(which_lab))
    self.update_buttons(self.erml_button)

  def microlab_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    #Clear the content panel and add the active Form
    self.content_panel.clear()
    global which_lab
    which_lab = "Microelectronics and Microprocessors Laboratory"
    self.content_panel.add_component(LabTemplate(which_lab))
    self.update_buttons(self.microlab_button)

  def pel_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    #Clear the content panel and add the active Form
    self.content_panel.clear()
    global which_lab
    which_lab = "Artesyn-Power Electronics Laboratory"
    self.content_panel.add_component(LabTemplate(which_lab))
    self.update_buttons(self.pel_button)

  def pssl_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    #Clear the content panel and add the active Form
    self.content_panel.clear()
    global which_lab
    which_lab = "Power Systems Simulation Laboratory"
    self.content_panel.add_component(LabTemplate(which_lab))
    self.update_buttons(self.pssl_button)

  def ral_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    #Clear the content panel and add the active Form
    self.content_panel.clear()
    global which_lab
    which_lab = "Robotics Automation Laboratory"
    self.content_panel.add_component(LabTemplate(which_lab))
    self.update_buttons(self.ral_button)

  def sgrc_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    #Clear the content panel and add the active Form
    self.content_panel.clear()
    global which_lab
    which_lab = "Smart Grid Research Center"
    self.content_panel.add_component(LabTemplate(which_lab))
    self.update_buttons(self.sgrc_button)

  def solar_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    #Clear the content panel and add the active Form
    self.content_panel.clear()
    global which_lab
    which_lab = "Solar Photovoltaics Laboratory"
    self.content_panel.add_component(LabTemplate(which_lab))
    self.update_buttons(self.solar_button)

  def ssl_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    #Clear the content panel and add the active Form
    self.content_panel.clear()
    global which_lab
    which_lab = "Smart Systems Laboratory"
    self.content_panel.add_component(LabTemplate(which_lab))
    self.update_buttons(self.ssl_button)

  def ucl_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    #Clear the content panel and add the active Form
    self.content_panel.clear()
    global which_lab
    which_lab = "Ubiquitous Computing Laboratory"
    print(which_lab, "which lab")
    self.content_panel.add_component(LabTemplate(which_lab))
    self.update_buttons(self.ucl_button)

  def wcel_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    #Clear the content panel and add the active Form
    self.content_panel.clear()
    global which_lab
    which_lab = "Wireless Communications Engineering Laboratory"
    self.content_panel.add_component(LabTemplate(which_lab))
    self.update_buttons(self.wcel_button)

  def test_click(self, **event_args):
    """This method is called when the button is clicked"""
    # anvil.server.call('get_leaderboard_order_too')
    # anvil.server.call('get_match_data', "Smart Systems Laboratory")
    anvil.server.call('update_weekly_database')