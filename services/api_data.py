from typing import Optional
import httpx
from models.character_model import charactermodel as model

async def get_characterById(characterId: int) -> Optional[model]:
    url = f"https://random-data-api.com/api/commerce/random_commerce?size=100{characterId}"
    async with httpx.AsyncClient() as client:
        response : httpx.Response = await client.get(url)
        response.raise_for_status()
        data = response.json()
        character = model(**data)
        return character
