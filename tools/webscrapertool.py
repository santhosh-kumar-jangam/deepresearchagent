def web_scraper(urls: list[str]) -> list[dict]:
    """
    Scrapes multiple webpages for their content.

    Args:
        urls (list): A list of webpage URLs to scrape.

    Returns:
        list[dict]: A list of dictionaries containing the link and content.
                    Each entry looks like {"link": "<url>", "content": "<content>"}.
    """
    import requests
    from bs4 import BeautifulSoup
    import re

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}

    results = []

    for url in urls:
        try:
            response = requests.get(url, headers=headers, timeout=15)
            response.raise_for_status()

            soup = BeautifulSoup(response.content, 'html.parser')

            # Extract body
            body = soup.find('body')
            if not body:
                raise ValueError("Could not find the body of the page.")

            # Remove unwanted tags
            tags_to_remove = ['nav', 'footer', 'header', 'aside', 'form', 'script', 'style', 'a']
            for tag_name in tags_to_remove:
                for tag in body.find_all(tag_name):
                    tag.decompose()

            # Clean body text
            raw_text = body.get_text(separator=' ', strip=True)
            cleaned_text = re.sub(r'\s+', ' ', raw_text).strip()

            results.append({
                "link": response.url,
                "content": cleaned_text[:3000]
            })

        except Exception as e:
            results.append({
                "link": url,
                "content": f"Error occurred: {e}"
            })

    return results