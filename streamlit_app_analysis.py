"""module docstring"""
import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

st.title('On Kindness')
st.subheader('By [Tyler Richards](https://www.twitter.com/tylerjrichards)')

"""
For the past couple years, I have listened to hundreds of hours of
a podcast called
[Invest Like the Best](https://open.spotify.com/show/22fi0RqfoBACCuQDv97wFO),
run by an investor/asset manager/public
intellectual named Patrick O'Shaughnessy. The podcast is a bunch
of fun because of the combination of great topics (everything from Costco to
Facebook to crypto), guests, and interviewing style, and my favorite part is
almost always the final question of each podcast where Patrick asks
the interviewee what is the kindest thing anyone has ever done for them.

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
    I think this is true for angel investing/the
    company/investor-flirtation period before angel investing and just the
    propensity to answer a cold email.
    Max Levchin and Alex Rampell (founders of Affirm)
    met via random cold email, Elad Gil (famous investor and operator) credits
    a thousand small acts of kindness in the Valley for his success. I
    have at least a 50 percent hit rate on cold emails since I started in
    tech, and quite a few of the opportunities I had came from cold emails!
    """)
st.markdown('#### Other Notes:')
st.write("""
    I was quite unsurprised with the next few popular mentions, support,
    mentorship, help in time of need, and sacrifice meet my own expectations
    for placement.

    The surprise to me above was critique, which was a little distinct but
    connected to mentorship, and involved people getting fired (David Tisch
    described his firing experience as 'aggressive'), teachers
    giving poor grades, and friends convincing others to get their shit
    together. These are, in my view, the other side of the 'Took a chance'
    coin in that they often push folks to be more ambitious or dedicated, but
    I would have never expected to see as many as I did here.

    The Immigration stories in this bunch are some of my favorites, they are
    often similar to sacrifice acts of kindness, but were distinct enough to
    deserve their own category. For example, from Jeff Ma of the famous MIT
    Blackjack team:



    """)
st.info("""
    "I think anyone that's born of immigrant parents, who came here basically
    to make their kids have a better life, their answer has to be their
    parents. My dad and mom came here from Taiwan. They were originally from
    China. When the communists took over, my dad, they never had cable in
    their lives. If you talk about a great lesson about compounding, my dad
    was a professor, my mom was a nurse anesthetist. Great jobs, but none of
    them are what you would consider to be jobs that would set you up for the
    rest of your life in terms of... but they never had cable. The only money
    they really ever spent was on our education. Both my sisters and I went
    to Phillips Exeter Academy and then to MIT. So that's not a cheap amount
    of money at that level... So I think clearly, my dad and my mom
    would be my answer. That's the easy answer."
    """)
st.markdown('#### Actor Action Combo Breakdown')
st.write("""
    The last question I had was, what are the most popular actor-action
    combinations?
    """)

df_doubled_up = df.dropna(subset=['Actor', 'Action'])
df_doubled_up['actor_action_combo'] = df_doubled_up['Actor'] + \
    '-' + df_doubled_up['Action']
top_combos = df_doubled_up['actor_action_combo'].value_counts()\
    .index[0:18].tolist()
df_combos = df_doubled_up[df_doubled_up['actor_action_combo']
    .isin(top_combos)]
combo_chart2 = alt.Chart(df_combos, height=400,
                         title='Combo Breakdown').mark_bar().encode(
    y=alt.Y('actor_action_combo', sort='-x'),
    x=alt.X('count(actor_action_combo)'),
    tooltip=[alt.Tooltip('actor_action_combo')]
    ).interactive()
st.altair_chart(combo_chart2, use_container_width=True)
st.write("""
    Families were most likely to be mentioned for support, upbringing,
    and sacrifice, Bosses and investment firms for taking a chance, wives for
    marriage, forgiveness (????) and sacrifice, and strangers for help in a
    time of need.
    It really was a blast reading through all these kind actions (even
    if it was slightly tedious!), I've included some of my favorites,
    along with interactive visualizations and the underlying data
    for the curious to look at if interested.
    """)

st.markdown("#### Tyler's Favorite Kind Actions")
st.write("""
    I've read and/or listened to each one of these 260 interviews, and
    below are my top 3 most surprising or interesting acts of kindness
    that I have yet to mention.



    """)
