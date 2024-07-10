import streamlit as st
from langchain.memory import ConversationSummaryBufferMemory
from langchain_openai import ChatOpenAI
from get_gptresponse import get_gptresponse
st.title("🤖思颖聊天机器人")
#侧边框
with st.sidebar:
    openai_key=st.text_input("请输入OpenAI API密钥")
    st.markdown("[如何获取OpenAI API密钥？](https://openai.com/index/chatgpt/)")
#初始聊天界面：
if "memory" not in st.session_state:
    model = ChatOpenAI(model='gpt-3.5-turbo',
                      api_key=openai_key,
                      openai_api_base="https://api.aigc369.com/v1")
    st.session_state["memory"]=ConversationSummaryBufferMemory(
        llm=model,max_token_limit=2000,return_messages=True
    )
    st.session_state["message"]=[{"role":"ai",
                                  "context":"你好，思颖机器人为您服务，有什么可以帮到你的吗？"}]
for message in st.session_state["message"]:
    st.chat_message(message["role"]).write(message["context"])
##询问开始
prompt=st.chat_input("您想了解一些什么？思颖来告诉你")
if prompt:
    if openai_key == '':
        st.info("请输入OpenAI API密钥")
        st.stop()
    else:
        st.chat_message('human').write(prompt)
        st.session_state["message"].append({"role":"human","context":prompt})
##问题处理
        with st.spinner("👩思颖正在思考哦，请稍等"):
            result=get_gptresponse(prompt,st.session_state["memory"],openai_key)
        st.chat_message('ai').write(result)
        st.session_state["message"].append({"role":"ai","context":result})
