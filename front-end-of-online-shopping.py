#!/usr/bin/env python
# coding: utf-8

# In[88]:


import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',passwd='hanith1362')


# In[21]:





# In[91]:


print("WELCOME TO ONLINE SHOPPING PLATFORM \n")
print("press 1 to register\n","press 2 to Login")
n=int(input("enter the number for above operation:"))
if(n==1):
    print("Hai Buddy welcome.........")
    n1=input("please enter the username:")
    n2=int(input("please enter the password:"))
    n3=input("please enter the name:")
    n4=input("please enter the phone Number:")
    n5=input("please enter the mail:")
    mycursor=mydb.cursor()
    mycursor.execute('use customerdatabase2')
    sql='insert into customercredentials(cus_username,cus_password,cus_name,cus_phone_number,cus_email) values(%s,%s,%s,%s,%s)'
    val=(n1,n2,n3,n4,n5)
    mycursor.execute(sql,val)
    mydb.commit()
if(n==2):
    print("LOGIN here: \n")
    m1=input("Please enter the username:")
    m2=int(input("please enter the password:"))
    mycursor=mydb.cursor()
    mycursor.execute('use customerdatabase2')
    sql='select * from customercredentials ;'
    mycursor.execute(sql)
    a=mycursor.fetchall()
    for i in range(len(a)):
        if a[i][1]==m1 and a[i][2]==m2:
            print("login successful \n")
            b=list(a[i])
            print("WELCOME ",a[i][3])
            print("enter 1 to purchase fruits from seller1:\n","enter 2 to purchase cosmetics from seller2:\n","enter 3 to purchase clothing from seller3:\n")
            s=int(input("enter the operation to purchase:"))
            if(s==1):
                mycursor1=mydb.cursor()
                mycursor1.execute('use sellerdatabase2')
                sql='select * from seller1 ;'
                mycursor1.execute(sql)
                a1=mycursor1.fetchall()
                for row in a1:
                    print(row)
                p=int(input("Enter the product Id to purchase:"))
                if(p==1):
                    for i in range(len(a1)):
                        if a1[i][4]==p:
                            l1=list(a1[i])
                    q1=int(input("you are going to buy apples please enter quantity to the cart:"))
                    if(q1<=a1[0][10]):
                        print("Required quantity of apples are added in to the cart:",q1)
                        c1=q1*(a1[0][7])
                        print("cart value is:",c1)
                        mycursor1=mydb.cursor()
                        mycursor1.execute('use sellerdatabase2')
                        sql='update seller1 set pro_sold=%s,pro_left=%s where product_Id=1'
                        val=(q1,l1[10]-q1)
                        mycursor1.execute(sql,val)
                        mydb.commit()
                        mycursor2=mydb.cursor()
                        mycursor2.execute('use maindatabase2')
                        sql1='insert into maindata(name_seller,email,licence_No,seller_phone_number,product_Id,product_cat,pro_name,pro_price,pro_quantity,spent_amount_by_customer,pro_desc,customer_Id,cus_username,cus_password,cus_name,cus_phone_number,cus_email) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
                        val1=(l1[0],l1[1],l1[2],l1[3],l1[4],l1[5],l1[6],l1[7],q1,c1,l1[8],b[0],b[1],b[2],b[3],b[4],b[5])
                        mycursor2.execute(sql1,val1)
                        mydb.commit()
                    else:
                        print("Required Quantity of product is not availabe")
                elif(p==2):
                    for i in range(len(a1)):
                        if a1[i][4]==p:
                            l2=list(a1[i])
                    q2=int(input("you are going to buy bananas please enter quantity to the cart:"))
                    if(q2<=a1[1][10]):
                        print("Required quantity of bananas are added in to the cart:",q2)
                        c2=q2*(a1[1][7])
                        print("cart value is:",c2)
                        mycursor1=mydb.cursor()
                        mycursor1.execute('use sellerdatabase2')
                        sql='update seller1 set pro_sold=%s,pro_left=%s where product_Id=2'
                        val=(q2,l2[10]-q2)
                        mycursor1.execute(sql,val)
                        mydb.commit()
                        mycursor2=mydb.cursor()
                        mycursor2.execute('use maindatabase2')
                        sql1='insert into maindata(name_seller,email,licence_No,seller_phone_number,product_Id,product_cat,pro_name,pro_price,pro_quantity,spent_amount_by_customer,pro_desc,customer_Id,cus_username,cus_password,cus_name,cus_phone_number,cus_email) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
                        val1=(l2[0],l2[1],l2[2],l2[3],l2[4],l2[5],l2[6],l2[7],q2,c2,l2[8],b[0],b[1],b[2],b[3],b[4],b[5])
                        mycursor2.execute(sql1,val1)
                        mydb.commit()
                    else:
                        print("Required Quantity of product is not availabe")
                elif(p==3):
                    for i in range(len(a1)):
                        if a1[i][4]==p:
                            l3=list(a1[i])
                    q3=int(input("you are going to buy oranges please enter quantity to the cart:"))
                    if(q3<=a1[2][10]):
                        print("Required quantity of oranges are added in to the cart:",q3)
                        c3=q3*(a1[2][7])
                        print("cart value is:",c3)
                        mycursor1=mydb.cursor()
                        mycursor1.execute('use sellerdatabase2')
                        sql='update seller1 set pro_sold=%s,pro_left=%s where product_Id=3'
                        val=(q3,l3[10]-q3)
                        mycursor1.execute(sql,val)
                        mydb.commit()
                        mycursor2=mydb.cursor()
                        mycursor2.execute('use maindatabase2')
                        sql1='insert into maindata(name_seller,email,licence_No,seller_phone_number,product_Id,product_cat,pro_name,pro_price,pro_quantity,spent_amount_by_customer,pro_desc,customer_Id,cus_username,cus_password,cus_name,cus_phone_number,cus_email) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
                        val1=(l3[0],l3[1],l3[2],l3[3],l3[4],l3[5],l3[6],l3[7],q3,c3,l3[8],b[0],b[1],b[2],b[3],b[4],b[5])
                        mycursor2.execute(sql1,val1)
                        mydb.commit()
                
                    else:
                        print("Required Quantity of product is not availabe")
                else:
                    print("sorry this product is not available with this seller")
            elif(s==2):
                mycursor1=mydb.cursor()
                mycursor1.execute('use sellerdatabase2')
                sql='select * from seller2 ;'
                mycursor1.execute(sql)
                a1=mycursor1.fetchall()
                for row in a1:
                    print(row)
                p=int(input("Enter the product Id to purchase:"))
                if(p==1):
                    for i in range(len(a1)):
                        if a1[i][4]==p:
                            l1=list(a1[i])
                    q1=int(input("you are going to buy soap please enter quantity to the cart:"))
                    if(q1<=a1[0][10]):
                        print("Required quantity of soap are added in to the cart:",q1)
                        c1=q1*(a1[0][7])
                        print("cart value is:",c1)
                        mycursor1=mydb.cursor()
                        mycursor1.execute('use sellerdatabase2')
                        sql='update seller2 set pro_sold=%s,pro_left=%s where product_Id=1'
                        val=(q1,l1[10]-q1)
                        mycursor1.execute(sql,val)
                        mydb.commit()
                        mycursor2=mydb.cursor()
                        mycursor2.execute('use maindatabase2')
                        sql1='insert into maindata(name_seller,email,licence_No,seller_phone_number,product_Id,product_cat,pro_name,pro_price,pro_quantity,spent_amount_by_customer,pro_desc,customer_Id,cus_username,cus_password,cus_name,cus_phone_number,cus_email) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
                        val1=(l1[0],l1[1],l1[2],l1[3],l1[4],l1[5],l1[6],l1[7],q1,c1,l1[8],b[0],b[1],b[2],b[3],b[4],b[5])
                        mycursor2.execute(sql1,val1)
                        mydb.commit()
                    else:
                        print("Required Quantity of product is not availabe")
                elif(p==2):
                    for i in range(len(a1)):
                        if a1[i][4]==p:
                            l2=list(a1[i])
                    q2=int(input("you are going to buy face_wash please enter quantity to the cart:"))
                    if(q2<=a1[1][10]):
                        print("Required quantity of face_wash are added in to the cart:",q2)
                        c2=q2*(a1[1][7])
                        print("cart value is:",c2)
                        mycursor1=mydb.cursor()
                        mycursor1.execute('use sellerdatabase2')
                        sql='update seller2 set pro_sold=%s,pro_left=%s where product_Id=2'
                        val=(q2,l2[10]-q2)
                        mycursor1.execute(sql,val)
                        mydb.commit()
                        mycursor2=mydb.cursor()
                        mycursor2.execute('use maindatabase2')
                        sql1='insert into maindata(name_seller,email,licence_No,seller_phone_number,product_Id,product_cat,pro_name,pro_price,pro_quantity,spent_amount_by_customer,pro_desc,customer_Id,cus_username,cus_password,cus_name,cus_phone_number,cus_email) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
                        val1=(l2[0],l2[1],l2[2],l2[3],l2[4],l2[5],l2[6],l2[7],q2,c2,l2[8],b[0],b[1],b[2],b[3],b[4],b[5])
                        mycursor2.execute(sql1,val1)
                        mydb.commit()
                    else:
                        print("Required Quantity of product is not availabe")
                elif(p==3):
                    for i in range(len(a1)):
                        if a1[i][4]==p:
                            l3=list(a1[i])
                    q3=int(input("you are going to buy face_wipes please enter quantity to the cart:"))
                    if(q3<=a1[2][10]):
                        print("Required quantity of face_wipes are added in to the cart:",q3)
                        c3=q3*(a1[2][7])
                        print("cart value is:",c3)
                        mycursor1=mydb.cursor()
                        mycursor1.execute('use sellerdatabase2')
                        sql='update seller2 set pro_sold=%s,pro_left=%s where product_Id=3'
                        val=(q3,l3[10]-q3)
                        mycursor1.execute(sql,val)
                        mydb.commit()
                        mycursor2=mydb.cursor()
                        mycursor2.execute('use maindatabase2')
                        sql1='insert into maindata(name_seller,email,licence_No,seller_phone_number,product_Id,product_cat,pro_name,pro_price,pro_quantity,spent_amount_by_customer,pro_desc,customer_Id,cus_username,cus_password,cus_name,cus_phone_number,cus_email) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
                        val1=(l3[0],l3[1],l3[2],l3[3],l3[4],l3[5],l3[6],l3[7],q3,c3,l3[8],b[0],b[1],b[2],b[3],b[4],b[5])
                        mycursor2.execute(sql1,val1)
                        mydb.commit()
                    else:
                        print("Required Quantity of product is not availabe")
                else:
                    print("sorry this product is not available with this seller")
            elif(s==3):
                mycursor1=mydb.cursor()
                mycursor1.execute('use sellerdatabase2')
                sql='select * from seller3 ;'
                mycursor1.execute(sql)
                a1=mycursor1.fetchall()
                for row in a1:
                    print(row)
                p=int(input("Enter the product Id to purchase:"))
                if(p==1):
                    for i in range(len(a1)):
                        if a1[i][4]==p:
                            l1=list(a1[i])
                    q1=int(input("you are going to buy shirts please enter quantity to the cart:"))
                    if(q1<=a1[0][10]):
                        print("Required quantity of shirts are added in to the cart:",q1)
                        c1=q1*(a1[0][7])
                        print("cart value is:",c1)
                        mycursor1=mydb.cursor()
                        mycursor1.execute('use sellerdatabase2')
                        sql='update seller3 set pro_sold=%s,pro_left=%s where product_Id=1'
                        val=(q1,l1[10]-q1)
                        mycursor1.execute(sql,val)
                        mydb.commit()
                        mycursor2=mydb.cursor()
                        mycursor2.execute('use maindatabase2')
                        sql1='insert into maindata(name_seller,email,licence_No,seller_phone_number,product_Id,product_cat,pro_name,pro_price,pro_quantity,spent_amount_by_customer,pro_desc,customer_Id,cus_username,cus_password,cus_name,cus_phone_number,cus_email) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
                        val1=(l1[0],l1[1],l1[2],l1[3],l1[4],l1[5],l1[6],l1[7],q1,c1,l1[8],b[0],b[1],b[2],b[3],b[4],b[5])
                        mycursor2.execute(sql1,val1)
                        mydb.commit()
                    else:
                        print("Required Quantity of product is not availabe")
                elif(p==2):
                    for i in range(len(a1)):
                        if a1[i][4]==p:
                            l2=list(a1[i])
                    q2=int(input("you are going to buy jeans please enter quantity to the cart:"))
                    if(q2<=a1[1][10]):
                        print("Required quantity of jeans are added in to the cart:",q2)
                        c2=q2*(a1[1][7])
                        print("cart value is:",c2)
                        mycursor1=mydb.cursor()
                        mycursor1.execute('use sellerdatabase2')
                        sql='update seller3 set pro_sold=%s,pro_left=%s where product_Id=2'
                        val=(q2,l2[10]-q2)
                        mycursor1.execute(sql,val)
                        mydb.commit()
                        mycursor2=mydb.cursor()
                        mycursor2.execute('use maindatabase2')
                        sql1='insert into maindata(name_seller,email,licence_No,seller_phone_number,product_Id,product_cat,pro_name,pro_price,pro_quantity,spent_amount_by_customer,pro_desc,customer_Id,cus_username,cus_password,cus_name,cus_phone_number,cus_email) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
                        val1=(l2[0],l2[1],l2[2],l2[3],l2[4],l2[5],l2[6],l2[7],q2,c2,l2[8],b[0],b[1],b[2],b[3],b[4],b[5])
                        mycursor2.execute(sql1,val1)
                        mydb.commit()
                    else:
                        print("Required Quantity of product is not availabe")
                elif(p==3):
                    for i in range(len(a1)):
                        if a1[i][4]==p:
                            l3=list(a1[i])
                    q3=int(input("you are going to buy T-shirts please enter quantity to the cart:"))
                    if(q3<=a1[2][10]):
                        print("Required quantity of T-shirts are added in to the cart:",q3)
                        c3=q3*(a1[2][7])
                        print("cart value is:",c3)
                        mycursor1=mydb.cursor()
                        mycursor1.execute('use sellerdatabase2')
                        sql='update seller3 set pro_sold=%s,pro_left=%s where product_Id=3'
                        val=(q3,l3[10]-q3)
                        mycursor1.execute(sql,val)
                        mydb.commit()
                        mycursor2=mydb.cursor()
                        mycursor2.execute('use maindatabase2')
                        sql1='insert into maindata(name_seller,email,licence_No,seller_phone_number,product_Id,product_cat,pro_name,pro_price,pro_quantity,spent_amount_by_customer,pro_desc,customer_Id,cus_username,cus_password,cus_name,cus_phone_number,cus_email) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
                        val1=(l3[0],l3[1],l3[2],l3[3],l3[4],l3[5],l3[6],l3[7],q3,c3,l3[8],b[0],b[1],b[2],b[3],b[4],b[5])
                        mycursor2.execute(sql1,val1)
                        mydb.commit()
                    else:
                        print("Required Quantity of product is not availabe")
                else:
                    print("sorry this product is not available with this seller")
                
            else:
                print("No seller with this operation")
            
else:
    print("Invalid credentials")


# In[ ]:





# In[ ]:





# In[75]:





# In[ ]:




