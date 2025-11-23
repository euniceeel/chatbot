import streamlit as st
import random
import time

st.set_page_config(page_title="ChatBotChatBot")

st.title("Talk")

def get_reply(message): 
    message = message.lower()

    if "안녕" in message or "hello" in message:
        return ("text", "안녕, 만나서 반가워.")
    elif "기분이 어때" in message:
        return ("text", get_random_mood())
    elif "cat" == message:
        img_url = get_cat_image_url()
        return ("image", img_url)
    else:
        return ("text", "아직 무슨 말인지 모르겠어.")
    
def get_random_mood():
    mood = ["기분이 좋아.", "기분이 그저 그래.", "나쁘지 않아.", "행복해."]
    return random.choices(mood)[0]

def get_cat_image_url():
    return "https://cataas.com/cat?time={time.time()}"
    

# user_input = st.text_input("message를 입력하세요")

if "chat_log" not in st.session_state:
    st.session_state.chat_log = []

prompt = st.chat_input("메시지를 입력하세요")

if prompt:
    st.session_state.chat_log.append(("user", prompt, "text"))
    with st.chat_message("user"):
        st.write(prompt)

    # 봇 응답
    reply_type, reply = get_reply(prompt)

    st.session_state.chat_log.append(("assistant", reply, reply_type))

    with st.chat_message("assistant"):
        if reply_type == "text":
            st.write(reply)
        else:
            st.image(reply, width=300)
