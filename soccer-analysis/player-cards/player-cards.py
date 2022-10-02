# -- coding: utf-8 --
"""
Created on Sat Oct  1 01:23:21 2022

@author: Ahmed Tarek """
import streamlit as st
import pandas as pd


m_players = pd.read_csv('players_22.csv')
player_id = []
player_name = []
for i in range(len(m_players)):
    player_name.append(m_players['short_name'][i])
    player_id.append(i)
m_players_dict = dict(zip(player_name, player_id))

f_players = pd.read_csv('female_players_22.csv')
f_player_id = []
f_player_name = []
for i in range(len(f_players)):
    f_player_name.append(f_players['short_name'][i])
    f_player_id.append(i)
f_players_dict = dict(zip(f_player_name, f_player_id))

## App
st.title('Discover stats of your favourite player 🏃‍♂️🤸‍♀️')
gender = st.selectbox('Player gender', ('Male', 'Female'))
if gender == 'Male':
    player = st.selectbox('Player name', player_name)
    st.write(f'Player name : {player}')
    st.write(f"overall rank : {m_players['overall'][m_players_dict[player]]}")
    st.write(f"Position : {m_players['club_position'][m_players_dict[player]]}")
    st.write(f"Age : {m_players['age'][m_players_dict[player]]}")
    st.write(f"Club : {m_players['club_name'][m_players_dict[player]]}")
    st.write(f"PAC: {m_players['pace'][m_players_dict[player]]}")
    st.write(f"Shooting : {m_players['shooting'][m_players_dict[player]]}")
    st.write(f"Passing : {m_players['passing'][m_players_dict[player]]}")
    st.write(f"Dribbling: {m_players['dribbling'][m_players_dict[player]]}")
    st.write(f"Defending : {m_players['defending'][m_players_dict[player]]}")
    st.write(f"Physic: {m_players['physic'][m_players_dict[player]]}")
elif gender == 'Female':
    player = st.selectbox('Female Player name', f_player_name)
    st.write(f'Player name : {player}')
    st.write(f"overall rank : {f_players['overall'][f_players_dict[player]]}")
    st.write(f"Position : {f_players['player_positions'][f_players_dict[player]]}")
    st.write(f"Age : {f_players['age'][f_players_dict[player]]}")
    st.write(f"PAC: {f_players['pace'][f_players_dict[player]]}")
    st.write(f"Shooting : {f_players['shooting'][f_players_dict[player]]}")
    st.write(f"Passing : {f_players['passing'][f_players_dict[player]]}")
    st.write(f"Dribbling: {f_players['dribbling'][f_players_dict[player]]}")
    st.write(f"Defending : {f_players['defending'][f_players_dict[player]]}")
    st.write(f"Physic: {f_players['physic'][f_players_dict[player]]}")