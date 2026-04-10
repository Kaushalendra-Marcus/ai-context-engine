from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
import os
from dotenv import load_dotenv
from langchain_core.runnables import RunnablePassthrough
from prompts.prompt import TECH_SPEC_PROMPT
from retrivers.retriever import get_retriever
from parsers.parser import get_parser


def get_llm():
    llm = HuggingFaceEndpoint(
        repo_id="meta-llama/Llama-3.3-70B-Instruct",
        task="text-generation",
        huggingfacehub_api_token=os.getenv("HUGGINGFACEHUB_API_TOKEN"),
        temperature=0.3,
    )
    return ChatHuggingFace(llm=llm)


def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)


def get_rag_chain():
    retriever = get_retriever()
    parser = get_parser()
    llm = get_llm()

    chain = (
        {"context": retriever | format_docs, "query": RunnablePassthrough()}
        | TECH_SPEC_PROMPT
        | llm
        | parser
    )
    return chain
