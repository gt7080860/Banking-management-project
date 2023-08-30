# imports 
from stat import filemode
from tkinter import *
import os
from PIL import ImageTk,Image
# main Screen
master =Tk() 
master.title('Banking APP')
#Functions
def finish_reg():
   name=temp_name.get()
   age=temp_age.get()
   gender=temp_gender.get()
   Password=temp_Password.get()
   all_acounts=os.listdir()
   #print(all_acounts)
   if name =="" or age==""or gender==""or Password=="":
        notif.config(fg="red",text="All field required")
        return
   for name_check in all_acounts:
        if name==name_check:
            notif.config(fg="red",text="Acounts already exists")
            return
        else:
            new_file=open(name,"w")
            new_file.write(name+'\n')
            new_file.write(Password+'\n')
            new_file.write(age+'\n')
            new_file.write(gender+'\n')
            new_file.write('0')
            new_file.close()
            notif.config(fg="green",text="Acounts has been Sucessfully created")

def register():
    # Vars
    global temp_name
    global temp_age
    global temp_gender
    global temp_Password
    global notif
    temp_name=StringVar()
    temp_age=StringVar()
    temp_gender=StringVar()
    temp_Password=StringVar()

    #Register Screen
    register_screen=Toplevel(master)
    register_screen.title("Register")
    #Labels
    Label(register_screen,text="please enter your details below to register",font=("Calibary",14)).grid(row=0,sticky=N,pady=10)
    Label(register_screen,text="Name",font=("Calibary",12)).grid(row=1,sticky=W)
    Label(register_screen,text="Age",font=("Calibary",12)).grid(row=2,sticky=W)
    Label(register_screen,text="Gender",font=("Calibary",12)).grid(row=3,sticky=W)
    Label(register_screen,text="Password",font=("Calibary",12)).grid(row=4,sticky=W)
    notif=Label(register_screen,font=("Calibary",12))
    notif.grid(row=6,sticky=N,pady=10)
    #Entries
    Entry(register_screen,textvariable=temp_name).grid(row=1,column=0)
    Entry(register_screen,textvariable=temp_age).grid(row=2,column=0)
    Entry(register_screen,textvariable=temp_gender).grid(row=3,column=0)
    Entry(register_screen,textvariable=temp_Password).grid(row=4,column=0)
    # Buttons
    Button(register_screen,text="Register",command=finish_reg,font=("calibri",12 )).grid(row=5,sticky=N,pady=10)

def login_session():
    global login_name
    all_accounts=os.listdir()
    login_name=temp_login_name.get()
    login_password=temp_login_password.get()
    for name in all_accounts:
        if name ==login_name:
            file=open(name,"r")
            file_data=file.read()
            file_data=file_data.split("\n")
            password=file_data[1]
            #Accounts Dashboard
            if login_password == password:
                Login_screen.destroy()
                account_dashboard=Toplevel(master)
                account_dashboard.title("Dashboard")
                #Label
                Label (account_dashboard,text="Account Dashboard",font=("Calibri",12)).grid(row=0,sticky=N,pady=10)
                Label (account_dashboard,text="Welcome"+" "+name,font=("Calibri",12)).grid(row=1,sticky=N,pady=5)
                #buttons
                Button(account_dashboard,text="personal details",font=("Calibri",12),width=30,command=personal_details).grid(row=2,sticky=N,padx=10)
                Button(account_dashboard,text=" Deposit",font=("Calibri",12),width=30,command=deposit).grid(row=3,sticky=N,padx=10)
                Button(account_dashboard,text="Withdraw",font=("Calibri",12),width=30,command=withdraw).grid(row=4,sticky=N,padx=10)
                Label(account_dashboard).grid(row=5,sticky=N,pady=10)
                return
            else :
                login_notif.config(fg="red",text="Password Incorrect!!")
                return
        login_notif.config(fg="red",text="No such account found")

def deposit():
    #var
    global amount
    global deposit_notif
    global current_balance_label
    amount=StringVar()
    file=open(login_name,"r")
    file_data=file.read()
    user_details=file_data.split('\n')#it will user details into an array which will atore all the details at the index location 
    details_balance=user_details[4]# at 4 th index we will have balance
    #deposit screen
    deposit_screen=Toplevel(master)
    deposit_screen.title("Deposit")
    #Label
    Label(deposit_screen,text="Deposit",font=('Calibri',12)).grid(row=0,sticky=N,pady=10)
    current_balance_label=Label(deposit_screen,text="Current Balance:$"+details_balance,font=('Calibri',12))
    current_balance_label.grid(row=1,sticky=W)
    Label(deposit_screen,text="Amount: ",font=('Calibri',12)).grid(row=2,sticky=W)
    deposit_notif=Label(deposit_screen,font=('Calibri',12))
    deposit_notif.grid(row=4,sticky=N,pady=5)
    #Entry
    Entry(deposit_screen,textvariable=amount).grid(row=2,column=1)
    #Buttons
    Button(deposit_screen,text="Finish",font=('Calibri',12),command=finish_deposit).grid(row=3,sticky=W,pady=5)
