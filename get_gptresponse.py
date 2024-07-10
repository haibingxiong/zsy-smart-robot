from langchain_openai import ChatOpenAI
from langchain.chains import ConversationChain
from langchain.prompts import ChatPromptTemplate
from langchain_core.prompts import MessagesPlaceholder
def get_gptresponse(prompt,memory,openai_key):
    model=ChatOpenAI(model='gpt-3.5-turbo',
                     api_key=openai_key,
                     openai_api_base = "https://api.aigc369.com/v1")
    prompt_template= ChatPromptTemplate.from_messages(
        [("system","你是一个乐于助人的对话助手"),
         MessagesPlaceholder(variable_name='history'),
         ("human","{input}")])
    chain=ConversationChain(llm=model,memory=memory,prompt= prompt_template)
    history= memory.load_memory_variables({})["history"]
    response=chain.invoke({"input":prompt})["response"]
    return response
###字典形式