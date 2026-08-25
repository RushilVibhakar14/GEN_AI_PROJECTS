import re


def validate_sql(sql: str):
    sql = sql.strip().replace("```sql", "").replace("```", "").strip()

    if not sql.upper().startswith("SELECT"):
        return False, "Only SELECT queries are allowed.", ""

    forbidden = ["DROP", "DELETE", "UPDATE", "INSERT", "ALTER", "CREATE"]

    if any(re.search(rf"\b{word}\b", sql.upper()) for word in forbidden):
        return False, "Unsafe SQL blocked.", ""

    if "LIMIT" not in sql.upper():
        sql += " LIMIT 100"

    return True, "SQL allowed.", sql
