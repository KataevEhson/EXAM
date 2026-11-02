from dotenv import load_dotenv
import asyncpg
import os

load_dotenv()
pasw  = os.getenv("PASSWORD_DB")


async def connection_db():
    try:
        conn = await asyncpg.connect(
            host="localhost",
            port=5432,
            user="postgres",
            database="final_exam",
            password=pasw
        )
        return conn
    except Exception as Error:
        print(f"Connection Error: {Error}")
        
async def create_table():
    try:
        conn = await connection_db()
        await conn.execute("""
CREATE TABLE if not exists users (
    id serial primary key,
    username varchar(50),
    full_name varchar(50),
    telegram_id text,
    is_admin boolean default false,
    created_at timestamp default now(),
    is_active boolean default true
);

      """)
        print("Table created")
    except Exception as Error:
        print(f"Create Error: {Error}")
    finally:
        await conn.close()
        
        