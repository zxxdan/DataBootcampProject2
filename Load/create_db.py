def create_db():
    from config import user, password
    from sqlalchemy import create_engine
    
    engine = create_engine(f"postgresql+psycopg2://{user}:{password}@localhost:5432/")

    connection = engine.connect()
    connection.execute("commit")
    return_string = ""
    try:
        connection.execute("create database collisions_db")
        return_string = "Success"
    except:
        return_string="Database already exists or the connection is not valid. Please check the connection string if the steps following this fail."
        
    connection.close()

    return return_string

