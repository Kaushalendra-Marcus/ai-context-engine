from dotenv import load_dotenv
load_dotenv()

from loaders.loader import load_documents
from splitters.splitter import split_documents
from vectorstore.pinecode_db import get_vectorstore


def ingest():
    docs = load_documents()
    chunks = split_documents(docs)

    print(f"Loaded {len(docs)} docs")
    print(f"Created {len(chunks)} chunks")

    vectorstore = get_vectorstore(docs=chunks)

    print("Data stored in Pinecone!")


if __name__ == "__main__":
    ingest()