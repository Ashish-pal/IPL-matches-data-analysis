#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt


ipl = pd.read_csv('C:\\Users\\ashish\\Documents\\Python DS project\\iplmatches\\gmatches.csv')


ipl.head()


ipl.info

ipl.describe(include='all')


ipl.shape

ipl['player_of_match'].value_counts()

ipl['player_of_match'].value_counts()[0:10]


ipl['player_of_match'].value_counts()[0:5]

plt.figure(figsize=(10,8))
plt.bar(list(ipl['player_of_match'].value_counts()[0:10].keys()),list(ipl['player_of_match'].value_counts()[0:10]),color='g')
plt.show


ipl['result'].value_counts()


ipl['toss_winner'].value_counts()

batting_first=ipl[ipl['win_by_runs']!=0]


batting_first.head()


plt.figure(figsize=(10,8))
plt.hist(batting_first['win_by_runs'])
plt.show


batting_first['winner'].value_counts()


plt.figure(figsize=(10,8))
plt.bar(list(batting_first['winner'].value_counts()[0:10].keys()), list(batting_first['winner'].value_counts()[0:10]),color=["blue","yellow","orange"])
plt.show


plt.figure(figsize=(10,10))
plt.pie(list(batting_first['winner'].value_counts()),labels=list(batting_first['winner'].value_counts().keys()),autopct='%0.1f%%')
plt.show

batting_second=ipl[ipl['win_by_wickets']!=0]


batting_second.head()

plt.figure(figsize=(10,10))
plt.hist(batting_second['win_by_wickets'],bins=30)
plt.show

batting_second['winner'].value_counts()

plt.figure(figsize=(10,10))
plt.bar(list(batting_second['winner'].value_counts()[0:10].keys()),list(batting_second['winner'].value_counts()[0:10]),color=["blue","red","yellow","green"])
plt.show

plt.figure(figsize=(10,10))
plt.pie(list(batting_second['winner'].value_counts()),labels=list(batting_second['winner'].value_counts().keys()),autopct="%0.1f%%")
plt.show


ipl['season'].value_counts()

ipl['city'].value_counts()


import numpy as np


np.sum(ipl['toss_winner']==ipl['winner'])


393/756





