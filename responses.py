def handle_response(message) -> str:
    p_message = message.lower()

    if p_message == "test":
        return "Journals Butler, At your service."

    if p_message == "dan":
        return "Smells!"