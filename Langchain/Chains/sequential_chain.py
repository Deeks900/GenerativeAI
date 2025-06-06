from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation",
)

model = ChatHuggingFace(llm=llm)

prompt1 = PromptTemplate(
    template = 'Generate a detailed report on topic {topic}',
    input_variables = ['topic']
)

prompt2 = PromptTemplate(
    template = 'Generate a 5 point summary on text {text}',
    input_variables = ['text']
)

parser = StrOutputParser()
chain  = prompt1 | model | parser | prompt2 | model | parser
result = chain.invoke({'topic':'cricket'})
print(result)