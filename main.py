from config import MYSQL_USER, MYSQL_PASSWORD
import mysql.connector as c
import csv
import os

con = c.connect(
    host='localhost',
    user=MYSQL_USER,
    passwd=MYSQL_PASSWORD
)

cur=con.cursor()
pas="*"
def create():
    file=open("stocks.csv",'w',newline='')
    write=csv.writer(file)
    cur.execute('create database if not exists shop') 
    cur.execute('use shop')
    cur.execute("create table if not exists stocks(item_no integer not null unique,product char(15) not null,price integer,quantity integer,total integer)")
    n=int(input('no. of items to be added:'))
    for i in range(n):
        item=int(input('enter item-no of product:'))
        pname=input('enter the product name:')
        pr=int(input('enter the price:'))
        quan=int(input('enter quantity:'))
        tot=pr*quan
        cur.execute('insert into stocks values(%s,%s,%s,%s,%s)',(item,pname,pr,quan,tot))
        con.commit()
    cur.execute('select * from stocks order by item_no')
    data=cur.fetchall()
    for i in data:
        a=list(i)
        write.writerow(a)
    file.close()
def add():
    file1=open("stocks.csv",'a',newline='')
    write=csv.writer(file1) 
    cur.execute('use shop')
    item=int(input('enter item-no of product:'))
    pname=input('enter the product name:')
    pr=int(input('enter the price:'))
    quan=int(input('enter quantity:'))
    tot=pr*quan
    cur.execute('insert into stocks values(%s,%s,%s,%s,%s)',(item,pname,pr,quan,tot))
    con.commit()
    cur.execute('select * from stocks order by item_no')  
    file2=open("temp.csv",'w',newline='')
    w=csv.writer(file2)
    data=cur.fetchall()
    for i in data:
        a=list(i)
        w.writerow(a)
    file1.close()
    file2.close()
    os.remove('stocks.csv')  
    os.rename('temp.csv','stocks.csv')
def bill():
    cur.execute('use shop')
    f1=open('stocks.csv','r')
    f2=open('bill.csv','w+',newline='')    
    w=csv.writer(f2)
    r=csv.reader(f1)
    a1=[]
    for i in r:
        a1.append(i)    
    ch='y'
    a=1
    to=0
    while ch in 'yY':
        pro=input('enter product name:')
        quan=int(input('enter quantity:'))        
        for i in a1:
            if i[1]==pro:
                tot=int(i[2])*quan
                to+=tot
                w.writerow([a,pro,i[2],quan,tot])
                a+=1
                q=int(i[3])-quan
                t=int(i[2])*q
                cur.execute('update stocks set quantity=%s,total=%s where product=%s',(q,t,pro))
                con.commit()
        ch=input('want to buy more product(y/n)')
    cur.execute('select * from stocks order by item_no')
    file2=open("temp.csv",'w',newline='')
    w=csv.writer(file2)
    data=cur.fetchall()
    for i in data:
        a=list(i)
        w.writerow(a)
    f1.close()
    file2.close()
    os.remove('stocks.csv')
    os.rename('temp.csv','stocks.csv') 
    f2.close()
    f3=open('bill.csv','r')
    r2=csv.reader(f3)
    print('='*80,'\n\t\t\t\t\tBILL\n','='*80)
    print('sl.no\t\tproduct\t\tprice\t\tquantity\t\ttotal')
    for i in r2:
        for j in i:
            print(j,end='\t\t')
        print()
    print('='*80,'\n\t\t\t\t\t\t\t\tG.total=',to,'\n','='*80)
    f3.close()
    os.remove('bill.csv')
def drop():
    pro=input('enter the name of exhausted product:')
    cur.execute('use shop')
    cur.execute('delete from stocks where product=%s',(pro,))
    con.commit()
    file1=open('stocks.csv','r',newline='')
    r=csv.reader(file1)
    file2=open('temp.csv','w',newline='')
    write=csv.writer(file2) 
    l=[]
    for i in r:
        l.append(i)
    for i in l:
        if i[1]!=pro:
            a=list(i)
            write.writerow(a)
    file1.close()
    file2.close()
    os.remove('stocks.csv')  
    os.rename('temp.csv','stocks.csv')    
