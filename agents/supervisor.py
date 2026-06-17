def supervisor(state):
    query = state.get("query", "").strip()
    return{
        "company" : query
    }