import streamlit as st
from langchain_core.messages import HumanMessage, AIMessage
from Backend import workflow
from Session_States import init_session_state
from Sidebar_ui import sidebar


# ********************************* Initializing session States ***********************************************************
init_session_state()

# ******************************************* Initializing Sidebar_UI ********************************************************
sidebar()

# ********************************************** MAIN UI ********************************************************************

# loading all the conversation history
for message in st.session_state['message_history']:
    with st.chat_message(message['role']):
        st.markdown(message['content'])


user_input = st.chat_input('Type Here')

if user_input:

    st.session_state['message_history'].append({'role':'user', 'content': user_input})
    with st.chat_message('user'):
        st.markdown(user_input)

    #config = {'configurable' : {'thread_id' : 'thread-1'}}
    #response = workflow.invoke({'messages' : [HumanMessage(content=user_input)]}, config=config)
    #ai_message = response['messages'][-1].content

    #st.session_state['message_history'].append({'role':'assistant', 'content': ai_message})
    #with st.chat_message('assistant'):
    #   st.markdown(ai_message) 

    # using streaming
    with st.chat_message('assistant'):
        ai_message =st.write_stream(
            message_chunk.content for message_chunk, metadata in workflow.stream(
                {'messages' : [HumanMessage(content=user_input)]},
                config = {'configurable' : {'thread_id' : st.session_state['thread_id']}},
                stream_mode='messages'
            )
        )
    st.session_state['message_history'].append({'role':'assistant', 'content': ai_message})