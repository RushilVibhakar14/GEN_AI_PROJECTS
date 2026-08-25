def sql_prompt(schema: str, question: str):
    return f"""
You are a SQL assistant.

Database schema:
{schema}

User question:
{question}

Return only one read-only SELECT query.
"""


def answer_prompt(question: str, sql: str, results: str):
    return f"""
Answer the user's question using only the SQL result.

Question: {question}
SQL: {sql}
Results: {results}

Give a short business-friendly answer.
"""
