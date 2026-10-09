import sqlite3
class Admin:
    def add_to_products(self):
        con=sqlite3.connect("store.db")
        cur=con.cursor()
        p_name=input("enter product name: ")
        p_price=input("enter product price: ")
        p_qu=input("enter amount: ")
        cur.execute("insert into products(name,price,quantity) values('{}','{}','{}')".format(p_name.lower().strip(),p_price.lower().strip(),p_qu.lower().strip()))
        con.commit()
admin=Admin()
admin.add_to_products()
        

