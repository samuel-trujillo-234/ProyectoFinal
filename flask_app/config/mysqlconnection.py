## Coding Dojo - Python Bootcamp Ene 2025
## Proyecto final
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
                # Imprimir la query para depuración
                print("Running Query:", query)
                
                if data:
                    executable = cursor.execute(query, data)
                else:
                    executable = cursor.execute(query)
                    
                if query.lower().find("insert") >= 0:
                    # Si es INSERT, devolver el ID del último row insertado
                    self.connection.commit()
                    return cursor.lastrowid
                elif query.lower().find("select") >= 0:
                    # Si es SELECT, devolver los resultados como diccionario
                    result = cursor.fetchall()
                    return result
                else:
                    # Si es UPDATE o DELETE, devolver nada
                    self.connection.commit()
            except Exception as e:
                # Si la query falla, imprimir error y devolver False
                print("Something went wrong", e)
                return False
            finally:
                # Cerrar la conexión
                self.connection.close()

def connectToMySQL():
    # Función para crear una instancia de la conexión
    return MySQLConnection()