st.markdown("""##### Kobe Bryant's Words of Encouragement""")
st.info("""
    "I played basketball in high school and it turns out that I'm the same age
    as Kobe Bryant and his high school was like a mile away from mine...He was
    practicing with the Sixers in the summertime when he was a junior in
    high school. And you could just tell that he was going to go places.
    So our junior year, we're playing and the first time we played his
    high school, I had a terrible game. It was at home and I was like
    humiliated. He just owned the team, but I took a shot and I think
    he threw it to the other side of the court or something. I just
    played poorly...

    And as I was leaving, he was coming out of the visiting
    team's locker room. And he could see that I was not in the best condition.
    And he came over to me and said ... "You're a very good player. Don't be
    discouraged. I'm sure the next time we play, you're going to have a much
    better game."

    Even though we were peers, he was already looked at as a superstar.
    It was sort of like Michael Jordan telling that to you ... he really went
    out of his way to encourage me and to say very positive things about me
    when I was feeling very down about myself ... I'll never forget that
    because sometimes you feel obligated to do nice things. when you really
    don't have to do something to help someone else, but you do it anyway,
    even if it's small, to me, I think that has a great deal of value and
    stood out to me." - Geoffrey Batt

    """)
st.markdown("""##### Northern Ireland Neighbors""")

st.info("""
    "(This question) took me all the way back to growing up in Northern
    Ireland and when the first bomb went off in our local village. I grew
    up in this really small little village of about 1200 people. The
    local police barracks got blown up and it took out all the windows
    in the back of our house. We didn't live a particularly big house,
    all the windows in the back, my bedroom, the dining room, the kitchen,
    all the windows blew in. So, there's glass everywhere, it had been a
    pretty traumatizing day because I had been in primary school.
    So, I was probably about 10 and we'd all had to shelter on our desks.
    ... What was amazing in terms of an act of kind is the minute ... our
    neighbors came in, took a look and they went back out and they had
    figured out where they could go by plywood ... They came in and
    they boarded up all our windows. And I remember Marcella,
    the mom bringing us hot food cause our kitchen was a disaster.
    But what made that really poignant is the whole divide in Northern
    Ireland was religious. And we were Protestant and our door neighbors
    are Catholic. And so, technically we were meant to hate each other.
    That's why people were blowing up things. And yet the fact that kindness
    that they just came that night, I just have such a sense of warmth still
    because it was a brutal like a day you never forget in your life.
    That family still lives next door to my mom and dad." - Sarah Friar
    """)

st.markdown('#### Interactive Data Viz')
actor_x = st.selectbox('Choose an Actor, see a breakdown of Actions', df_clean['Actor'].unique())
df_selected = df_clean[df_clean['Actor'] == actor_x]
cols_to_keep = ['GUEST', 'SITE_URL', 'Introduction', 'Response',
                'Action', 'Actor']
df_selected = df_selected[cols_to_keep]
selected_chart = alt.Chart(df_selected, height=400,
                           title='Kind Action Breakdown for selection: {}'
                           .format(actor_x)).mark_bar().encode(
    y=alt.Y('Action', sort='-x'),
    x=alt.X('count(Action):Q'),
    tooltip=[alt.Tooltip('Action')]
    ).interactive()
st.altair_chart(selected_chart, use_container_width=True)
st.write("""
    Below are all the interviews for the actor you selected!
    """)
st.write(df_selected)

action_x = st.selectbox('Choose an Action, see a breakdown of Actors',
                        df_actions['Action'].unique())
df_selected_action = df_actions[df_actions['Action'] == action_x]
df_selected_action = df_selected_action[cols_to_keep]
selected_chart = alt.Chart(df_selected_action, height=400,
                           title='Kind Actor Breakdown for selection: {}'
                           .format(action_x)).mark_bar().encode(
    y=alt.Y('Actor', sort='-x'),
    x=alt.X('count(Actor):Q'),
    tooltip=[alt.Tooltip('Actor')]
    ).interactive()
st.altair_chart(selected_chart, use_container_width=True)
st.write("""
    Below are all the interviews for the action you selected!
    """)
st.write(df_selected_action)




"""
Definitions:
Peer vs friend: peer needs to be someone in the same field with a connection that is non-business related. A friend here usually has no real connection in industry. If someone is a peer and a friend, I looked at the act of kindness to define the acting person.
"""
