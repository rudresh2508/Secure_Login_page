import customtkinter
import sqlite3
from tkinter import *
from tkinter import messagebox

app = customtkinter.CTk() 
app.title("Login")
app.geometry("450x360")
app.config(bg="#001220")

font1 = ("Helvetica", 25, "bold")
font2 = ("Arial", 17, "bold")
font3 = ("Arial", 13, "bold")
font4 = ("Arial", 13, "bold", "underline")

conn = sqlite3.connect("data.db")
cursor = conn.cursor()

cursor.execute('''
      CREATE TABLE IF NOT EXISTS users (
               username TEXT NOT NULL,
               password TEXT NOT NULL)''' )

# Define username_entry in the global scope
username_entry = None

def signup():
    username = username_entry.get()
    password = Password_entry.get()
    if username != '' and password != '':
        cursor.execute("SELECT username FROM users WHERE username = ?", [username])
        if cursor.fetchone() is not None:
            messagebox.showerror("Error", "Username already exists.")
        else:
            cursor.execute('INSERT INTO users VALUES (?, ?)', [username, password])
            conn.commit()
            messagebox.showinfo('Success', 'Account has been created.')
    else:
        messagebox.showerror('Error', 'Enter all data.')

def login_account():
    username = username_entry2.get()
    password = password_entry2.get()
    if username != '' and password != '':
        cursor.execute('SELECT password FROM users WHERE username = ?', [username])
        result = cursor.fetchone()
        if result:
            if password == result[0]:
                messagebox.showinfo('Success','Logged in successfully.')
            else:
                messagebox.showerror('Error','Invalid password.')
        else:
            messagebox.showerror('Error','Invalid username.')
    else:
        messagebox.showerror('Error','Enter all data.')

def reset_password():
    global username_entry  # Access the global username_entry
    
    # Get the username entered by the user
    username = username_entry.get()
    
    # Check if the username exists in the database
    cursor.execute("SELECT * FROM users WHERE username = ?", [username])
    user = cursor.fetchone()
    
    if user:
        # Display a messagebox with a password reset confirmation
        messagebox.showinfo('Reset Password', f'A password reset link has been sent to {username}\'s email.')
    else:
        # If the username doesn't exist, display an error message
        messagebox.showerror('Error', 'Invalid username.')

def logout():
    # Clear the user's session data
    username_entry2.delete(0, END)  # Clear the username entry field
    password_entry2.delete(0, END)  # Clear the password entry field
    
    # Redirect the user to the login page
    frame2.destroy()  # Destroy the current frame (logged-in page)
    show_login_frame()  # Show the login frame again

def show_login_frame():
    global frame1
    frame1 = customtkinter.CTkFrame(app,bg_color="#001220",fg_color="#001220",width=470,height=360)
    frame1.place(x=0,y=0)

    image1 = PhotoImage(file = "image2.png")
    image1_label = Label(frame1, image=image1,bg="#001220")
    image1_label.place(x=0,y=0)

    signup_label = customtkinter.CTkLabel(frame1,font=font1,text="Sign up",text_color = "#fff",bg_color="#001220")
    signup_label.place(x=280,y=20)

    global username_entry
    global Password_entry

    username_entry = customtkinter.CTkEntry(frame1,font=font2,text_color = "#fff",fg_color="#001a2e",bg_color="#121111",border_color ="#004780", border_width=3,placeholder_text="Username",placeholder_text_color="#a3a3a3",width = 200,height=50)
    username_entry.place(x=230,y=80)

    Password_entry = customtkinter.CTkEntry(frame1,font=font2,show = "*",text_color = "#fff",fg_color="#001a2e",bg_color="#121111",border_color ="#004780", border_width=3,placeholder_text="Password",placeholder_text_color="#a3a3a3",width = 200,height=50)
    Password_entry.place(x=230,y=150)

    signup_button = customtkinter.CTkButton(frame1,command = signup, font=font2,text_color = "#fff", text="sign up",fg_color="#00965d",hover_color = "#006e44",bg_color="#121111",cursor = "hand2",corner_radius = 5, width = 120) 
    signup_button.place(x=230,y=220)

    login_label = customtkinter.CTkLabel(frame1,font=font3,text = "Already have an account?", text_color="#fff",bg_color="#001220")           
    login_label.place(x=230,y=250)

    login_button = customtkinter.CTkButton(frame1,command = login, font=font4,text_color="#00bf77",text="Login",fg_color="#001220",hover_color="#001220",cursor="hand2",width=40)
    login_button.place(x=395,y=250)

def login():
    global frame2
    frame1.destroy()
    frame2 = customtkinter.CTkFrame(app,bg_color="#001220",fg_color="#001220",width = 470,height=360)
    frame2.place(x=0,y=0)

    image1 = PhotoImage(file='')
    image1_label = Label(frame2,image=image1,bg="#001220")
    image1_label.place(x=0,y=0)
    frame2.image1 = image1 

    login_label2 = customtkinter.CTkLabel(frame2,font=font1,text = 'Log in',text_color = '#fff',bg_color='#001220')
    login_label2.place(x=280,y=20)

    global username_entry2
    global password_entry2

    username_entry2 = customtkinter.CTkEntry(frame2,font=font2,text_color="#fff",fg_color="#001a2e",bg_color="#121111",border_color="#004780",border_width=3,placeholder_text="Username",placeholder_text_color="#a3a3a3",width=200,height = 50)
    username_entry2.place(x=230,y=80)

    password_entry2 = customtkinter.CTkEntry(frame2,font=font2, show = '*',text_color="#fff",fg_color="#001a2e",bg_color="#121111",border_color="#004780",border_width=3,placeholder_text="Password",placeholder_text_color="#a3a3a3",width=200,height = 50)
    password_entry2.place(x=230,y=150)

    login_button2 = customtkinter.CTkButton(frame2,command = login_account,font=font2,text_color="#fff",text="Log in",fg_color="#00965d",hover_color="#006e44",bg_color = "#121111",cursor="hand2",corner_radius=5,width=120)
    login_button2.place(x=230,y=220)

    # Add a "Forgot Password?" button linked to the reset_password function.
    forgot_password_button = customtkinter.CTkButton(frame2, command=reset_password, text="Forgot Password?", font=font3, text_color="#fff", bg_color="#001220", border_width=0)
    forgot_password_button.place(x=230, y=280)

    # Add a "Logout" button linked to the logout function.
    logout_button = customtkinter.CTkButton(frame2, command=logout, text="Logout", font=font3, text_color="#fff", bg_color="#001220", border_width=0)
    logout_button.place(x=340, y=280)

show_login_frame()

app.mainloop()
