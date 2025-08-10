from langchain.llms import OpenAI
from langchain.memory import ConversationBufferMemory
from langgraph import LangGraph, InputNode, OutputNode, LLMNode, MemoryNode, DecisionNode

def calculator_tool(expr: str) -> str:
    try:
        return str(eval(expr))
    except Exception:
        return "Sorry, I can't calculate that."

def decide_path(user_input: str) -> str:
    calc_tokens = {"calculate", "compute", "+", "-", "*", "/", "solve", "what is"}
    return "calculator" if any(token in user_input.lower() for token in calc_tokens) else "chatbot"

def build_graph():
    graph = LangGraph()

    user_input = InputNode("User Input")
    dispatcher = DecisionNode("Dispatcher", decision_function=decide_path)
    chatbot_llm = LLMNode("Chatbot LLM", llm=OpenAI(temperature=0))
    calculator_output = OutputNode("Calculator Output")
    memory = MemoryNode("Conversation Memory", memory=ConversationBufferMemory())
    final_output = OutputNode("Final Output")

    for node in [user_input, dispatcher, chatbot_llm, calculator_output, memory, final_output]:
        graph.add_node(node)

    graph.connect(user_input, dispatcher)
    graph.connect(dispatcher, calculator_output, condition="calculator")
    graph.connect(dispatcher, chatbot_llm, condition="chatbot")
    graph.connect(calculator_output, memory)
    graph.connect(chatbot_llm, memory)
    graph.connect(memory, final_output)

    calculator_output.run = lambda: calculator_output.set_value(calculator_tool(user_input.get_value()))

    return graph, user_input, final_output

def run_chat(graph, user_input_node, output_node, message: str) -> str:
    user_input_node.set_value(message)
    graph.run()
    return output_node.get_value()


graph, user_input, output = build_graph()

print(run_chat(graph, user_input, output, "What's the weather today?"))  
print(run_chat(graph, user_input, output, "Calculate 12 * 7 - 3"))       
