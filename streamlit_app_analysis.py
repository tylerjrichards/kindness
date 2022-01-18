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
    y=alt.Y('Actor', sort='-x'),
    x='count(Actor)',
    tooltip=[alt.Tooltip('Actor')]
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
    y=alt.Y('Acting Person', sort='-x'),
    x='count(Acting Person)',
    tooltip=[alt.Tooltip('Acting Person')]
    )
st.altair_chart(fam_chart, use_container_width=True)


st.write("""
    Parents and wives absolutely dominate here. The only surprise
    to me here is that stepfathers make it, but when I listened to
    the pseudonymous account Modest Proposal's reason, it starts to make
    sense.""")
st.info("""

    "My parents divorced when I was about six months old ... and she started
    dating a guy who ultimately became my stepfather. I always appreciated how
    incredibly generous and amazing he was to support us when we weren't his
    kids, and to take us on at that age when he was a grad student and
    didn't have a full-time income yet ... and for him to have done it and
    provide me and my siblings with the opportunity that we got ...
    in retrospect it's just the magnitude of that."
    """)
st.write("""

    The same sentiment about step-fathers is repeated by Brad Katsuyama
    (the protagonist in Flash Boys), when he said:""")
st.info("""

    "... so when I was four years old, my parents got divorced but remained
    friends. And my stepfather came in and started living with us when I was
    like five years old... And I think I look back, especially now I have
    three kids now, Brandon's seven, Rylan is five, and Emmy is turning
     two. And I just can't imagine going into a situation with someone else's
     children and making them feel like this is the way life should be.
     And I've never known a different life. What's interesting though is
     my wife, now you're going to get me all emotional here. My wife has
     said I have so many attributes of my stepfather. Oh my God. Can we cut?"

    """)
st.subheader("What Do People Mention?")
st.write("""
    While doing this project, i've heard quite a few incredibly shitty
    definitions of kindness. There is really only one that I've felt is
    useful while also is true to what Patrick probably means when he asks
    this question to his guests.
    """)
st.info("""
    Kindness is the sincere and voluntary use of one’s time, talent,
    and resources to better the lives of others, one’s own life, and
    the world through genuine acts of love, compassion, generosity, and
    service.
    """)
st.write("""
    The only thing I would add here is that kindness needs
    to be done without the expectation of repayment. If I loan you
    $1000, I'm not doing that to be kind even if it helps you kickstart
    your lemonade stand. This means, under that definition, any investment
    would not really be an act of kindness as there are expected returns.

    Now, I've broken down the podcast responses into
    a few categories. Note: there are lots of grey areas between these
    categories, but this is the best I could figure out!
    """)
test_chart2 = alt.Chart(df_actions, height=400,
                        title='Kind Action Breakdown').mark_bar().encode(
    y=alt.Y('Action', sort='-x'),
    x=alt.X('count(Action):Q'),
    tooltip=[alt.Tooltip('Action')]
    ).interactive()
st.altair_chart(test_chart2, use_container_width=True)
st.markdown('#### The "Took a chance" Category')
st.write("""
    The category where someone took a chance on others was far and away
    the most popular one. Often, this in when folks take the time to see
    the potential in you long before anyone else. there are a few key
    situations where this can happen.

    1. Investment via the 'first check'. Roughly a quarter of the
    'took a chance'segment are when an investor or firm believed
    in the vision of the entrepreneur enough to finance their effort.
    2. Another quarter of this segment came from hiring. Often this involved
    a recruiter or other employee advocating to give someone a job they
    might not be completely qualified for, where their enthusiasm was greater
    than their conpetence (as Charlie Songhurst, head of Strategy for Microsoft
    and incredible investor put it).
    3. There were three people who mentioned the 'Pay it forward' nature of
    Silicon Valley where people were extremely generous with advice or help,
    with little to no expectation of anything in return.
    [Alex Danco](www.alexdanco.com) often blogs about this (especially
    pre-covid), saying that there are social status gains to helping
    entrepreneurs through angel investing or advice unique to the Bay Area,
    [saying:](https://alexdanco.com/2019/11/27/the-social-subsidy-of-angel-investing/)
    """)
st.info("""
    The Bay Area tech ecosystem has been so successful that startup-related
    news has become the principal determinant of social status in San
    Francisco. In other cities, you acquire and flex social status by joining
    exclusive neighbourhoods or country clubs, or through philanthropic
    gestures, or even something as simple as what car you drive. In San
    Francisco, it’s angel investing. Other than founding a successful startup
    yourself, there’s not much higher-status in the Bay Area than backing
    founders that go on to build Uber or Stripe.
    """)

st.write("""
    I think this is true for both angel investing (and the
    company/investor-flirtation period before angel investing) and just the
    propensity to answer a cold email or  or starting
    a company with a peer. Max Levchin and Alex Rampell (founders of Affirm)
    met via random cold email, Elad Gil (famous investor and operator) credits
    a thousand small acts of kindness in the Valley for his success.
    """)
st.markdown('#### Other Notes:')
st.write("""
    I was quite unsurprised with the next few popular mentions, support,
    mentorship, help in time of need, and sacrifice meet my own expectations
    for placement.
    The surprise to me above was critique, which was a little distinct but
    connected to mentorship, and involved people getting fired Support and mentorship unsurprisingly



    """)
st.markdown('#### Platform Promotion')
st.write("""
    There were 3 interviewees who have (Jeremy Grantham, Ben Thompson
    of Stratechery fame, Michael Kitces)


    """)

df_doubled_up = df.dropna(subset=['Actor', 'Action'])
df_doubled_up['actor_action_combo'] = df_doubled_up['Actor'] + \
    '-' + df_doubled_up['Action']
st.write(df_doubled_up['actor_action_combo'].value_counts())

"""
Definitions:
Peer vs friend: peer needs to be someone in the same field with a connection that is non-business related. A friend here usually has no real connection in industry. If someone is a peer and a friend, I looked at the act of kindness to define the acting person.
"""
