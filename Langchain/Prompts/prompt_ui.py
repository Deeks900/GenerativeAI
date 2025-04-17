import streamlit as st
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
import os
import torch
from langchain_core.prompts import load_prompt

torch.classes.__path__ = []

load_dotenv()
template = load_prompt('template.json')

paper_input = st.selectbox( "Select Research Paper Name", ["Attention Is All You Need", "BERT: Pre-training of Deep Bidirectional Transformers", "GPT-3: Language Models are Few-Shot Learners", "Diffusion Models Beat GANs on Image Synthesis"] )

style_input = st.selectbox( "Select Explanation Style", ["Beginner-Friendly", "Technical", "Code-Oriented", "Mathematical"] ) 

length_input = st.selectbox( "Select Explanation Length", ["Short (1-2 paragraphs)", "Medium (3-5 paragraphs)", "Long (detailed explanation)"] )

llm = HuggingFaceEndpoint(
    repo_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation",
)
model = ChatHuggingFace(llm=llm)

prompt = template.invoke(
    {
        'paper_input':paper_input,
        'style_input':style_input,
        'length_input':length_input
    }
)
st.header('Research Tool')
# userInput = st.text_input('Enter your prompt')

if st.button('Summarize'):
    result = model.invoke(prompt)
    st.write(result.content)
