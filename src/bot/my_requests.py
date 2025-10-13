import logging

import aiohttp
import asyncio
from typing import Dict, Any

API_LINK = "http://localhost:8000/api/v1/users"


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


async def make_post_request(username: str, user_id: int) -> Dict[str, Any]:
    payload = {"username": username, "tg_id": user_id}

    try:
        async with aiohttp.ClientSession() as session:
            async with session.post(API_LINK, json=payload) as response:
                if response.status == 200:
                    return await response.json()
                else:
                    error_text = await response.text()
                    raise Exception(f"HTTP {response.status}: {error_text}")

    except aiohttp.ClientError as e:
        print(f"Network error occurred: {e}")
        raise
    except Exception as e:
        print(f"Unexpected error: {e}")
        raise


async def get_user_if_exist(tg_id: int) -> bool:
    params = {"tg_id": tg_id}

    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(API_LINK, params=params, timeout=30) as response:

                if response.status == 200:

                    data = await response.json()
                    logger.info(f"Пользователь {tg_id} существует: {data}")
                    return True
                elif response.status == 404:

                    logger.info(f"Пользователь {tg_id} не найден")
                    return False
                else:

                    error_text = await response.text()
                    logger.error(f"Ошибка сервера {response.status}: {error_text}")
                    return False

    except aiohttp.ClientError as e:
        logger.error(f"Ошибка сети при проверке пользователя {tg_id}: {e}")
        return False
    except asyncio.TimeoutError:
        logger.error(f"Таймаут при проверке пользователя {tg_id}")
        return False
    except Exception as e:
        logger.error(f"Неожиданная ошибка при проверке пользователя {tg_id}: {e}")
        return False
