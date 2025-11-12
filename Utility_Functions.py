import uuid
import streamlit as st
from Backend import workflow
from Backend import checkpointer


def generate_thread_id():

    threads = str(uuid.uuid4())
    return threads

def reset_chat():
    thread_id = generate_thread_id()
    st.session_state['thread_id'] = thread_id

    if 'chat_threads' not in st.session_state:
        st.session_state['chat_threads'] = []

    add_threads(st.session_state['thread_id'])
    st.session_state['message_history'] = []


def add_threads(thread_id):
    if thread_id not in st.session_state['chat_threads']:
        return st.session_state['chat_threads'].append(thread_id)
    

def load_conversation(thread_id):
    state = workflow.get_state(config={'configurable': {'thread_id': thread_id}})
    # Use .get() to safely access the key
    return state.values.get('messages', [])

def delete_thread(thread_id):

    checkpointer.delete(config={'configurable': {'thread_id': thread_id}})

    if thread_id in st.session_state['chat_threads']:
        st.session_state['chat_threads'].remove(thread_id)

    if st.session_state.get('thread_id') == thread_id:
        st.session_state['thread_id'] = None
        st.session_state['message_history'] = []

