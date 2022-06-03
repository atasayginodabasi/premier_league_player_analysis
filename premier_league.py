import os
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import plotly.figure_factory as ff
import plotly.graph_objects as go
import numpy as np
import plotly.express as px

# Reading the data
print(os.listdir(r'C:/Users/ata-d/'))
data = pd.read_csv(r'C:/Users/ata-d/OneDrive/Masaüstü/ML/Datasets/EPL_20_21.csv')

data.isna().sum()

# ----------------------------------------------------------------------------------------------------------------------

# Top 10 Goal Kings
'''''''''
fig_bar = px.bar(data_frame=data.nlargest(10, 'Goals')[['Name', 'Goals']],
                 x='Name', y='Goals', color='Goals', text='Goals')
fig_bar.update_traces(marker=dict(line=dict(color='#000000', width=2)))
fig_bar.update_layout(title_text='Top 10 Goal Kings of the League',  # Main title for the project
                      title_x=0.5, title_font=dict(size=30))  # Location and the font size of the main title
fig_bar.update_traces(texttemplate='%{text:.2s}', textposition='outside')
fig_bar.show()
'''''''''

# Top 10 Assist Kings
'''''''''
fig_bar = px.bar(data_frame=data.nlargest(10, 'Assists')[['Name', 'Assists']],
                 x='Name', y='Assists', color='Assists', text='Assists')
fig_bar.update_traces(marker=dict(line=dict(color='#000000', width=2)))
fig_bar.update_layout(title_text='Top 10 Assist Kings of the League',  # Main title for the project
                      title_x=0.5, title_font=dict(size=30))  # Location and the font size of the main title
fig_bar.update_traces(texttemplate='%{text:.2s}', textposition='outside')
fig_bar.show()
'''''''''

# Top 10 DF Players that have the most Red Card
'''''''''
DF_players = data[data['Position'].str.contains("DF")]
DF_players_red = DF_players.nlargest(10, 'Red_Cards')[['Name', 'Red_Cards', 'Yellow_Cards']]
fig = px.bar(DF_players_red, x="Name", y=["Red_Cards", "Yellow_Cards"],
             color_discrete_map={
                 "Red_Cards": "red",
                 "Yellow_Cards": "yellow"}

             )
fig.update_layout(title_text='Top 10 DF Players that have the most Red Card',
                  title_x=0.5, title_font=dict(size=30))
fig.update_traces(marker=dict(line=dict(color='#000000', width=2)))
fig.show()
'''''''''

# Top 10 DF Players that have the most Yellow Card
'''''''''
DF_players_yellow = DF_players.nlargest(10, 'Yellow_Cards')[['Name', 'Red_Cards', 'Yellow_Cards']]
fig = px.bar(DF_players_yellow, x="Name", y=["Red_Cards", "Yellow_Cards"],
             color_discrete_map={
                 "Red_Cards": "red",
                 "Yellow_Cards": "yellow"}
             )
fig.update_layout(title_text='Top 10 DF Players that have the most Yellow Card',
                  title_x=0.5, title_font=dict(size=30))
fig.update_traces(marker=dict(line=dict(color='#000000', width=2)))
fig.show()
'''''''''

# Top 10 Players due to Ages
'''''''''
fig_bar = px.bar(data_frame=data.nlargest(10, 'Age')[['Name', 'Age']],
                 x='Name', y='Age', color='Age', text='Age')
fig_bar.update_traces(marker=dict(line=dict(color='#000000', width=2)))
fig_bar.update_layout(title_text='Top 10 Players due to Ages',  # Main title for the project
                      title_x=0.5, title_font=dict(size=30))  # Location and the font size of the main title
fig_bar.update_traces(texttemplate='%{text:.2s}', textposition='outside')
fig_bar.show()
'''''''''

# Density Plot of the Ages
'''''''''
plt.figure(figsize=(15, 8))
sns.distplot(data['Age'], hist=True, color='red')
plt.xlabel("Ages", fontsize=12)
plt.ylabel('Density', fontsize=12)
plt.title("Density Plot of the Ages", fontsize=16)
'''''''''

