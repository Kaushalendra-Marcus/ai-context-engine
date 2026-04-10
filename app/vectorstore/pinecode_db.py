import os
from langchain_pinecone import PineconeVectorStore
from pinecone import Pinecone, ServerLessSpec
from embeddings.embedding import get_embeddings

INDEX_NAME = "ai-context-engine"


def init_pinecode():
    pc = Pinecone(api_key=os.getenv("PINECONE_API_KEY"))
    if INDEX_NAME not in [index["name"] for index in pc.list_indexes()]:
        pc.create_index(
            name=INDEX_NAME,
            dimension=384,
            metric="cosine",
            spec=ServerLessSpec(cloud="aws", region="us-east-1"),
        )
    return pc


def get_vectorstore(docs =None):
    embeddings = get_embeddings()
    pc = init_pinecode()

    if docs:
        return PineconeVectorStore.from_documents(
            docs, embeddings, index_name=INDEX_NAME
        )

    return PineconeVectorStore.from_existing_index(index_name=INDEX_NAME, embedding=embeddings)
