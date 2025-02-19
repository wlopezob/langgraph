from langchain_openai import ChatOpenAI
from typing import TypedDict
from langgraph.graph import StateGraph, START, END, MessagesState
from langchain_core.messages import SystemMessage

# set by default env OPENAI_API_KEY
llm = ChatOpenAI(model="gpt-4o", temperature=0.5, max_tokens=2000)
llm.invoke("Hola quien eres tu?")



class State(MessagesState):
    my_var: str
    customer_name: str


system_message = SystemMessage(content="Eres especialista en angular 19, si te pido cualquier otro lenguaje de programación, tienes que rechazar la solicitud")


def node_llm(state: State) -> State:
    print(state)
    message = llm.invoke([system_message] + state["messages"])
    return {"messages": message}


builder = StateGraph(State)

builder.add_node('node_llm', node_llm)

builder.add_edge(START, 'node_llm')
builder.add_edge('node_llm', END)

graph = builder.compile()