# Top 10 Players due to Passes Attempted
'''''''''
fig_bar = px.bar(data_frame=data.nlargest(10, 'Passes_Attempted')[['Name', 'Passes_Attempted']],
                 x='Name', y='Passes_Attempted', color='Passes_Attempted', text='Passes_Attempted')
fig_bar.update_traces(marker=dict(line=dict(color='#000000', width=2)))
fig_bar.update_layout(title_text='Top 10 Players due to Passes Attempted',  # Main title for the project
                      title_x=0.5, title_font=dict(size=30))  # Location and the font size of the main title
fig_bar.update_traces(texttemplate='%{text:.2s}', textposition='outside')
fig_bar.show()
'''''''''

# Top 10 Average Red and Yellow Cards due to Nationality
'''''''''
Nat_Card_avr = data.groupby(by=['Nationality']).mean()
Nat_Card_avr_top = Nat_Card_avr.nlargest(10, 'Red_Cards')[['Red_Cards', 'Yellow_Cards']]
fig = px.bar(Nat_Card_avr_top, x=Nat_Card_avr_top.index, y=["Red_Cards", "Yellow_Cards"],
             color_discrete_map={
                 "Red_Cards": "red",
                 "Yellow_Cards": "yellow"}

             )
fig.update_layout(title_text='Top 10 Average Red and Yellow Cards due to Nationality',
                  title_x=0.5, title_font=dict(size=30))
fig.update_traces(marker=dict(line=dict(color='#000000', width=2)))
fig.show()
'''''''''

# Top 25 Players due to Percentage of Passes Completed
'''''''''
fig_bar = px.bar(data_frame=data.nlargest(25, 'Perc_Passes_Completed')[['Name', 'Perc_Passes_Completed']],
                 x='Name', y='Perc_Passes_Completed', color='Perc_Passes_Completed', text='Perc_Passes_Completed')
fig_bar.update_traces(marker=dict(line=dict(color='#000000', width=2)))
fig_bar.update_layout(title_text='Top 25 Players due to Percentage of Passes Completed',
                      title_x=0.5, title_font=dict(size=30))
fig_bar.update_traces(texttemplate='%{text:.2s}', textposition='outside')
fig_bar.show()
'''''''''

# ----------------------------------------------------------------------------------------------------------------------

# Goals by the Teams
'''''''''
goalsbyteam = data['Goals'].groupby(data['Club']).sum().sort_values(ascending=False).to_frame()
fig = px.bar(data_frame=goalsbyteam, x=goalsbyteam.index, y='Goals', color='Goals')
fig.update_layout(title_text='Number of Goals by the Teams',
                  title_x=0.5, title_font=dict(size=30))
fig.update_layout(xaxis={'categoryorder': 'total descending'})
fig.update_traces(marker=dict(line=dict(color='#000000', width=2)))
fig.show()
'''''''''

# Number of Assists by the Teams
'''''''''
assistsbyteam = data['Assists'].groupby(data['Club']).sum().sort_values(ascending=False).to_frame()
fig = px.bar(data_frame=assistsbyteam, x=assistsbyteam.index, y='Assists', color='Assists')
fig.update_layout(title_text='Number of Assists by the Teams',
                  title_x=0.5, title_font=dict(size=30))
fig.update_layout(xaxis={'categoryorder': 'total descending'})
fig.update_traces(marker=dict(line=dict(color='#000000', width=2)))
fig.show()
'''''''''

# Number of Red Cards by the Teams
'''''''''
redcardbyteam = data['Red_Cards'].groupby(data['Club']).sum().sort_values(ascending=False).to_frame()
fig = px.bar(data_frame=redcardbyteam, x=redcardbyteam.index, y='Red_Cards', color='Red_Cards')
fig.update_layout(title_text='Number of Red Cards by the Teams',
                  title_x=0.5, title_font=dict(size=30))
fig.update_layout(xaxis={'categoryorder': 'total descending'})
fig.update_traces(marker=dict(line=dict(color='#000000', width=2)))
fig.show()
'''''''''

# Nationalities of the League
'''''''''
Nationality = data.groupby(pd.Grouper(key='Nationality')).size().reset_index(name='count')
fig = px.treemap(Nationality, path=['Nationality'], values='count')
fig.update_layout(title_text='Nationalities of the League',
                  title_x=0.5, title_font=dict(size=30)
                  )
fig.update_traces(textinfo="label+value")
fig.show()
'''''''''

