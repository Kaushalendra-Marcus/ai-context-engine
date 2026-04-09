from pydantic import BaseModel, Field
from typing import List


class TechSpec(BaseModel):
    summary: str = Field(
        description="High level summary of the feature or query",
    )
    dependencies: List[str] = Field(
        description="List of dependecies, module, learning or servies invloved"
    )
    risks: str = Field(description="Risk level, challanges for the given task")
