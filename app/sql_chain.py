from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

from app.database import get_schema
from app.llm_service import get_llm
from app.prompts import sql_prompt


def generate_sql(question: str):
    prompt = ChatPromptTemplate.from_template(
        sql_prompt(get_schema(), "{question}")
    )

    chain = prompt | get_llm() | StrOutputParser()

    return chain.invoke({"question": question}).strip()
