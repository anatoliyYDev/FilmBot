import aiosqlite
from aiosqlite import Error as sqliteError
from loader import DB_PATH, DB_SQL_PATH, logger


async def init_db():
    async with aiosqlite.connect(DB_PATH) as conn:
        cur = await conn.cursor()
        try:
            with open(DB_SQL_PATH, "r") as script:
                await cur.executescript(script.read())
        except sqliteError:
            logger.exception("Произошла ошибка при инициализации БД!")
            await conn.rollback()
        else:
            await conn.commit()


async def check_code_exist(code):
    async with aiosqlite.connect(DB_PATH) as conn:
        cur = await conn.cursor()
        await cur.execute(f'SELECT * FROM films WHERE code="{code}"')
        res = await cur.fetchone()
    return res


async def write_film(code, title, about):
    async with aiosqlite.connect(DB_PATH) as conn:
        cur = await conn.cursor()
        try:
            await cur.execute(f'INSERT INTO films VALUES("{code}", "{title}", "{about}")')
        except sqliteError:
            logger.exception("Произошла ошибка при записи нового фильма!")
            await conn.rollback()
            return False
        else:
            await conn.commit()
            return True


async def change_film_db(code, title, about):
    async with aiosqlite.connect(DB_PATH) as conn:
        cur = await conn.cursor()
        try:
            await cur.execute(f'UPDATE films SET title="{title}", about="{about}" WHERE code="{code}"')
        except sqliteError:
            logger.exception("Произошла ошибка при изменении фильма!")
            await conn.rollback()
            return False
        else:
            await conn.commit()
            return True


async def delete_film_db(code):
    async with aiosqlite.connect(DB_PATH) as conn:
        cur = await conn.cursor()
        try:
            await cur.execute(f'DELETE FROM films WHERE code="{code}"')
        except sqliteError:
            logger.exception("Произошла ошибка при удалении фильма!")
            await conn.rollback()
            return False
        else:
            await conn.commit()
            return True
