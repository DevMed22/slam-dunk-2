# -*- coding: utf-8 -*-
"""
Created on Sat Oct  1 01:23:21 2022

@author: Ahmed Tarek """
import streamlit as st
import pandas as pd

'''  male player features needed :
    short_name , overall, club_position,age , club_name ,  pace , 
shooting ,passing , dribbling , defending ,physic
'''
m_players = pd.read_csv('players_22.csv')
player_id, player_name = []
for i in range(len(m_players)):
    player_name.append(m_players['short_name'][i])
    player_id.append(i)
m_players_dict = dict(zip(player_id, player_name))
'''  male player features needed :
    short_name , overall, player_positions , age ,  pace , 
shooting ,passing , dribbling , defending ,physic
'''
f_players = pd.read_csv('female_players_22.csv')
f_player_id, f_player_name = []
for i in range(len(m_players)):
    f_player_name.append(f_players['short_name'][i])
    f_player_id.append(i)
f_players_dict = dict(zip(f_player_id, f_player_name))

## App
st.title('Discover stats of your favourite player 🏃‍♂️🤸‍♀️')
gender = st.selectbox('Player gender', ('Male', 'Female'))
if gender == 'Male':
    player = st.selectbox('Player name', player_name)
    st.write(f'Player name : {player}')
    st.write(f"overall rank : {m_players['overall'][i]}")
elif gender == 'Female':
    player = st.selectbox('Player name', player_name)
    st.write(f'Player name : {player}')
    st.write(f"overall rank : {f_players['overall'][i]}")
