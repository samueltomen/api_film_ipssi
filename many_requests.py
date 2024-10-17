import asyncio

import aiohttp


async def fetch_data(session, url):
    async with session.get(url) as response:
        if response.status == 200:
            return await response.json()
        else:
            return {"error": f"Failed to fetch data, status code: {response.status}"}


async def main():
    urls = [
        "https://jsonplaceholder.typicode.com/posts/1",
        "https://jsonplaceholder.typicode.com/posts/2",
        "https://jsonplaceholder.typicode.com/posts/3",
        "https://jsonplaceholder.typicode.com/posts/4",
        "https://jsonplaceholder.typicode.com/posts/5",
        "https://jsonplaceholder.typicode.com/posts/6",
        "https://jsonplaceholder.typicode.com/posts/7",
        "https://jsonplaceholder.typicode.com/posts/8",
    ]
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_data(session, url) for url in urls]
        results = await asyncio.gather(*tasks)
        for result in results:
            count = len(results)
        return count


asyncio.run(main())
