
from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma
from chromadb import PersistentClient

load_dotenv()

client = PersistentClient(path="chroma_db")
from langchain_huggingface import HuggingFaceEmbeddings
vectorstore = Chroma(
    client=client,
    collection_name="pipeline_troubleshooting",
    # embedding_function=OpenAIEmbeddings(
    #     model="text-embedding-3-small" )
    

    embedding_function = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )
    
)

retriever = vectorstore.as_retriever(
    search_type="similarity",
    search_kwargs={"k": 3}
)

question = (
    "Spark AnalysisException: "
    "Path does not exist: /data/sales/"
)

results = retriever.invoke(question)

print(f"Retrieved {len(results)} chunks.\n")

for i, doc in enumerate(results, start=1):
    print(f"--- Result {i} ---")
    print("Source:", doc.metadata.get("source"))
    print(doc.page_content)
    print()
