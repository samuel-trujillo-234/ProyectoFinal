## Coding Dojo - Python Bootcamp Jan 2025
## Final project
## Wavely
 
import pymysql.cursors 
import os

class MySQLConnection: 
    def __init__(self):
        print("USER ", os.getenv("USER"))
        connection = pymysql.connect(
            host=os.getenv("HOST_DATABASE", "localhost"),
            user=os.getenv("USER_DATABASE"),
            password=os.getenv("PASSWORD"),
            db=os.getenv("DATABASE"),
            charset="utf8mb4",
            cursorclass=pymysql.cursors.DictCursor,
            autocommit=True,
        )
        self.connection = connection 


    def query_db(self, query, data=None):
        with self.connection.cursor() as cursor:
            try:
                query = cursor.mogrify(query, data)
                print("Running Query:", query)

                executable = cursor.execute(query, data)
                if query.lower().find("insert") >= 0:
                    self.connection.commit()
                    return cursor.lastrowid
                elif query.lower().find("select") >= 0:
                    
                    result = cursor.fetchall()
                    return result
                else:

                    self.connection.commit()
            except Exception as e:
                print("Something went wrong", e)
                return False
            finally:
                self.connection.close() 

def connectToMySQL():
    return MySQLConnection()