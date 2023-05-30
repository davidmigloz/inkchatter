from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage

chat = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)

messages = []

while True:
    message = input("> ")
    usr_msg = HumanMessage(content=message)
    messages.append(usr_msg)
    ai_msg = chat(messages)
    print(ai_msg.content)
    messages.append(ai_msg)
