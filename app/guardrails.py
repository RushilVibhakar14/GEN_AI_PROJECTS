def validate_question(question: str):
    if not question or not question.strip():
        return False, "Please enter a question."

    blocked = ["drop table", "delete from", "update ", "insert into"]
    text = question.lower()

    if any(item in text for item in blocked):
        return False, "Question blocked by guardrails."

    return True, "Question allowed."
