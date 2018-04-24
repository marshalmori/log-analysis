from database import Database


Database.initialise(database="news",
                    user="marshal",
                    password="marshal",
                    host="localhost")



print(Database.connection_pool)
