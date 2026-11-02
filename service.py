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







async def menu_service():
    try:
        conn = await connection_db()
        a =await conn.fetch("""
SELECT * FROM dishes
""")
        return a
    except Exception as error:
        print("Menu erorr:", error)
    finally:
        await conn.close()




async def get_dish_by_id(dish_id):
    conn = await connection_db()
    try:
        return await conn.fetchrow("""
SELECT * FROM dishes 
WHERE id = $1
""", dish_id)
    finally:
        await conn.close()




async def add_to_card_service(tg_id, dish_id, quantity):
    try:
        conn = await connection_db()
        await conn.execute("""
INSERT INTO cart_items (user_id, dish_id, quantity) VALUES
($1, $2, $3)
""", int(tg_id), dish_id, int(quantity))
    except Exception as erorr:
        print("add to card erorr!", erorr)
    finally:
        await conn.close()




async def plus_quantity(dish_id, user_id):
    try:
        conn = await connection_db()
        await conn.execute("""
UPDATE cart_items
SET quantity = quantity + 1
WHERE dish_id = $1 and user_id = $2
""", dish_id, user_id)
    except Exception as erorr:
        print("plus  quantity erorr!", erorr)
    finally:
        await conn.close()


async def minus_quantity(dish_id, user_id):
    try:
        conn = await connection_db()
        await conn.execute("""
UPDATE cart_items
SET quantity = quantity - 1
WHERE dish_id = $1 and user_id = $2 and quantity > 1
""", dish_id, user_id)
        return True
    except Exception as erorr:
        print("minus  quantity erorr!", erorr)
    finally:
        await conn.close()




async def delete_cart_item(dish_id, tg_id):
    conn = await connection_db()
    try:
        return await conn.fetchval("""
            DELETE FROM cart_items
            WHERE user_id = $1 AND dish_id = $2
            RETURNING id
        """, int(tg_id), int(dish_id))
    finally:
        await conn.close()








async def show_cart_service(user_id):
    try:
        conn = await connection_db()
        a1 = await conn.fetch("""
SELECT title, quantity, price FROM cart_items
JOIN dishes ON dishes.id = cart_items.dish_id
WHERE user_id = $1
""", user_id)
        return a1
    except Exception as error:
        print("Show cart error:", error)
    finally:
        await conn.close()


















