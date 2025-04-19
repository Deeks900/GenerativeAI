from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader
loader = DirectoryLoader(
    path = 'books',
    glob="*.pdf",
    loader_cls=PyPDFLoader,
)

docs = loader.load()

docs = loader.lazy_load()
# print(docs)
# print(len(docs))
print(docs[3].page_content)