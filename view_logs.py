import asyncio
import aiosqlite


async def view_logs():
    async with aiosqlite.connect("requests.db") as db:
        async with db.execute("SELECT * FROM requests") as cursor:
            async for row in cursor:
                print(row)

asyncio.run(view_logs())
