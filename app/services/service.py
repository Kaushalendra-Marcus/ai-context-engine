from chains.rag_chains import get_rag_chain


class QueryService:
    def __init__(self):
        self.chain = get_rag_chain()

    def process_query(self, query: str):
        try:
            result = self.chain.invoke(query)
            return {
                "summary": result.summary,
                "depencies": result.dependencies,
                "risks": result.risks,
            }
        except Exception as e:
            return {"error": str(e)}
