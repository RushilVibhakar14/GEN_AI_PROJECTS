import pandas as pd
from langchain_core.messages import HumanMessage, SystemMessage

from app.database import run_query
from app.guardrails import validate_question
from app.llm_service import get_llm
from app.prompts import answer_prompt
from app.sql_chain import generate_sql
from app.sql_validator import validate_sql


def ask_database(question: str):
    allowed, message = validate_question(question)

    if not allowed:
        return message, "", pd.DataFrame(), ""

    try:
        raw_sql = generate_sql(question)
    except Exception as e:
        return f"LLM error: {e}", "", pd.DataFrame(), ""

    allowed, message, safe_sql = validate_sql(raw_sql)

    if not allowed:
        return message, raw_sql, pd.DataFrame(), ""

    try:
        columns, rows = run_query(safe_sql)
        df = pd.DataFrame(rows, columns=columns)
    except Exception as e:
        return f"Database error: {e}", safe_sql, pd.DataFrame(), ""

    try:
        response = get_llm().invoke([
            SystemMessage(content="You are a helpful business data analyst."),
            HumanMessage(content=answer_prompt(question, safe_sql, str(rows)))
        ])
        if isinstance(response.content, list):
            answer = "".join(
                item.get("text", "")
                for item in response.content
                if isinstance(item, dict))
        else:
            answer = str(response.content)
    except Exception:
        answer = "Query succeeded, but the explanation could not be generated."

    return f"Query complete. Rows: {len(df)}", safe_sql, df, answer
