from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader

loader = DirectoryLoader(
    path=r'E:\\Udemy Course\\LangChain',
    glob='*.pdf',
    loader_cls=PyPDFLoader
)

#docs = loader.lazy_load()
docs=loader.load()

print(docs[0].page_content)
print(docs[0].metadata)
# for document in docs:
#     print(document.metadata)