def update():
    ch1='y'
    while ch1 in 'yY':
        ch2=int(input('enter \n1)to update price\n2)to update quantity\n:->'))
        if ch2==1:
           pro=input("Enter the product name :")
           n_price=int(input("Enter New price:"))
           f1=open('stocks.csv','r',newline='')
           r=csv.reader(f1)
           l=[]
           for i in r:
               l.append(i)
           f1.close()
           for i in l:
                if i[1]==pro:
                   i[2]=n_price
                   t1=i[2]*int(i[3])
                   i[4]=t1
           print("Record updated")
           f2=open('temp.csv','w',newline='')
           w=csv.writer(f2)
           for i in l:
                w.writerow(i)
           f2.close()
           os.remove('stocks.csv')
           os.rename('temp.csv','stocks.csv')
           cur.execute('use shop')
           cur.execute('update stocks set price=%s,total=%s where product=%s',(n_price,t1,pro))
           con.commit()                      
        if ch2==2:
           pro=input("Enter the product name :")
           q=int(input("Enter New quantity:"))
           f3=open('stocks.csv','r',newline='')
           r=csv.reader(f3)
           l=[]
           for i in r:
               l.append(i)
           f3.close()
           for i in l:
                if i[1]==pro:
                   i[3]=q
                   t=int(i[2])*i[3]
                   i[4]=t
           print("Record updated")
           f4=open('temp.csv','w',newline='')
           w=csv.writer(f4)
           for i in l:
                w.writerow(i)
           f4.close()
           os.remove('stocks.csv')
           os.rename('temp.csv','stocks.csv')
           cur.execute('use shop')
           cur.execute('update stocks set quantity=%s,total=%s where product=%s',(q,t,pro))
           con.commit()
        ch1=input('anymore update(y/n):')
def show():
    file=open('stocks.csv','r')
    read=csv.reader(file)
    print("Product no.\tProduct name\tPrice\t\tQuantity\t\tAmount")
    for i in read:
        for j in i:
            print(j,end="\t\t")
        print()
    file.close()
def menu():
    while True:
        print('='*80,"\n\t\tWelcome to Sales And Inventory Management System")
        print("="*80,"\n1.Admin\n2.Customer\n3.First time user\n4.Exit")
        ch_m=int(input("Enter your choice:"))
        if ch_m==1:
              p=input("Enter password:")
              if p==pas:
                   print('='*80,'\n\t\t\t\tWelcome !')
                   l1='y'
                   while l1=='y' or l1=='Y':
                        print('='*80,"""\n1.Add New Item
2.Updating price/quantity
3.Deleting item
4.Display All Items
5.Change Password
6.Log Out""")
                        ch_a=int(input("Enter your choice:"))
                        if ch_a==1:
                             l2='y'
                             while l2=='y' or l2=='Y':
                                 add()
                                 l2=input("Do you want to add more item(y/n):")
                             l1=input("Do you want to continue editing stock(y/n):")
                        elif ch_a==2:
                             update()
                             l1=input("Do you want to continue with editing stock(y/n):")
                        elif ch_a==3:
                             l4='y'
                             while l4=='y' or l4=='Y':
                                 drop()
                                 l4=input("Do you want to delete more items (y/n):")
                             l1=input("Do you want to continue with editing stock(y/n):")
                        elif ch_a==4:
                            show()
                        elif ch_a==5:
                             old_pass=input("Enter Old Password:")
                             if old_pass==pas:
                                  new_pass=input("Enter new password:")
                                  pas==new_pass
                                  print("Password Updated . . . ")
                        elif ch_a==6:
                            break
              else:
                   print("Wrong password !")
        elif ch_m==2:
            show()
            bill()
        elif ch_m==3:
            create()
        elif ch_m==4:
            print(''*20,'Thank you, Visit Again',''*20)
            exit()
menu()
