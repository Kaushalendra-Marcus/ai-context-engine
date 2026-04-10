from langchain_core.prompts import PromptTemplate
from parsers.parser import get_parser

parser = get_parser()

TECH_SPEC_PROMPT = PromptTemplate(
    template="""
You are a senior backend engineer.

Use ONLY the given context.

{format_instructions}

Context:
{context}

Query:
{query}
""",
    input_variables=["context", "query"],
    partial_variables={
        "format_instructions": parser.get_format_instructions()
    }
)