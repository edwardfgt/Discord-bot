def get_response(message: str) -> str:
    p_message = message.lower()

    if p_message == "?bot":
        return "Journals Butler, At your service."

    if p_message == "?":
        return "?"
        
    if p_message == "dan":
        return "Smells!"
