import pandas as pd
import streamlit as st
import datetime as dt

st.markdown('# Keep track of Krillion Daily Deep Dive Scores 🦐')

st.session_state.date = dt.date.today()


data = pd.DataFrame(data={'Al-Ameen':[330], 'Jamie':[335], 'Millie':[410], 'Noah':[335]}, index=[st.session_state.date])

st.subheader("Current Scores")
if 'my_df' not in st.session_state:
    st.session_state['my_df'] = data
st.dataframe(st.session_state['my_df'],width='stretch')


last_idx = st.session_state['my_df'].index[-1]
st.subheader("Add new scores")
form = st.form(key='match')
with form:
    user = st.selectbox("Choose Player", ('Al-Ameen', 'Jamie', 'Millie', 'Noah'))
    score = st.text_input("Today's Score")
    submit = st.form_submit_button('Submit')
    if submit:
        df = st.session_state['my_df']

        if not pd.isnull(df[user].iloc[-1]):
            empty_row = pd.DataFrame(
                {col:[None] for col in df.columns},index=[st.session_state.date]
            )
            df = pd.concat([df,empty_row], ignore_index=True)
        df.loc[df.index[-1],user]=float(score)
        st.session_state['my_df'] = df


st.subheader('Updated Scores')
st.dataframe(st.session_state['my_df'], width='stretch', key='updated_scores')



todays_results = st.session_state['my_df'].loc[st.session_state['my_df'].index[-1]].to_dict()


