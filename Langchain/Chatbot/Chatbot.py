from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage, FunctionMessage, AIMessage

load_dotenv()
llm = HuggingFaceEndpoint(
    repo_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation",
)
model = ChatHuggingFace(llm=llm)
chatHistory = [
    SystemMessage(content="You are a helpful assistant.")
]

while True:
    userInput = input('You: ')
    chatHistory.append(HumanMessage(content=userInput))
    if userInput.lower() == 'exit':
        break
    result = model.invoke(chatHistory)
    print(f"Model: {result.content}")
    chatHistory.append(AIMessage(content=result.content))


