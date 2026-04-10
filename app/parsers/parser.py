from langchain_core.output_parsers import PydanticOutputParser
from models.schema import TechSpec

def get_parser():
    return PydanticOutputParser(pydantic_object=TechSpec)