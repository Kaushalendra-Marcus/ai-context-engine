from langchain_community.document_loaders import TextLoader, DirectoryLoader


def load_documents(path="data/"):
    loader = DirectoryLoader(path, glob="**/*.txt", loader_cls=TextLoader)
    docs = loader.load()
    return docs