# Number of Players for each Club
'''''''''
NumberofPlayers = data.groupby(pd.Grouper(key='Club')).size().reset_index(name='count')
fig = px.treemap(NumberofPlayers, path=['Club'], values='count')
fig.update_layout(title_text='Number of Players for each Club',
                  title_x=0.5, title_font=dict(size=30)
                  )
fig.update_traces(textinfo="label+value")
fig.show()
'''''''''

# Density Plot of the Matches and Starts
'''''''''
plt.figure(figsize=(15, 8))
sns.distplot(data['Matches'], color='red')
sns.distplot(data['Starts'], color='blue')
plt.xlabel("Matches and Starts", fontsize=12)
plt.ylabel('Density', fontsize=12)
plt.legend(['Matches', 'Starts'], loc='upper right')
plt.title("Density Plot of the Matches and Starts", fontsize=16)
'''''''''

# Distribution of the Goals
'''''''''
Grouped_NumofGoals = data.groupby(pd.Grouper(key='Goals')).size().reset_index(name='count')
labels = Grouped_NumofGoals['Goals'].values
values = Grouped_NumofGoals['count'].values

fig = go.Figure(data=[go.Pie(labels=labels, values=values, opacity=0.8)])
fig.update_traces(textinfo='percent+label', marker=dict(line=dict(color='#000000', width=2)))
fig.update_layout(title_text='Distribution of the Goals', title_x=0.5, title_font=dict(size=32))
fig.show()
'''''''''

# All Scored DF Players
'''''''''
DF_players_scored = data[data['Position'].str.contains("DF")]
DF_players_scored = DF_players_scored.drop(DF_players_scored.index[DF_players_scored['Goals'] == 0])
fig = px.bar(data_frame=DF_players_scored, x='Name', y='Goals', color='Goals')
fig.update_layout(title_text='Defenders with most goals!! (Wow!)',
                  title_x=0.5, title_font=dict(size=30))
fig.update_layout(xaxis={'categoryorder': 'total descending'})
fig.update_traces(marker=dict(line=dict(color='#000000', width=2)))
fig.show()
'''''''''

# Scored and Assisted GK Players
'''''''''
GK_players = data[data['Position'].str.contains("GK")]
GK_players_top = GK_players.nlargest(10, 'Goals')[['Name', 'Goals', 'Assists']]
fig = px.bar(GK_players_top, x="Name", y=["Goals", "Assists"],
             color_discrete_map={
                 "Red_Cards": "red",
                 "Yellow_Cards": "yellow"}

             )
fig.update_layout(title_text='Scored and Assisted GK Players',
                  title_x=0.5, title_font=dict(size=30))
fig.update_layout(xaxis={'categoryorder': 'total descending'})
fig.update_traces(marker=dict(line=dict(color='#000000', width=2)))
fig.show()
'''''''''

# Graph of Players who have the highest Penalty_Goals/Penalty_Attempted Ratio
'''''''''
PenaltyPerAttempted = pd.concat([data['Name'], 1/(data['Penalty_Attempted']/data['Penalty_Goals'])], axis=1)
PenaltyPerAttempted = PenaltyPerAttempted.replace([np.inf], np.nan).dropna(axis=0)
fig = px.bar(data_frame=PenaltyPerAttempted, x='Name', y=0, color=0)
fig.update_layout(title_text='Graph of Players who have the highest Penalty_Goals/Penalty_Attempted Ratio',
                  title_x=0.5, title_font=dict(size=30))
fig.update_layout(xaxis={'categoryorder': 'total descending'})
fig.update_traces(marker=dict(line=dict(color='#000000', width=2)))
fig.show()
'''''''''

# Correlation Graph
'''''''''
plt.figure(figsize=(15, 8))
correlation = sns.heatmap(data.corr(), vmin=-1, vmax=1, annot=True, linewidths=1, linecolor='black')
correlation.set_title('Correlation Graph of the Dataset', fontdict={'fontsize': 24})
'''''''''
