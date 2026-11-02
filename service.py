from conection import *




async def create_user(username, full_name, telegram_id):
    try:
        conn = await connection_db()
        await conn.execute("""
        insert into users(username, full_name, telegram_id) Values
        ($1, $2, $3) 
                     """, username, full_name,str(telegram_id))
    except Exception as Error:
        print(f"Create user Error: {Error}")
    finally:
        await conn.close()
        


async def get_user_by_id(telegram_id):
    try:
        conn = await connection_db()
        user = await conn.fetchrow("""
        select * from users where telegram_id = $1
                     """, str(telegram_id))
        return user
    except Exception as Error:
        print(f"Get user by id Error: {Error}")
    finally:
        await conn.close()
        

async def check_admin(telegram_id):
    try:
        conn = await connection_db()
        users = await conn.fetchrow("""
        select * from users where telegram_id = $1 and is_admin = true
                     """, str(telegram_id))
        return users
    except Exception as Error:
        print(f"Get user Error: {Error}")
    finally:
        await conn.close()
        
        








async def add_dish_service(title, price, description, photo_file_id):
    try:
        conn = await connection_db()
        await conn.execute("""
insert into dishes (title, price, description, photo_file_id) VALUES
($1, $2, $3, $4)
""", title, int(price), description, photo_file_id)
        return True
    except Exception as error:
        print("Add dish error:", error)
    finally:
        await conn.close()



















































