from langchain.llms import AzureChatOpenAI
from langchain.memory import ConversationBufferMemory
from langgraph import LangGraph, InputNode, OutputNode, LLMNode, MemoryNode


llm = AzureChatOpenAI(
    deployment_name="AopenAI",
    model_name="gpt-35-turbo",
    temperature=0,
    #openai_api_key="6I1m3qrSuwN0hFCavPrmZarUXy5wkwCEQp9gcTt07bz5YaBpBbFuJQQJ99BHACqBBLyXJ3w3AAABACOG8MHB",
    openai_api_base="https://firsttaskoai.openai.azure.com/",
    openai_api_version="2023-05-15"
)


graph = LangGraph()


input_node = InputNode(name="User Input")                   
llm_node = LLMNode(name="Azure GPT-3.5", llm=llm)           
memory_node = MemoryNode(name="Conversation Memory", memory=ConversationBufferMemory())  
output_node = OutputNode(name="Output")                     


for node in [input_node, llm_node, memory_node, output_node]:
    graph.add_node(node)


graph.connect(input_node, llm_node)
graph.connect(llm_node, memory_node)
graph.connect(memory_node, output_node)

def chat(user_text):
    input_node.set_value(user_text) 
    graph.run()                      
    return output_node.get_value()   


print("You: Hello, how are you?")
print("Bot:", chat("Hello, how are you?"))

print("\nYou: Tell me a joke")
print("Bot:", chat("Tell me a joke"))
