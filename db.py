import aiosqlite


class Database:
    def __init__(self, db_file: str = "requests.db"):
        self.db_file = db_file

    async def init(self) -> None:
        async with aiosqlite.connect(self.db_file) as db:
            await db.execute(
                """
                CREATE TABLE IF NOT EXISTS requests (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    operation TEXT NOT NULL,
                    input_data TEXT NOT NULL,
                    result TEXT NOT NULL,
                    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
                )
                """
            )
            await db.commit()

    async def log_request(
        self,
        operation: str,
        input_data: str,
        result: str
    ) -> None:
        async with aiosqlite.connect(self.db_file) as db:
            await db.execute(
                """
                INSERT INTO requests (operation, input_data, result)
                VALUES (?, ?, ?)
                """,
                (operation, input_data, result)
            )
            await db.commit()
