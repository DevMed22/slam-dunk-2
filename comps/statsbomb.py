#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 09:10:33 2020

@author: davsu428
"""

# print("hello world")

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Arc
from statsbombpy import sb 
from mplsoccer.pitch import Pitch,VerticalPitch
from highlight_text import fig_text

com = sb.competitions()

com_name = com['competition_name']
com_id = com['competition_id']
season_name = com['season_name']
season_id = com['season_id']

com_dict = dict(zip(com_name,com_id))
season_dict = dict(zip(season_name,season_id))

def get_comp(season, comp):
  print(comp, season)
  x=sb.matches(competition_id=com_dict[comp], season_id=season_dict[season])
  
  return x


def matches_id(data):
  match_id=[]
  match_name=[]
  match_index=np.arange(0,len(data))
  for i in range(len(data)):
    match_id.append(data['match_id'][i])
    match_name.append(data['home_team'][i]+' vs '+data['away_team'][i]+' '+data['competition_stage'][i])
  match_dict_id = dict(zip(match_name,match_id))
  match_dict_index = dict(zip(match_name,match_index))
  return match_name,match_dict_index,match_dict_id





def match_data(data,match_index):
  home_team = data['home_team'][match_index]
  away_team = data['away_team'][match_index]
  home_score = data['home_score'][match_index]
  away_score = data['away_score'][match_index]
  stadium = data['stadium'][match_index]
  home_maneger = data['home_managers'][match_index]
  away_maneger = data['away_managers'][match_index]
  comp_stats = data['competition_stage'][match_index]
  return home_team,away_team,home_score,away_score,stadium,home_maneger,away_maneger,comp_stats





















