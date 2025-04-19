from langchain_community.document_loaders import WebBaseLoader

loader = WebBaseLoader("https://www.geeksforgeeks.org/what-is-python/")
docs = loader.load()

print(docs)