import mysql.connector
conn = mysql.connector.connect(host='localhost',password='saad2012#S',user='root',database='library')

if conn.is_connected():
    print("connection established....")


def addbook():
    bn=input("enter book name:")
    c=input("enter book code:")
    t=input("total book:")
    s=input("enter subject:")
    data=(bn,c,t,s)
    sql = 'insert into books values(%s,%s,%s,%s)'
    c=conn.cursor()
    c.execute(sql,data)
    conn.commit()
    print(">.......................................................<")
    print("data entered sucessfully")
    main()


def issueb():
    n=input("enter name")
    r=input("enter regno")
    co=input("enter book code")
    d=input("enter date")
    a="insert into issue values(%s,%s,%s,%s)"
    data =(n,r,co,d)
    c=conn.cursor()
    c.execute(a,data)
    conn.commit()
    print(">------------------------------------------------------<")
    print("book issued to",n)
    bookup(co,-1)


def submitb():
    n=input("enter name:")
    r=input("enter regno")
    co=input("enter book codee")
    d=input("enter date:")
    a="insert into submit values(%s,%s,%s,%s)"
    data=(n,r,co,d)
    c=conn.cursor()
    c.execute(a,data)
    conn.commit()
    print(">------------------------------------------------------<")
    print("book  submitteed from :",n)
    bookup(co,1)


def bookup(co,u):
    a="select TOTAL from books where BCODE=%s"
    data=(co,)
    c=conn.cursor()
    c.execute(a,data)
    myresult=c.fetchone()
    t=myresult[0]+u
    sql="update books set TOTAL =%s where BCODE= %s"
    d=(t,co)
    c.execute(sql,d)
    conn.commit()
    main()

def dbook():
    ac=input("enter book code")
    a="delete from books where BCODE=%s"
    data=(ac,)
    c=conn.cursor()
    c.execute(a,data)
    conn.commit()
    main()


def dispbook():
    a="select * from books"
    c=conn.cursor()
    c.execute(a)
    myresult=c.fetchall()
    for i in myresult:
        print("book name:",i[0])
        print("book code:",i[1])
        print("total :",i[2])
        print(">-------------------------------------<")
    main()    


    
def main():
    print(""""
                         LIBRARY MANAGEMT SYSTEM
   1.ADD BOOK
   2.ISSUE BOOK
   3.SUBMIT BOOK
   4.DELETE BOOK
   5.DISPLAY BOOK
   """)
    choice =input ("enter task no:")
    print(">------------------------------------------------------------")
    if(choice =='1'):
        addbook()
    elif(choice =='2'):
        issueb()
    elif(choice=='3'):
        submitb()
    elif(choice =='5'):
        dispbook()
    else:
        print("wrong choice......")
        main()

def pswd():
    ps= input("enter password")
    if ps == "py123":
        main()
    else:
        print("wrong password")
        pswd()
pswd()        
        


