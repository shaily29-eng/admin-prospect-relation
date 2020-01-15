import mysql.connector
def add_prospect():
    db = mysql.connector.connect(host='192.168.43.14', database='kiit_db', user='root', password='password')
    mycursor = db.cursor()
    pn = input("enter prospect name")
    ph = input("enter phone no.")
    pa = input("enter prospect address.")
    im= input("enter prospect interested model")
    ic = input("enter interested color")
    dov= input("enter date of visit")
    h = input("enter hotness of prospect")

    sql = "insert into prospect(prospName,prospPhone, prospAddress, interestedModel,interestedColor, dateofvisit)values('%s', '%s','%s','%s','%s','%s','%s')"
    values = (pn,ph,pa,im,ic,dov,h)
    #print("sql=", sql%values)
    mycursor.execute(sql%values)
    print("prospect data inserted successfully form ")
    mycursor.close()
    db.commit()
def view_users_emp():
    db = mysql.connector.connect(host='192.168.43.14', database='kiit_db', user='root', password='password')
    mycursor = db.cursor()
    sql="select * from employee"

    mycursor.execute(sql)
    for row in mycursor:
        print(row)
    db.commit()

def view_prospect():
    db = mysql.connector.connect(host='192.168.43.14', database='kiit_db', user='root', password='password')
    mycursor = db.cursor()

    sql = "select * from prospect"

    mycursor.execute(sql)
    for row in mycursor:
        print(row)
    db.commit()


def update_prospect(b):
    db = mysql.connector.connect(host='192.168.43.14', database='kiit_db', user='root', password='password')
    mycursor = db.cursor()
    if(b==2):
     sql = "update prospect set prospPhone = '%s' where prospId=%d"
     ro = int(input("enter Prospect ID  whose phone no. is to be updated"))
     ph = input("enter new phone no.")
     values = (ph,ro)
     mycursor.execute(sql%values)
     db.commit()

     if mycursor.rowcount == 1:
        print("record updated successfully", ro)
     else:
        print("record updation failed retry")
     db.close()
    if (b == 4):
        sql = "update prospect set interestedModel = '%s' where prospId=%d"
        ro = int(input("enter Prospect ID  whose model is to be updated"))
        ph = input("enter new model no.")
        values = (ph, ro)

        mycursor.execute(sql%values)
        db.commit()

        if mycursor.rowcount == 1:
            print("record updated successfully", ro)
        else:
            print("record updation failed retry")
        db.close()

    if (b == 5):
        sql = "update prospect set interestedColor = '%s' where prospId=%d"
        ro = int(input("enter Prospect ID  whose color is to be updated"))
        ph = input("enter new color")
        values = (ph, ro)

        mycursor.execute(sql%values)
        db.commit()

        if mycursor.rowcount == 1:
            print("record updated successfully", ro)
        else:
            print("record updation failed retry")
        db.close()
    if (b == 7):
        sql = "update prospect set hotness = '%s' where prospId=%d"
        ro = int(input("enter Prospect ID  whose hotness is to be updated"))
        ph = input("enter new hotness ")
        values = (ph,ro)

        mycursor.execute(sql%values)
        db.commit()

        if mycursor.rowcount == 1:
            print("record updated successfully", ro)
        else:
            print("record updation failed retry")
        db.close()
def search_prospect(c):
    if(c==7):
        db = mysql.connector.connect(host='192.168.43.14', database='kiit_db', user='root', password='password')
        mycursor = db.cursor()
        hot1=input("enter the hotness level")
        sql= "select * from prospect where hotness = '%s'"
        values=(hot1)
        mycursor.execute(sql%values)
        for row in mycursor:
            print(row)
        db.commit()
    if(c==0):
        db = mysql.connector.connect(host='192.168.43.14', database='kiit_db', user='root', password='password')
        mycursor = db.cursor()
        h1 = int(input("enter the prospect id"))
        sql = "select * from prospect where prospId =%d"
        values =(h1)
        mycursor.execute(sql%values)
        for row in mycursor:
            print(row)
        db.commit()
def change_password():
    db = mysql.connector.connect(host='192.168.43.14', database='kiit_db', user='root', password='password')
    mycursor = db.cursor()
    sql = "update employee set userPass = '%s' where userName='%s'"
    ro = input("enter  your employee ID  to change password")
    ph = input("enter new password")
    values = (ph,ro)

    mycursor.execute(sql%values)
    db.commit()

    if mycursor.rowcount == 1:
        print("record updated successfully", ro)
    else:
        print("record updation failed retry")
    db.close()

