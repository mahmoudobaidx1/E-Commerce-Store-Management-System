import sqlite3
class Search:
    def __init__(self):

        ans= input("enter a product: ")
        self.ans=ans.lower().strip()
        con=sqlite3.connect("store.db")
        cur=con.cursor()
        a=cur.execute("select name ,price,quantity from products where name='{}'".format(self.ans.lower().strip())).fetchall()
        if a:
            print("product name           product price    quantity")
            for i in a:
                print(f"\n {i[0]}            {i[1]}       {i[2]}")

        else:
            print("cannot find product")

    def buy_item(self):
        p_client=self.ans

        ans1=input("do you want to add it to your cart?[yes/no] ")
        if ans1=="yes".strip().lower():

            am_client=int(input("enter amount"))

            con = sqlite3.connect("store.db")
            cur = con.cursor()

            pro_name = cur.execute("select name,price,quantity from products").fetchall()


            for i in pro_name:

                if i[0] == p_client.lower().strip():

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

        elif ans1=="no".lower().strip():
            print("ok")
        else:
            print("wrong input")



oa=Search()
oa.buy_item()
