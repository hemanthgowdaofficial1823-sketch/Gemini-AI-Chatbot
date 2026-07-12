from duckduckgo_search import DDGS


def search_web(query, max_results=5):
    """
    Search the web using DuckDuckGo.

    Args:
        query (str): Search query.
        max_results (int): Number of search results.

    Returns:
        list: List of search results.
    """
    results = []

    try:
        with DDGS() as ddgs:
            for result in ddgs.text(query, max_results=max_results):
                results.append({
                    "title": result.get("title", ""),
                    "body": result.get("body", ""),
                    "href": result.get("href", "")
                })

    except Exception as e:
        print(f"Search Error: {e}")

    return results


if __name__ == "__main__":
    query = input("Enter your search query: ")

    results = search_web(query)

    if results:
        print("\nSearch Results:\n")
        for i, result in enumerate(results, 1):
            print(f"{i}. {result['title']}")
            print(result["body"])
            print(result["href"])
            print("-" * 60)
    else:
        print("No results found.")
