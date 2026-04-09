from langchain_core.prompts import PromptTemplate

TECH_SPEC_PROMPT = PromptTemplate(
    template="""
You are a senior backend engineer.

Use ONLY the given context to answer.

If context is not enough, say "I don't know".

Context:
{context}

User Query:
{query}

Generate a structured response with:
1. Summary (clear explanation of feature/request)
2. Dependencies (services, modules, APIs involved)
3. Risks (edge cases, failure points, constraints)

Keep it concise and practical.
""",
    input_variables=["context", "query"],
)