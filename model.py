
import sqlite3

database=sqlite3.Connection("cars_sadatabse.db")
RunSQL = database.cursor()

RunSQL.execute("CREATE TABLE IF NOT EXISTS cars_table(carid INTEGER PRIMARY KEY, brand TEXT, model TEXT, year INTEGER, price FLOAT)")
database.commit()

class Car:

    number_of_cars = 0
    def __init__(self, carid, brand, model, year, price):
        self.carid=carid
        self.brand=brand
        self.model=model
        self.year=year
        self.price=price
        Car.number_of_cars+=1
        try:
            RunSQL.execute("INSERT INTO cars_table VALUES(?,?,?,?,?)",(self.carid, self.brand, self.model, self.year, self.price))
            database.commit()
        except:
            print("CarID is duplicate !")
        
    
    @classmethod
    def find_car(cls,carid):
        select_cars=list(RunSQL.execute("SELECT * FROM cars_table WHERE carid = ?" , (carid,)))
        if len(select_cars) == 0 :
            raise Exception("Car not exists in database !")
        else:
            return list(select_cars)
    
    @classmethod
    def list(cls):
        return list(RunSQL.execute("SELECT * FROM cars_table"))

    @classmethod
    def update(cls, carid, brand, model, year, price):
        update_cars=RunSQL.execute("UPDATE cars_table SET carid=?, brand=?, model=?, year=?, price=? WHERE carid=?",(carid, brand, model, year, price,carid))
        if update_cars.rowcount == 0 :
            print("Car not exists in database !")
        database.commit()
    
    @classmethod
    def delete(cls,carid):
        del_car=RunSQL.execute("DELETE FROM cars_table WHERE carid = ?",(carid,))
        if del_car.rowcount == 0:
            print("Car not exists in database !")
        database.commit()
    
    
    def __del__(self):
        database.close()