def finish_deposit():
    if amount.get()=="":
        deposit_notif.config(text="Amount is required",fg="red")
    if float(amount.get())<=0:
        deposit_notif.config(text="Negative currency is not accepted",fg='red')
        return
    
    file=open (login_name,'r+')
    file_data=file.read()
    details=file_data.split('\n')
    current_balance=details[4]
    updated_balance=current_balance
    updated_balance=float (updated_balance)+float(amount.get())
    file_data    =file_data.replace(current_balance,str(updated_balance))
    file.seek(0)
    file.truncate(0)
    file.write(file_data)
    file.close()
    current_balance_label.config(text="Current Balance: $" + str(updated_balance),fg="green")
    deposit_notif.config(text='balance Updated',fg='green')

def withdraw():
    global withdraw_amount
    global withdraw_notif
    global current_balance_label
    withdraw_amount=StringVar()
    file=open(login_name,"r")
    file_data=file.read()
    user_details=file_data.split('\n')#it will user details into an array which will atore all the details at the index location 
    details_balance=user_details[4]# at 4 th index we will have balance
    #deposit screen
    withdraw_screen=Toplevel(master)
    withdraw_screen.title("Withdraw")
    #Label
    Label(withdraw_screen,text="Withdraw",font=('Calibri',12)).grid(row=0,sticky=N,pady=10)
    current_balance_label=Label(withdraw_screen,text="Current Balance:$"+details_balance,font=('Calibri',12))
    current_balance_label.grid(row=1,sticky=W)
    Label(withdraw_screen,text="Amount: ",font=('Calibri',12)).grid(row=2,sticky=W)
    withdraw_notif=Label(withdraw_screen,font=('Calibri',12))
    withdraw_notif.grid(row=4,sticky=N,pady=5)
    #Entry
    Entry(withdraw_screen,textvariable=withdraw_amount).grid(row=2,column=1)
    #Buttons
    Button(withdraw_screen,text="Finish",font=('Calibri',12),command=finish_withdraw).grid(row=3,sticky=W,pady=5)

def finish_withdraw():
    if withdraw_amount.get()=="":
        withdraw_notif.config(text="Amount is required",fg="red")
    if float(withdraw_amount.get())<=0:
        withdraw_notif.config(text="Negative currency is not accepted",fg='red')
        return
    file=open (login_name,'r+')
    file_data=file.read()
    details=file_data.split('\n')
    current_balance=details[4]

    if float(withdraw_amount.get())> float(current_balance):
        withdraw_notif.config(text='Insufficient Funds !!',fg='red')
        return
    updated_balance =current_balance
    updated_balance =float (updated_balance) - float(withdraw_amount.get())
    file_data       =file_data.replace(current_balance,str(updated_balance))
    file.seek(0)
    file.truncate(0)
    file.write(file_data)
    file.close()
    current_balance_label.config(text="Current Balance: $" + str(updated_balance),fg="green")
    withdraw_notif.config(text='balance Updated',fg='green')

def personal_details():
    #vars
    file=open(login_name ,'r')
    file_data=file.read()
    user_details=file_data.split('\n')
    details_name=user_details[0]
    details_age=user_details[2]
    details_gender=user_details[3]
    details_balance=user_details[4]
        # Personal details screen
    personal_details_screen=Toplevel(master)
    personal_details_screen.title('personal Details')
        #Labels
    Label(personal_details_screen,text="Personal Details",font=('Calibri',12)).grid(row=0,sticky=N,pady=10)
    Label(personal_details_screen,text="Name : " +details_name,font=('Calibri',12)).grid(row=1,sticky=W)
    Label(personal_details_screen,text="Age : " + details_age,font=('Calibri',12)).grid(row=2,sticky=W)
    Label(personal_details_screen,text="Gender : " + details_gender,font=('Calibri',12)).grid(row=3,sticky=W)
    Label(personal_details_screen,text="Balance : " + details_balance,font=('Calibri',12)).grid(row=4,sticky=W)

def login():
    #variable
  global temp_login_name
  global temp_login_password
  global login_notif
  global Login_screen
  temp_login_name=StringVar()
  temp_login_password=StringVar()
#Login master 
  Login_screen=Toplevel(master)
  Login_screen.title("Login")
  #Labels
  Label(Login_screen,text="Login to your acounts",font=("Calibri",12)).grid(row=0,sticky=N,pady=10)
  Label(Login_screen,text="Username",font=("Calibri",12)).grid(row=1,sticky=W)
  Label(Login_screen,text="Password",font=("Calibri",12)).grid(row=2,sticky=W)
  login_notif=Label(Login_screen,font=("calibri",12))
  login_notif.grid(row=4,sticky=N)
  #Entry
  Entry(Login_screen,textvariable=temp_login_name).grid(row=1,column=1,padx=5)
  Entry(Login_screen,textvariable=temp_login_password,show="#").grid(row=2,column=1,padx=5)
  #Buttons
  Button(Login_screen,text="Login",command=login_session,width=15,font=('Calibri',12)).grid(row=3,sticky=N,pady=5,padx=5)

# import image
img= Image.open("banksystem2.png") 
img=img.resize((150,150))
img=ImageTk.PhotoImage(img)
#Label
Label(master ,text="Custom Banking ",font=("Calibary",14)).grid(row=0,sticky=N,pady=10)
Label(master ,text="Most secure bank youhave probably used",font=("Calibary",12)).grid(row=1,sticky=N)
Label(master ,image=img).grid(row=2,sticky=N,pady=15)
#Buttons
Button (master,text="Register",font=("Calibari",12),width=20,command=register).grid(row=3,sticky=N) 
Button (master,text="Login",font=("Calibari",12),width=20,command=login).grid(row=4,sticky=N,pady=10) 


master.mainloop()