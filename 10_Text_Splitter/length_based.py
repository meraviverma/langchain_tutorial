#from langchain.text_splitter import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter


loader = PyPDFLoader('D:\\langchain_models\\10_Text_Splitter\\DA_2026_Syllabus.pdf')

docs = loader.load()

# splitter = CharacterTextSplitter(
#     chunk_size=200,
#     chunk_overlap=0,
#     separator=''
# )

#chunk_size: The maximum size of each chunk of text. If a chunk exceeds this size, it will be split into
# smaller chunks.
#chunk_overlap: The number of characters that should overlap between consecutive chunks. This can help to ensure that important context is not lost when splitting the text.

#separators: A string or list of strings that specify the characters or sequences of characters that should be used to split the text. For example, you could use a newline character ("\n") to split the text into paragraphs, or a space character (" ") to split the text into words.
#seprator ["\n", " ", ",", ".", "!", "?"]  # This will split the text into sentences based on common punctuation marks.
# Paragraphs: separator "\n\n"  # This will split the text into paragraphs based on double newline characters.
#Lines: separator "\n"  # This will split the text into lines based on single newline characters.
#sentences: separator [".", "!", "?"]  # This will split the text into sentences based on common punctuation marks.
#Words: separator " "  # This will split the text into words based on spaces.
#characters: separator ""  # This will split the text into individual characters.
text_splitter = RecursiveCharacterTextSplitter(chunk_size=100, chunk_overlap=0, separators="\n")
texts = text_splitter.split_text(docs[0].page_content)

for text in texts[2:]:
    print(len(text))
    print(text)
    print('------------------')
# result = splitter.split_documents(docs)

# print(result[1].page_content)