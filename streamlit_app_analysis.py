"""module docstring"""
import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

"""
For the past couple years, I have listened to hundreds of hours of
a podcast called [Invest Like the Best](), run by an investor/asset manager/
public intellectual named Patrick O'Shaughnessy. The podcast is a bunch
of fun because of the combination of great topics (everything from Costco to
Facebook to crypto), guests, and interviewing style, and my favorite part is
almost always the final question of each podcast where Patrick asks the interviewee
what is the kindest thing anyone has ever done for them.

People's answers to this say a lot about them; some people mention
the action that gave them the biggest 'leg up' in life
or business, while others chose actions that took the most effort or
sacrifice from the other party. People mention their parents, bosses,
exes, and strangers, people who fired them, hired them, invested in them, or
raised them.

I spent some time scraping the last 260 podcasts and going through the
time intensive process of labeling each one, discovering who people
mention when answering the question, and what the action was. Why?
In part because I just was curious, but in the end I learned what this
subset of people appreciated in aggregate, which encourages my own
behavior changes. May we all strive to be kinder to each other in
the very ways that others find the most kind! On to the analysis.
"""
st.subheader('Who Do People Mention?')
st.write("""
    Below is a breakdown of who the person was doing the kindness. I had to
    Take some liberties in these definitions (e.g. I separated Family and Wife
    by the classic family you choose vs family you don't choose principle). I
    put the trickier definitions down at the bottom.
    """)

df = pd.read_csv('itlb_responses.csv')
family_member_list = ['Father', 'Mother', 'Parents',
                      'Family', 'Stepfather', 'Parent',
                      'Grandmother', 'Uncle', 'Grandfather']
df['Actor'] = df['Acting Person']
df['Actor'] = np.where(
    df['Acting Person'].isin(family_member_list),
    'Family', df['Acting Person'])

df_clean = df.dropna(subset=['Actor'])
top_actors = df_clean['Actor'].value_counts().index[0:15].tolist()
df_clean = df_clean[df_clean['Actor'].isin(top_actors)]
test_chart = alt.Chart(df_clean,
                       title='Kind Actor Breakdown',
                       height=400).mark_bar().encode(
    x=alt.X('Actor', sort='-y'),
    y='count(Actor)'
    )
st.altair_chart(test_chart, use_container_width=True)
df_actions = df.dropna(subset=['Action'])
top_actions = df_actions['Action'].value_counts().index[0:14].tolist()
df_actions = df_actions[df_actions['Action'].isin(top_actions)]

st.write("""
     A few things that were surprising to me were:

     1. Husbands were never mentioned, probably because the podcasts guests are
     mostly straight dudes.
     2. Doctors, Coaches, Teachers, and Investors were the only professions to
      make it on the list. I wasn't expecting Doctors to be on there at all!
     3. The majority of the non-family actors were in a position of
     power or influence over the interviewee (e.g. investor, boss, doctor).
     Neighbors, peers, strangers, friends were the exception to this.
    """
        )
st.write("""
    When we break down the family members (this time lumping in
    spouses as well), we get this graph.
    """)
family_member_list.append('Wife')
df_family = df_clean[df_clean['Acting Person'].isin(family_member_list)]

fam_chart = alt.Chart(df_family, height=400,
                      title='Family Breakdown').mark_bar().encode(
    x=alt.X('Acting Person', sort='-y'),
    y='count(Acting Person)'
    )
st.altair_chart(fam_chart, use_container_width=True)

test_chart2 = alt.Chart(df_actions, height=400,
                        title='Kind Action Breakdown').mark_bar().encode(
    x=alt.X('Action', sort='-y'),
    y='count(Action)'
    )
st.altair_chart(test_chart2, use_container_width=True)


"""
Definitions:
Peer vs friend: peer needs to be someone in the same field with a connection that is non-business related. A friend here usually has no real connection in industry. If someone is a peer and a friend, I looked at the act of kindness to define the acting person.
"""
