from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()
llm = HuggingFaceEndpoint(
    repo_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation",
)
model = ChatHuggingFace(llm=llm)
chatHistory = []

while True:
    userInput = input('You: ')
    chatHistory.append(userInput)
    if userInput.lower() == 'exit':
        break
    result = model.invoke(chatHistory)
    print(f"Model: {result.content}")
    chatHistory.append(result.content)


