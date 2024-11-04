from sqlalchemy.ext.asyncio import AsyncSession
from typing import AsyncGenerator
from backend.db import async_session_maker


# async def get_db_sync():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()


async def get_db() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session