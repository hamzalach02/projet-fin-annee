from tkinter import *
from PIL import Image,ImageTk
import os
import mysql.connector
import tk


root = Tk()
root.geometry("800x600")





class m :
    
    def __init__(self,master):
        
        
        

        
        #buttons 

        

        self.firstpage()
        
    def firstpage(self):
        global myFrame
        myFrame=Frame(bg="#369E98")
        myFrame.pack()
        myFrame.place(x=50,y=50,width=700,height=500)
        #presentation de l application

        left_frame=Frame(myFrame,bg="#C4E3E1")
        left_frame.pack()
        left_frame.place(x=0,y=0,width=400,height=500)
        titre = Label(left_frame, text="application gestion de stock",font=("Trajan Pro",18,"bold"),bg="#C4E3E1",fg="#708685")  
        titre.pack()
        titre.place(x=25,y=50)
        text_label=Label(left_frame,text="Lorsqu'une entreprise gère des stocks, il est essentiel de disposer d'un système efficace pour suivre et contrôler les mouvements des articles. Une application de gestion de stock peut aider à automatiser et à simplifier ce processus.",font=("Trajan Pro",10,"bold"),bg="#C4E3E1",fg="#485E5D",wraplength=300, padx=10)
        text_label.pack()
        text_label.place(x=40,y=130)
        text2_label=Label(left_frame,text="Projet de : Hamza Lachgar,Ayoub Marhrani,Achraf Essaadi",font=("Trajan Pro",10,"bold"),bg="#C4E3E1",fg="#485E5D",wraplength=320, padx=10)
        text2_label.pack()
        text2_label.place(x=60,y=340)

           #login as user
        self.button1 = Button(myFrame,text="login as user" ,bg="#FF5733",font=("Trajan Pro",10,"bold"),command=self.login)
        self.button1.pack()
        self.button1.place(x=480,y=120,height=40,width=130)
        
        #register user
        self.button2 = Button(myFrame,bg="#FF5733",text="register ",font=("Trajan Pro",10,"bold"),command=self.register)
        self.button2.pack()
        self.button2.place(x=480,y=220,height=40,width=130)


        #login as admin
        self.button2 = Button(myFrame,bg="#FF5733",text="login as admin ",font=("Trajan Pro",10,"bold"),command=self.login_admin)
        self.button2.pack()
        self.button2.place(x=480,y=320,height=40,width=130)
        
    def register(self):

     

    #variables def
       global frame1
       frame1=Frame(bg="#369E98")
       frame1.pack()
       frame1.place(x=50,y=50,width=700,height=500)
       global username
       global password
       global Cpassword
       username = StringVar()
       password = StringVar()
       Cpassword = StringVar()
       
    #text(left frame)
       left_frame=Frame(frame1,bg="#C4E3E1")
       left_frame.pack()
       left_frame.place(x=0,y=0,width=400,height=500)
       titre = Label(left_frame, text="application gestion de stock",font=("Trajan Pro",18,"bold"),bg="#C4E3E1",fg="#708685")  
       titre.pack()
       titre.place(x=25,y=50)
       text_label=Label(left_frame,text="Lorsque vous remplissez des formulaires avec des champs de mot de passe et de confirmation de mot de passe, il est important de vous assurer que les deux champs correspondent. Voici quelques conseils pour vous aider à remplir ces champs correctement.",font=("Trajan Pro",10,"bold"),bg="#C4E3E1",fg="#485E5D",wraplength=300, padx=10)
       text_label.pack()
       text_label.place(x=40,y=130)

    #register label
       register_label = Label(frame1, text="register",font=("Trajan Pro",20,"bold"))  
       register_label.pack()
       register_label.place(x=480,y=30)
    #username label 
       username_label = Label(frame1, text="Username * ")
       username_label.pack()
       username_label.place(x=480,y=70)
       username_entry = Entry(frame1,textvariable=username)
       username_entry.pack()
       username_entry.place(x=480,y=110)
    #password label
       password_label = Label(frame1, text="password * ")
       password_label.pack()
       password_label.place(x=480,y=150)
       password_entry = Entry(frame1,show="*",textvariable=password)
       password_entry.pack()
       password_entry.place(x=480,y=180)

    #confirm password label
       Cpassword_label = Label(frame1, text="confirm password * ")
       Cpassword_label.pack()
       Cpassword_label.place(x=480,y=210)
       Cpassword_entry = Entry(frame1,show="*",textvariable=Cpassword)
       Cpassword_entry.pack()
       Cpassword_entry.place(x=480,y=250)
       

    #button registration
       button3 = Button(frame1,bg="#FF5733",text="register ",command=self.register_user,font=("Trajan Pro",10,"bold"))
       button3.pack()
       button3.place(x=480,y=280,height=40,width=130)
    #button homme
       button4 = Button(frame1,bg="#FF5733",text="home ",command=self.firstpage,font=("Trajan Pro",10,"bold"))
       button4.pack()
       button4.place(x=480,y=350,height=40,width=130)



       myFrame.destroy()
       

    def connect_to_database(self):
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="gestion_stock"
        )
        return mydb     

    def register_user(self):
        username_cf = username.get()
        password_cf = password.get()
        Cpassword_cf = Cpassword.get()

       
        #check out the entries
        if username_cf == "" or password_cf == "" or Cpassword_cf =="":
           lb1 = Label(frame1, text="please fill in all required fields", fg="red", font=("calibri", 11)).place(x=100,y=260)
           lb1.pack()

        elif password_cf != Cpassword_cf:
           lb2 =  Label(frame1, text="not the same password", fg="red", font=("calibri", 11)).place(x=100,y=260)
           lb2.pack()
        #insert to table (userinfo)
        else : 
            

            # Establish a connection to the MySQL server
            mydb = self.connect_to_database()
            # Create a cursor object to interact with the database
            mycursor = mydb.cursor()

            

            # Define the SQL query to insert a new row into the table
            sql = "INSERT INTO userinfo (username, password) VALUES (%s, %s)"
            val = (username_cf, password_cf)

            # Execute the query and commit the changes
            mycursor.execute(sql, val)
            mydb.commit()
            Label(frame1, text="Registration Success", fg="green", font=("calibri", 11)).place(x=100,y=260,width=200)
     


         


    def login(self):
       global username
       global password
       global frame2
       frame2=Frame(bg="#369E98")
       frame2.pack()
       frame2.place(x=50,y=50,width=700,height=500)

       #text(left frame)
       left_frame=Frame(frame2,bg="#C4E3E1")
       left_frame.pack()
       left_frame.place(x=0,y=0,width=400,height=500)
       titre = Label(left_frame, text="application gestion de stock",font=("Trajan Pro",18,"bold"),bg="#C4E3E1",fg="#708685")  
       titre.pack()
       titre.place(x=25,y=50)
       text_label=Label(left_frame,text="Lorsque vous remplissez une page de connexion avec des champs de nom d'utilisateur et de mot de passe, il est important de prendre certaines mesures pour protéger votre compte. ",font=("Trajan Pro",10,"bold"),bg="#C4E3E1",fg="#485E5D",wraplength=300, padx=10)
       text_label.pack()
       text_label.place(x=40,y=130)
       #variables
       username = StringVar()
       password = StringVar()
       #login label
       login_label = Label(frame2, text="login",font=("Trajan Pro",20,"bold"))
       login_label.pack()
       login_label.place(x=480,y=30)

       #username label
       username_label = Label(frame2, text="Username * ")
       username_label.pack()
       username_label.place(x=480,y=70)
       username_entry = Entry(frame2,textvariable=username)
       username_entry.pack()
       username_entry.place(x=480,y=110)
       #password label
       password_label = Label(frame2, text="password * ")
       password_label.pack()
       password_label.place(x=480,y=150)
       password_entry = Entry(frame2,show="*",textvariable=password)
       password_entry.pack()
       password_entry.place(x=480,y=180)
       #login button
       button3 = Button(frame2,bg="#FF5733",text="login ",command=self.login_user,font=("Trajan Pro",10,"bold"))
       button3.pack()
       button3.place(x=480,y=230,height=40,width=130)
       #button homme
       button4 = Button(frame2,bg="#FF5733",text="home ",command=self.firstpage,font=("Trajan Pro",10,"bold"))
       button4.pack()
       button4.place(x=480,y=350,height=40,width=130)
       

       
       myFrame.destroy()

    



    def login_user(self):
         username_lg = username.get()
         password_lg = password.get()


         mydb = self.connect_to_database()
         mycursor = mydb.cursor()


         sql = "SELECT * FROM userinfo WHERE username = %s AND password = %s"
         values = (username_lg, password_lg)
         mycursor.execute(sql, values)

        # Fetch all the rows from the result set
         rows = mycursor.fetchall()

            # Check if any rows are returned
         if rows:
                Label(frame2, text="user exist", fg="green", font=("calibri", 11)).place(x=100,y=260)
                os.system('python userinterface.py')
                root.destroy()
                
         else:
                Label(frame2, text="user doesn't exist ", fg="red", font=("calibri", 11)).place(x=100,y=260)


    def login_admin(self):
       #variables
       global username_adm
       global password_adm
       global frame3
       frame3=Frame(bg="#369E98")
       frame3.pack()
       frame3.place(x=50,y=50,width=700,height=500)
   
       username_adm = StringVar()
       password_adm = StringVar()

      #text(left frame)
       left_frame=Frame(frame3,bg="#C4E3E1")
       left_frame.pack()
       left_frame.place(x=0,y=0,width=400,height=500)
       titre = Label(left_frame, text="application gestion de stock",font=("Trajan Pro",18,"bold"),bg="#C4E3E1",fg="#708685")  
       titre.pack()
       titre.place(x=25,y=50)
       text_label=Label(left_frame,text="Lorsque vous remplissez une page de connexion avec des champs de nom d'utilisateur et de mot de passe, il est important de prendre certaines mesures pour protéger votre compte. ",font=("Trajan Pro",10,"bold"),bg="#C4E3E1",fg="#485E5D",wraplength=300, padx=10)
       text_label.pack()
       text_label.place(x=40,y=130)



       #login label
       login_label = Label(frame3, text="login as admin",font=("Trajan Pro",20,"bold"))
       login_label.pack()
       login_label.place(x=480,y=30)

       #username label
       username_label = Label(frame3, text="Username * ")
       username_label.pack()
       username_label.place(x=480,y=70)
       username_entry = Entry(frame3,textvariable=username_adm)
       username_entry.pack()
       username_entry.place(x=480,y=110)
       #password label
       password_label = Label(frame3, text="password * ")
       password_label.pack()
       password_label.place(x=480,y=150)
       password_entry = Entry(frame3,show="*",textvariable=password_adm)
       password_entry.pack()
       password_entry.place(x=480,y=180)
       #login button
       button3 = Button(frame3,bg="#FF5733",text="login ",command=self.login_as_admin,font=("Trajan Pro",10,"bold"))
       button3.pack()
       button3.place(x=480,y=230,height=40,width=130)
       #button homme
       button4 = Button(frame3,bg="#FF5733",text="home ",command=self.firstpage,font=("Trajan Pro",10,"bold"))
       button4.pack()
       button4.place(x=480,y=350,height=40,width=130)
     

       
      
       

       
       myFrame.destroy()



    def login_as_admin(self):
         username_lg_adm = username_adm.get()
         password_lg_adm = password_adm.get()


         mydb = self.connect_to_database()
         mycursor = mydb.cursor()


         sql = "SELECT * FROM admin WHERE username = %s AND password = %s"
         values = (username_lg_adm, password_lg_adm)
         mycursor.execute(sql, values)

        # Fetch all the rows from the result set
         rows = mycursor.fetchall()

            # Check if any rows are returned
         if rows:
                Label(frame3, text="admin exist", fg="green", font=("calibri", 11)).place(x=100,y=260)
                os.system('python admininterface.py')
                root.destroy()
                
                
                
         else:
                Label(frame3, text="admin doesn't exist ", fg="red", font=("calibri", 11)).place(x=100,y=260)


    





        
    
       
    



    




e=m(root)




root.mainloop()

        