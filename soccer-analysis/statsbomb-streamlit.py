#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# # run the app using this line in commnands :streamlit run --theme.base "light" statsbomb.py

import streamlit as st
import matplotlib.pyplot as plt
from statsbombpy import sb
from mplsoccer.pitch import Pitch, VerticalPitch
from highlight_text import fig_text

## competitions 
com = sb.competitions()

com_name = com['competition_name']
com_id = com['competition_id']
season_name = com['season_name']
season_id = com['season_id']

com_dict = dict(zip(com_name, com_id))
season_dict = dict(zip(season_name, season_id))


## Matches
def matches_id(data):
    match_id = []
    match_name = []
    match_index = []
    for i in range(len(data)):
        match_index.append(i)
        match_id.append(data['match_id'][i])
        match_name.append(data['home_team'][i] + ' vs ' + data['away_team'][i] + ' ' + data['competition_stage'][i])
    match_dict_id = dict(zip(match_name, match_id))
    match_dict_index = dict(zip(match_name, match_index))
    return match_name, match_dict_index, match_dict_id


def match_data(data, match_index):
    home_team = data['home_team'][match_index]
    away_team = data['away_team'][match_index]
    home_score = data['home_score'][match_index]
    away_score = data['away_score'][match_index]
    stadium = data['stadium'][match_index]
    home_manager = data['home_managers'][match_index]
    away_manager = data['away_managers'][match_index]
    comp_stats = data['competition_stage'][match_index]
    return home_team, away_team, home_score, away_score, stadium, home_manager, away_manager, comp_stats


## Lineups
def lineups(h, w, data):
    home_lineups = []
    away_lineups = []
    for i in range(len(data)):
        home_lineups.append(data[h]['player_name'])
        away_lineups.append(data[w]['player_name'])
    return home_lineups[0].values, away_lineups[0].values


## events
def shots(events, h, w, match_id):
    fig, ax = plt.subplots(figsize=(13, 8.5))
    # The statsbomb pitch from mplsoccer
    pitch = Pitch(pitch_type='statsbomb', half=True,
                  pitch_color='grass', line_color='#c7d5cc', stripe=True)

    pitch.draw(ax=ax)

    # I invert the axis to make it so I am viewing it how I want
    plt.gca().invert_yaxis()

    # plot the points, you can use a for loop to plot the different outcomes if you want
    x_h = []
    y_h = []
    x_w = []
    y_w = []
    for i, shot in events['shots'].iterrows():
        if events['shots']['possession_team'][i] == h:
            x_h.append(shot['location'][0])
            y_h.append(shot['location'][1])
        elif events['shots']['possession_team'][i] == w:
            x_w.append(shot['location'][0])
            y_w.append(shot['location'][1])

    plt.scatter(x_h, y_h, s=100, c='red', alpha=.7)

    plt.scatter(x_w, y_w, s=100, c='blue', alpha=.7)

    total_shots = len(events['shots'])
    fig_text(s=f'Total Shots: {total_shots}',
             x=.49, y=.67, fontsize=14, color='white')

    fig.text(.22, .14, f'@ahmedtarek26 / Github', fontstyle='italic', fontsize=12,
             color='white')

    plt.savefig(f'graphs/shots-{match_id}.png', dpi=300, bbox_inches='tight', facecolor='#486F38')
    st.image(f'graphs/shots-{match_id}.png')


## Dripples
def dribbles(events, h, w, match_id):
    fig, ax = plt.subplots(figsize=(13, 8.5))
    fig.set_facecolor('#22312b')
    ax.patch.set_facecolor('#22312b')

    # The statsbomb pitch from mplsoccer
    pitch = Pitch(pitch_type='statsbomb',
                  pitch_color='grass', line_color='#c7d5cc', stripe=True)

    pitch.draw(ax=ax)

    # I invert the axis to make it so I am viewing it how I want
    plt.gca().invert_yaxis()

    # plot the points, you can use a for loop to plot the different outcomes if you want
    x_h = []
    y_h = []
    x_w = []
    y_w = []
    for i, shot in events['dribbles'].iterrows():
        if events['dribbles']['possession_team'][i] == h:
            x_h.append(shot['location'][0])
            y_h.append(shot['location'][1])
        elif events['dribbles']['possession_team'][i] == w:
            x_w.append(shot['location'][0])
            y_w.append(shot['location'][1])
    plt.scatter(x_h, y_h, s=100, c='red', alpha=.7)

    plt.scatter(x_w, y_w, s=100, c='blue', alpha=.7)

    total_shots = len(events['dribbles'])

    fig_text(s=f'Total Dribbles: {total_shots}',
             x=.49, y=.67, fontsize=14, color='white')

    fig.text(.22, .14, f'@ahmedtarek / Github', fontstyle='italic', fontsize=12,
             color='white')

    plt.savefig(f'graphs/dribbles-{match_id}.png', dpi=300, bbox_inches='tight', facecolor='#486F38')
    st.image(f'graphs/dribbles-{match_id}.png')


