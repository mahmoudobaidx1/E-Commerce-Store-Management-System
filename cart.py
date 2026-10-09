import sqlite3

class Cart:
    def __init__(self):
        print("cart category: ")
        con=sqlite3.connect("store.db")
        cur=con.cursor()
        self.cart= cur.execute("select * from cart").fetchall()
        print("product name          product price       amount        total")
        for i in self.cart:
            print(f"\n {i[0]}             {i[1]}             {i[2]}           {i[3]}")

    def change_amount(self):
        n=input("choose a product: ")
        new_am=int(input("enter new amount: "))
        con = sqlite3.connect("store.db")
        cur = con.cursor()
        c=self.cart
        q=cur.execute("select quantity from products where name='{}'".format(n.lower().strip())).fetchall()
        found=False
        for i in c:
            if i[0]==n.lower().strip():
                found=True
                for j in q:
                    if new_am<=j[0]:
                        cur.execute("update cart set amount='{}', total='{}' where name='{}'".format(new_am,i[1]*new_am,n.lower().strip()))
                        con.commit()
        if found==False:
            print("wrong input")
    def delete_item(self):
        n = input("choose a product: ")
        con = sqlite3.connect("store.db")
        cur = con.cursor()
        c=self.cart
        found=False
        for i in c:
            if i[0] == n.lower().strip():
                found = True
                cur.execute("delete from cart where name='{}'".format(n.lower().strip()))
                con.commit()
        if found==False:
            print("wrong input")
    def proceed_buying(self):
        con = sqlite3.connect("store.db")
        cur = con.cursor()

        total =cur.execute("select total from cart").fetchall()
        sum=0
        for i in total:
            sum=sum+i[0]
        print("your total is: "+str(sum))
        ans=input("proceed buying?[yes/no] ")
        if ans=="yes".strip().lower():
            am=cur.execute("select name,   amount from cart").fetchall()
            pro=cur.execute("select name, quantity from products").fetchall()
            for i,j in zip(am,pro):

                if i[0]==j[0]:
                    cur.execute("update products set quantity='{}' where name='{}' ".format(j[1]-i[1],j[0]))
                    con.commit()
            cur.execute("delete from cart")
            con.commit()
        elif ans=="no".lower().strip():
            print("ok")
        else:
            print("wrong input")

def main():
    cart=Cart()
    while True:
        cl=input("determine next step[change amount/delete item/proceed buying]: ")
        if cl=="change amount".lower():
            cart.change_amount()
        elif cl=="delete item".lower():
            cart.delete_item()
        elif cl=="proceed buying".lower():
            cart.proceed_buying()
        else:
            print("wrong input")

main()

            






