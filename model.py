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
    
    def create(self):
        RunSQL.execute("INSERT INTO cars_table VALUES(?,?,?,?,?)",(self.carid, self.brand, self.model, self.year, self.price))
        database.commit()
    
    def delete(self,carid):
        RunSQL.execute("DELETE FROM cars_table WHERE carid = ?",carid)
        database.commit()
    
    def car(self,carid):
        return RunSQL.execute("SELECT * FROM cars_table WHERE carid = ?" , carid)
    
    @classmethod
    def cars_list(cls):
        return list(RunSQL.execute("SELECT * FROM cars_table"))

    def update(self, cardid, brand, model, year, price):
        RunSQL.execute("UPDATE cars-table SET (?,?,?,?,?) WHERE carid = ? ",(cardid, brand, model, year, price),cardid)
        database.commit()
        
    
car1=Car(101,"Toyota","Camry",2019,22000)

car1.create()
