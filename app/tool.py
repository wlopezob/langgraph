from langchain_openai import ChatOpenAI
from langgraph.graph import StateGraph, START, END, MessagesState
from langchain_core.messages import SystemMessage
from langgraph.prebuilt import ToolNode, tools_condition

class State(MessagesState):
    my_var: str

def multiply(a: int, b:int) -> int:
    """Multitply a and b.

    Args:
        a: first int
        b: second int
    """
    return a * b

def add(a: int, b:int) -> int:
    """Adds a and b.

    Args:
        a: first int
        b: second int
    """
    return a + b

tools = [multiply, add]
llm = ChatOpenAI(model="gpt-4o", temperature=0.5, max_tokens=2000)
lm = llm.bind_tools(tools, parallel_tool_calls=False)


def assistant(state: State) -> State:
    system_message = SystemMessage(content="Eres un experto en matematicas y debes de ayudar a resolver problemas")
    message = llm.invoke([system_message] + state["messages"])
    return {"messages": message}

builder = StateGraph(State)

builder.add_node('assistant', assistant)
builder.add_node("tools", ToolNode(tools))


builder.add_edge(START, 'assistant')
builder.add_conditional_edges('assistant', 
                              # evalua si la respuesa del mensaje tiene contenido o si el resultado sera la ejecucion de una funcion
                              tools_condition)
builder.add_edge('tools', 'assistant')

graph = builder.compile()