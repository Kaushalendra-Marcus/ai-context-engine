from langchain_community.document_loaders import TextLoader, DirectoryLoader


def load_documents(path="data/"):
    loader = DirectoryLoader(path, glob="**/*.txt", loader_cls=TextLoader)
    docs = loader.load()
    return docs

def load_codebase(path="repo/"):
    all_docs = []

    file_types = ["**/*.py", "**/*.js", "**/*.ts", "**/*.json", "**/*.md"]

    for pattern in file_types:
        loader = DirectoryLoader(
            path,
            glob=pattern,
            loader_cls=TextLoader
        )
        docs = loader.load()

        for doc in docs:
            doc.metadata["type"] = "code"
            doc.metadata["file_type"] = pattern

        all_docs.extend(docs)

    return all_docs