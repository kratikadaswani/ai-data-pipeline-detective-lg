import chromadb

client = chromadb.PersistentClient(path="chroma_db")

collection = client.get_collection(
    name="pipeline_troubleshooting"
)

data = collection.get(
    include=["documents", "metadatas", "embeddings"]
)

print("Total records:", len(data["ids"]))

for i, record_id in enumerate(data["ids"]):
    print(f"\n--- Record {i + 1} ---")
    print("ID:", record_id)
    print("Document:", data["documents"][i])
    print("Metadata:", data["metadatas"][i])

    if data["embeddings"] is not None:
        print("Embedding dimensions:", len(data["embeddings"][i]))