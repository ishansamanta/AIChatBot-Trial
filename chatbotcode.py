#cell 1 execution:
!pip install -U langchain-core langchain-community langchain-groq

'''Dependencies getting installed'''
#cell 2 execution:
pip install streamlit langchain-groq langchain python-dotenv

'''Dependencies getting installed'''

#cell 3 execution:
import getpass
api_key = getpass.getpass("paste the api you got from the website ")
''' Run the shell for confirmation'''

#cell 4 execution:
GROQ_API_KEY='paste your api key here'

#cell 5 execution:
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableWithMessageHistory
from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_core.messages import HumanMessage, AIMessage
import getpass
api_key = getpass.getpass("your api key")
chat = ChatGroq(groq_api_key=api_key, model="moonshotai/kimi-k2-instruct-0905") 
'''in the model section if your model is not working visit this website, scroll down and use the latest model: https://console.groq.com/docs/deprecations '''
prompt = ChatPromptTemplate.from_template("{input}")
store = {}
def get_history(session_id: str):
    if session_id not in store:
        store[session_id] = InMemoryChatMessageHistory()
    return store[session_id]
chain = prompt | chat
chat_with_memory = RunnableWithMessageHistory(
    chain,
    get_history,
    input_messages_key="input",
    history_messages_key="history",
)
print(" Groq LLaMA 3 Chatbot ready! Type 'exit' to quit.\n")
session_id = "ishan_session"

while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        break
    response = chat_with_memory.invoke(
        {"input": user_input},
        config={"configurable": {"session_id": session_id}},
    )
    print("Bot:", response.content)

#AFTER EXECUTION, YOU NEED TO ENTER THE GROQ API KEY AGAIN, IT WILL ASK IT FOR THE VERIFICATION AND YOUR CHATBOT WILL BE READY !!!


