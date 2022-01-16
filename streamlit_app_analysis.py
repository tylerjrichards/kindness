"""module docstring"""
import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

"""
For the past couple years, I have listened to hundreds of hours of a podcast called Invest Like the Best, run by an investor/asset manager/public intellectual named Patrick O'Shaughnessy. The podcast is a bunch of fun because of the combination of great topics (everything from Costco to Facebook to crypto), guests, and interviewing style, and my favorite part is almost always the final question of each podcast where Patrick asks the interviewee what the kindest thing anyone has ever done for them.
I thought people's answers always said a lot about them; some people mentioned the action that gave them the most perceived 'leg up'in life or business, while others chose actions that took the most effort or sacrifice. People mentioned their parents, bosses, wives, and strangers, people who fired them, hired them, invested in them, and

could not be  others mentioned the action that .  be
Kindness is a tricky thing to define,

Definitions:
Peer vs friend: peer needs to be someone in the same field with a connection that is non-business related. A friend here usually has no real connection in industry. If someone is a peer and a friend, I looked at the act of kindness to define the acting person.

"""

df = pd.read_csv('itlb_responses.csv')


st.write(df['Acting Person'].value_counts())

st.write(df['Action'].value_counts())

family_member_list = ['Father', 'Mother', 'Parents',
                      'Family', 'Stepfather', 'Parent',
                      'Grandmother', 'Uncle', 'Grandfather']
df['acting_person_clean'] = df['Acting Person']
df['acting_person_clean'] = np.where(
    df['Acting Person'].isin(family_member_list),
    'Family', df['Acting Person'])

df_grouped = df.groupby('acting_person_clean').count().reset_index()
st.write(df_grouped)
#alt.Chart()
st.write(df['acting_person_clean'].value_counts())
