## Conversational Q&A Chatbot
import streamlit as st

from langchain.schema import HumanMessage,SystemMessage,AIMessage
from langchain.chat_models import ChatOpenAI

## Streamlit UI
with open("style.css") as f:

        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


st.title("🥰🥰يمكنك طرح أي سؤال وسأجيب عنه")


#st.set_page_config(page_title="Conversational Q&A Chatbot")
#st.header("Hey, Let's Chat")

from dotenv import load_dotenv
load_dotenv()
import os

chat=ChatOpenAI(temperature=0.5)

if 'flowmessages' not in st.session_state:
    st.session_state['flowmessages']=[
        SystemMessage(content="أنت معلم خبير في إعداد مذكرات بيداغوجية وانتاج تمرينات ومسائل نموذجية")
    ]
conversation = st.session_state['flowmessages']
## Function to load OpenAI model and get respones

def get_chatmodel_response(question):

    conversation.append(HumanMessage(content=question))
    answer=chat(conversation)
    conversation.append(AIMessage(content=answer.content))
    return answer.content


for message in conversation[1:]:
    if message.type == 'human':
            with st.chat_message(message.type, avatar = "🧑‍💻"):
                st.write(message.content)
    else:
             with st.chat_message(message.type):
                st.write(message.content)


#input=st.text_input("Input: ",key="input")
prompt = st.chat_input("أرجوك حاول أن تجعل سؤالك واضحا قدر الإمكان")
if prompt:
    # Display user message in chat message container
        with st.chat_message("user"):
            st.markdown(prompt)
    # Add user message to chat history
        response = get_chatmodel_response(prompt)
        

        with st.chat_message("assistant"):
            st.markdown(response)

