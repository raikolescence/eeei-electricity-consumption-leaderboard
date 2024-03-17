from ._anvil_designer import ItemTemplate2Template
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

from ...Frame import which_lab

class ItemTemplate2(ItemTemplate2Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    
    self.label_battle_time.text = self.item['battle_time']
    
    if self.item['participant1'] == which_lab:
      self.label_enemy_name.text = self.item['participant2']
      self.label_enemy_score.text = self.item['participant2_score']
      self.label_your_score.text = self.item['participant1_score']
    else:
      self.label_enemy_name.text = self.item['participant1']
      self.label_enemy_score.text = self.item['participant1_score']
      self.label_your_score.text = self.item['participant2_score']      

    if self.item['battle_winner'] == which_lab:
      self.label_win_status.text = "VICTORY"
    else:
      self.label_win_status.text = "DEFEAT"
  
    # Any code you write here will run before the form opens.
