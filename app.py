import streamlit as st
from chat_bot import get_response
st.set_page_config(page_title="Bot Forge", page_icon='🛠️')

_, c=st.columns([0.5,3.5])
with c:
    st.title("BotForge 🤖✨")
st.markdown("##")

if 'message_list' not in st.session_state:
    st.session_state['message_list'] = []
    st.session_state['disable_input'] = False
    st.session_state['start_bot'] = False

def show_message() :
    for i in st.session_state['message_list'][1:]:
        with st.chat_message(i['role']) :
            st.write(i['content'])
    st.session_state.disable_input = False

st.markdown("##### Add Knowledge Base For The BOT !")
knowledge = st.text_area(label='', label_visibility='collapsed', height=150)  
    
def restart_bot() :
    st.session_state['start_bot'] = True

st.button("Initialize Your Bot", on_click=restart_bot)

if st.session_state['start_bot'] :
    if knowledge :
        st.session_state['start_bot'] = False
        intial_prompt = f"You are a chat-bot with a sole purpose of answering user's question. You would not use your knowledge base but instead you would be using a specific knowledge base provided at the end. Your answers should be generated only from the contents of the knowledge base. If a user asks you a question which is not related to the contents of the knowledge base then you should not respond to it, but instead you should say that it is out of your knowledge base. \nThe following is your new knowledge base\n{knowledge}"
        system_content = {'role':'assistant', 'content':intial_prompt}
        assistant_response = get_response([system_content])
        assistant_content_greet = {'role':'assistant', 'content':'Hello! How can I help you'}
        st.session_state['message_list'] = [system_content, assistant_content_greet]
        show_message()  
    else :
        st.warning("Please Add Knowledge Base")

if knowledge and not(st.session_state['start_bot']) :        
    prompt = st.chat_input("Enter message", disabled=st.session_state.disable_input)
    if prompt :
        st.session_state.disable_input = True
        st.session_state['message_list'].append({'role':'user', 'content':prompt})
        response = get_response(st.session_state['message_list'])
        st.session_state['message_list'].append(response)
        show_message()