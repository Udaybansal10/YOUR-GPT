import streamlit as st
from Utility_Functions import reset_chat, load_conversation, delete_thread
from langchain_core.messages import HumanMessage


reset_chat()

def sidebar():

    st.sidebar.title('YOUR-GPT')

    if st.sidebar.button('New Chat'):
        reset_chat()

    st.sidebar.header('My Conversations')

    for thread_id in st.session_state['chat_threads']:

        col1, col2 = st.sidebar.columns([0.9, 0.1])

        with col1:     
            if st.button(str(thread_id)):
                st.session_state['thread_id'] = thread_id
                messages = load_conversation(thread_id)

                temp_messages = []

                for msg in messages:
                    if isinstance(msg, HumanMessage):
                        role = 'user'
                    else:
                        role = 'assistant'
                    temp_messages.append({'role': role, 'content': msg.content})

                st.session_state['message_history'] = temp_messages

        with col2:
            with st.popover("⋮", use_container_width=True):
                st.write("**Options**")
                if st.button("Delete Chat", key=f"del_{thread_id}"):
                    st.session_state['delete_thread']  = thread_id
                    delete_thread(thread_id)