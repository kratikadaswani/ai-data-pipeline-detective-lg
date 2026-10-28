import hashlib
from pathlib import Path

from langchain_community.document_loaders import DirectoryLoader, TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma
from chromadb import PersistentClient

KNOWLEDGE_DIR = "knowledge_base"
DB_DIR = "chroma_db"
COLLECTION_NAME = "pipeline_troubleshooting"


# 1. Load all Markdown troubleshooting documents
loader = DirectoryLoader(
    KNOWLEDGE_DIR,
    glob="*.md",
    loader_cls=TextLoader, 
    loader_kwargs={"encoding": "utf-8"},
    show_progress=True
)

documents = loader.load()

if not documents:
    raise ValueError(
        "No Markdown documents found in knowledge_base/."
    )

print(f"Loaded {len(documents)} documents.")

# 2. Split documents into overlapping chunks
splitter = RecursiveCharacterTextSplitter(
    chunk_size=800,
    chunk_overlap=120
)

chunks = splitter.split_documents(documents)

print(f"Created {len(chunks)} chunks.")

# 3. Initialize the embedding model
from langchain_huggingface import HuggingFaceEmbeddings

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# 4. Create or reuse the persistent Chroma collection
client = PersistentClient(path=DB_DIR)


try:
    client.delete_collection(COLLECTION_NAME)
except Exception as exc:
    # A missing collection is expected on the first run.
    # if "not found" not in str(exc).lower():
    #     raise
    pass

vectorstore = Chroma(
    client=client,
    collection_name=COLLECTION_NAME,
    embedding_function=embeddings
)

# 5. Generate stable IDs so each rebuild indexes
#    the current documents without accumulating duplicates.
ids = []

for doc in chunks:
    print(doc)
    source = doc.metadata.get("source", "unknown")
    digest = hashlib.sha256(
        f"{source}\n{doc.page_content}".encode("utf-8")
    ).hexdigest()
    ids.append(digest)

vectorstore.add_documents(
    documents=chunks,
    ids=ids
)

print(f"Indexed {len(chunks)} chunks.")
print(f"Chroma database saved in: {DB_DIR}")