def create_user():
    db = mysql.connector.connect(host='192.168.43.14', database='kiit_db', user='root', password='password')
    mycursor = db.cursor()
    pn = input("enter unique user name")
    ph = input("enter new password.")
    pa = input("enter usertype.")
    im = input("enter your full name")
    ic = input("enter your phone number")
    dov = input("enter your email id")
    h = input("enter your status")

    sql = "insert into employee(userName,userPass, userType, fullName,phone,email,status)values('%s','%s','%s','%s','%s','%s','%s')"
    values = (pn, ph, pa, im, ic, dov, h)
    print("sql=",sql%values)
    mycursor.execute(sql%values)
    print("employee data inserted successfully  ")
    mycursor.close()
    db.commit()


def change_own_password(y):
    if(y==1):
        db = mysql.connector.connect(host='192.168.43.14', database='kiit_db', user='root', password='password')
        mycursor = db.cursor()
        sql = "update employee set userPass = '%s' where userName='%s'"
        ro = input("enter  your employee ID  to change password")
        ph = input("enter new password")
        values = (ph,ro)

        mycursor.execute(sql%values)
        db.commit()

        if mycursor.rowcount == 1:
            print("record updated successfully", ro)
        else:
            print("record updation failed retry")
        db.close()
    if(y==2):
        db = mysql.connector.connect(host='192.168.43.14', database='kiit_db', user='root', password='password')
        mycursor = db.cursor()
        sql = "update employee set userPass = '%s' where userName='%s'"
        ro = input("enter  employee id to change password")
        ph = input("enter new password")
        values = (ph,ro)

        mycursor.execute(sql%values)
        db.commit()

        if mycursor.rowcount == 1:
            print("record updated successfully", ro)
        else:
            print("record updation failed retry")
        db.close()
def ac_deac():
    db = mysql.connector.connect(host='192.168.43.14', database='kiit_db', user='root', password='password')
    mycursor = db.cursor()
    sql = "update employee set status = '%s' where userName='%s'"
    ro = input("enter  employee id to change status")
    ph = input("enter new status ")
    values = (ph,ro)

    mycursor.execute(sql%values)
    db.commit()

    if mycursor.rowcount == 1:
        print("record updated successfully",ro)
    else:
        print("record updation failed retry")
    db.close()








def employeelogin():
    uname = input("enter username")
    upassword = input("enter user password")
    db= mysql.connector.connect(host='192.168.43.14',database='kiit_db', user='root',password='password')
    mycursor=db.cursor()
    sql="select * from employee where username= '%s'"
    values=(uname)
    mycursor.execute(sql%values)
    #print("Prospect Encore")
    try:
        row=mycursor.fetchmany(1)[0]
        dbpass=row[1]
        if upassword == dbpass:
            print("login authentication success....")
            usertype=row[2]
            if usertype=="admin":
                print("welcome administrator")
                print("press 1: create user account")
                print("press 2: view all users")
                print("press 3: view all prospects")
                print("press 4: change the password")
                print("press 5: search the prospect")
                print("press 6: activate/deactivate the account")
                print("press 7: signout")
                z=int(input("enter your choice"))
                if(z==1):
                    w=int(input("enter 1 for creating monitor account and 2 for user"))
                    create_user()
                if(z==2):
                    view_users_emp()
                if(z==3):
                    view_prospect()
                if(z==4):
                    y=int(input("enter 1 for changing own password and 2 for others"))
                    change_own_password(y)
                if(z==5):
                    c = int(input("enter 7 for search by hotness, 0 for search by prospect id"))
                    search_prospect(c)

                if(z==6):
                    ac_deac()
                if(z==7):
                    print("Software Shutting down \n Developed By: Shaily Goyal,Lakshmi Srivastava,Anushka Singh Bhardwaj and Aunkita Mandal")


            else:
                print("welcome prospect monitor")
                print("press 1: add new prospect")
                print("press 2:view all prospects")
                print("press 3:update the prospect")
                print("press 4:for search prospect")
                print("press 5:change own password")
                print("press 6:signout")
                a=int(input("enter your choice"))
                if(a==1):
                    add_prospect()
                if(a==2):
                    view_prospect()
                if(a==3):
                    b=int(input("enter 2 update phone number,4 for model update, 5 for color update, 7 for hotness update"))
                    update_prospect(b)
                if(a==4):
                    c=int(input("enter 7 for search by hotness, 0 for search by prospect id"))
                    search_prospect(c)
                if(a==5):
                    change_password()
                if(a==6):
                    print("Software Shutting down \n Developed By: Shaily Goyal,Lakshmi Srivastava,Anushka Singh Bhardwaj and Aunkita Mondal")



        else:
            print("login authentication failed")
    except IndexError:
        print("invalid user name retry")
    db.commit()
    db.close()
employeelogin()
