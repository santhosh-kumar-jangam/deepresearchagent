def web_search(query: str) -> list[dict]:
    """
    Searches the web and return top results with title, link and summary.
    
    Args:
        query (str): Search query
        max_results (int): Number of top results to be returned
    
    Returns:
        List[dict]: List of dictionaries with keys: title, link, summary, content
    """
    from ddgs import DDGS

    results = []
    try:
        ddgs = DDGS()
        search_results = list(ddgs.text(query, max_results=2))

        for res in search_results:
            results.append({
                "title": res.get("title", "No Title"),
                "link": res.get("href", ""),
                "summary": res.get("body", "No Summary")
            })

    except Exception as e:
        results.append({"error": f"Search failed: {str(e)}"})

    return results