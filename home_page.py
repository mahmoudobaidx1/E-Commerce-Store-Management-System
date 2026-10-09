import sqlite3


class home_page:
    def print_products(self):
        print("welcome to our store!")
        con = sqlite3.connect("store.db")
        cur = con.cursor()
        prd = cur.execute("select name, price,quantity from products").fetchall()
        print("product name               product price         quantity   ")
        for i in prd:
            print(f"\n {i[0]}               {i[1]}        {i[2]}")



    def add_to_cart(self):
        self.print_products()

        while True:
            try:

                p_client = input("what do you want to buy? ")
                am_client = int(input("enter amount: "))
                con = sqlite3.connect("store.db")
                cur = con.cursor()

                pro_name = cur.execute("select name,price,quantity from products").fetchall()


                found=False
                for i in pro_name:

                    if i[0] == p_client.lower().strip():
                        found=True
                        if am_client <= i[2]:
                            cur.execute(
                                "insert into cart(name,price,amount,total) values('{}','{}','{}','{}')".format(i[0],
                                                                                                               i[1],
                                                                                                               am_client,
                                                                                                               i[
                                                                                                                   1] * am_client))
                            con.commit()
                        else:
                            print("amount out of range")
                if found==False:
                    print("product not found ")


            except:
                print("wrong input")


os = home_page()
os.add_to_cart()
