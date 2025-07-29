import httpx
from app.config import NEWS_API_ENDPOINT, NEWS_API_KEY

async def get_news():
    try:
        async with httpx.AsyncClient() as client:
            url = NEWS_API_ENDPOINT
            params = {
                "apiKey" : NEWS_API_KEY,
                "q": "Python programming",
                "language": "en",
                "sortBy": "publishedAt"
            }
            res = await client.get(url=url, params=params)
            if res.status_code != 200:
                return
            
            data = res.json()
            if res.status_code != 200 or data.get("status") != "ok":
                print("NewsAPI Error:", data.get("message"))
                return
            
            return data
    except httpx.RequestError as e:
        print("Network error while requesting NewsAPI:", str(e))
        return