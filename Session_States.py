import streamlit as st
from Utility_Functions import generate_thread_id, add_threads
from Backend_Functions import retrieve_all_threads


def init_session_state():
    
    if 'message_history' not in st.session_state:
        st.session_state['message_history'] = []

    if 'thread_id' not in st.session_state:
        st.session_state['thread_id'] = generate_thread_id()

    if 'chat_threads' not in st.session_state:
        st.session_state['chat_threads'] = retrieve_all_threads()

        add_threads(st.session_state['thread_id'])

    if 'delete_thread' not in st.session_state:
        st.session_state['delete_thread'] = None

