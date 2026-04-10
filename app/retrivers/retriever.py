from vectorstore.pinecode_db import get_vectorstore


def get_retriever():
    vectorstore = get_vectorstore()
    retriever = vectorstore.as_retriever(
        search_type="similarity", search_kwargs={"k": 3}
    )
    return retriever
