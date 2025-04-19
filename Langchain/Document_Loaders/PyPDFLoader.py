from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader('abc.pdf')
docs = loader.load()

print(docs)
print(len(docs))
