# write an Program which will read the data from PDF File
# and convert into three small chunks and summerize it.

from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
import os

# os.environ["OPENAI_API_KEY"] = "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"

# Step 1 : Load PDF File
pdf_Path = pdf_Path = r"C:\Users\Dell\Documents\Langchain_Examples\sample.pdf"
loader = PyPDFLoader (pdf_Path)
pages = loader.load_and_split()

print(f"Loaded {len(pages)} page(s)")
print(pages[0].page_content[:300]) 

# Step 2 : Split into chunks

splitter = RecursiveCharacterTextSplitter(
    chunk_size= 300,
    chunk_overlap=50
)

chunks = splitter.split_text(pdf_text)

print (f"Total Chunks are : {len(chunks)}")

#step : 3 : Init LLM and Setup Prompt Chain
llm = ChatOpenAI (model = "gpt-4", temperature=0.3)

prompt = PromptTemplate(
    input_variables = ["text"],
    template = "Summarize this chunk: \n {text}"
)

chain = LLMChain (llm=llm, prompt= prompt)

for i, chunk in enumerate(chunks):
    chunk_summary = chain.run({"text": chunk})
    print (f"\n--- Chunk{i+1} : {chunk} \nSummary ---\n {chunk_summary}")