## passes
def home_team_passes(events, home_team, match_id):
    x_h = []
    y_h = []

    for i, shot in events['passes'].iterrows():
        if events['passes']['possession_team'][i] == home_team:
            x_h.append(shot['location'][0])
            y_h.append(shot['location'][1])

    pitch = Pitch(pitch_type='statsbomb', line_zorder=2, line_color='gray', pitch_color='#22312b')
    bins = (6, 4)

    fig, ax = pitch.draw(figsize=(16, 11), constrained_layout=True, tight_layout=False)
    fig_text(s=f'{home_team} Passes: {len(x_h)}',
             x=.49, y=.67, fontsize=14, color='yellow')
    fig.text(.22, .14, f'@ahmedtarek26 / Github', fontstyle='italic', fontsize=12, color='yellow')
    # plot the heatmap - darker colors = more passes originating from that square

    bs_heatmap = pitch.bin_statistic(x_h, y_h, statistic='count', bins=bins)
    hm = pitch.heatmap(bs_heatmap, ax=ax, cmap='Blues')
    plt.savefig(f'graphs/{home_team}passes-{match_id}.png', dpi=300, bbox_inches='tight')
    st.image(f'graphs/{home_team}passes-{match_id}.png')


def away_team_passes(events, away_team, match_id):
    x_w = []
    y_w = []
    for i, shot in events['dribbles'].iterrows():
        if events['dribbles']['possession_team'][i] == away_team:
            x_w.append(shot['location'][0])
            y_w.append(shot['location'][1])

    pitch = Pitch(pitch_type='statsbomb', line_zorder=2, line_color='gray', pitch_color='#22312b')
    bins = (6, 4)
    fig, ax = pitch.draw(figsize=(16, 11), constrained_layout=True, tight_layout=False)
    fig_text(s=f'{away_team} Passes: {len(x_w)}',
             x=.49, y=.67, fontsize=14, color='yellow')
    fig.text(.22, .14, f'@ahmedtarek26 / Github', fontstyle='italic', fontsize=12, color='yellow')
    fig.set_facecolor('#22312b')
    # plot the heatmap - darker colors = more passes originating from that square

    bs_heatmap = pitch.bin_statistic(x_w, y_w, statistic='count', bins=bins)
    hm = pitch.heatmap(bs_heatmap, ax=ax, cmap='Reds')
    plt.savefig(f'graphs/{away_team}passes-{match_id}.png', dpi=300, bbox_inches='tight')
    st.image(f'graphs/{away_team}passes-{match_id}.png')


## streamlit app
st.title('Discover the competition like couches 😉')
competition = st.selectbox('Choose the competition', (com_dict.keys()))

season = st.selectbox('Choose the season', (season_dict.keys()))
data = sb.matches(competition_id=com_dict[competition], season_id=season_dict[season])
matches_names, matches_idx, matches_id = matches_id(data)
match = st.selectbox('Select the match', matches_names)
sub_2 = st.button('Analyze')
if sub_2:
    home_team, away_team, home_score, away_score, stadium, home_manager, away_manager, comp_stats = match_data(
        data, matches_idx[match])
    home_lineup, away_lineup = lineups(home_team, away_team, data=sb.lineups(match_id=matches_id[match]))
    st.subheader(f'{home_team} {home_score} : {away_score} {away_team}')
    st.subheader(f'{home_team}')
    st.write(f'Goals: {home_score}')
    st.write(f'Manager: {home_manager}')
    st.write(f'Lineup:')
    st.write(f'{home_lineup}')
    st.subheader(f'{away_team}')
    st.write(f'Goals: {away_score}')
    st.write(f'Manager: {away_manager}')
    st.write(f'Lineup: {away_lineup}')

    # st.write(home_team, away_team, home_score, away_score, stadium, home_manager, away_manager, comp_stats)
    
    st.subheader(f'{stadium} Stadium')
    st.subheader(f'{comp_stats} Stage')

    # st.subheader('Lineups')
    # st.write(home_lineup, away_lineup)
    events = sb.events(match_id=matches_id[match], split=True, flatten_attrs=False)
    st.subheader(f'{home_team} shots vs {away_team} shots')
    shots(events, home_team, away_team, matches_id[match])
    st.subheader('Dribbles')
    dribbles(events, home_team, away_team, matches_id[match])
    st.subheader(f'{home_team} pass map')
    home_team_passes(events, home_team, matches_id[match])
    st.subheader(f'{away_team} pass map')
    home_team_passes(events, away_team, matches_id[match])