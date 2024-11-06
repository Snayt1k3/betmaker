from logging import getLogger

import aiohttp

logger = getLogger(__name__)

class HttpClient:

    async def request(self, method: str, url: str, **kwargs: dict):
        """Общий метод для выполнения HTTP-запросов"""
        async with aiohttp.ClientSession() as session:
            try:
                logger.info(f"Starting {method.upper()} request to {url} with {kwargs}")
                async with session.request(method.upper(), url, **kwargs) as response:
                    response_data = await response.json()
                    logger.info(f"Received response from {url} with status {response.status}: {response_data}")
                    return response_data
            except Exception as e:
                logger.error(f"Error during {method.upper()} request to {url}: {e}")
                raise

    async def get(self, url: str, **kwargs: dict):
        """GET-запрос через общий метод request"""
        return await self.request("GET", url, **kwargs)

    async def post(self, url: str, **kwargs: dict):
        """POST-запрос через общий метод request"""
        return await self.request("POST", url, **kwargs)

    async def patch(self, url: str, **kwargs: dict):
        """POST-запрос через общий метод request"""
        return await self.request("PATCH", url, **kwargs)
