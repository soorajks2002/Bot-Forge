import streamlit as st
from chat_bot import get_response

if 'message_list' not in st.session_state:
    st.session_state['message_list'] = []
    st.session_state['disable_input'] = False
    st.session_state['start_bot'] = False

def show_message() :
    for i in st.session_state['message_list'][1:]:
        with st.chat_message(i['role']) :
            st.write(i['content'])
    st.session_state.disable_input = False
    
def restart_bot() :
    st.session_state['start_bot'] = True

knowledge = st.text_area(label='', label_visibility='collapsed', height=200)
st.button("Initialize Your Bot", on_click=restart_bot)

if st.session_state['start_bot'] :
    st.session_state['start_bot'] = False
    system_content = {'role':'user', 'content':f"You are a chat bot with limited knowledge focused on {knowledge}\nHowever, if asked about topics outside this scope, please respond with 'out of my scope' and address questions associated with your knowledge."}
    assistant_content = {'role':'assistant', 'content':'Hello! How can I help you'}
    st.session_state['message_list'] = [system_content, assistant_content]
    show_message()  

if knowledge :              
    prompt = st.chat_input("Enter message", disabled=st.session_state.disable_input)
    if prompt :
        st.session_state.disable_input = True
        st.session_state['message_list'].append({'role':'user', 'content':prompt})
        response = get_response(st.session_state['message_list'])
        st.session_state['message_list'].append(response)
        show_message()