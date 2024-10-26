import time
import customtkinter

from library import ou_status, csu_status, cu_status, tt_status, tr_status, du_status, mi_status


def login():
    user = user_var.get()
    password = pass_var.get()

    print(user, password)
    if user == "user" and password == "password":
        time.sleep(0.5)
        login_page.destroy()
        main_gui_open()  # Open the main GUI only on successful login
    else:
        try_again = customtkinter.CTkLabel(master=frame, text="Incorrect Username or Password", text_color="red")
        try_again.pack(padx=5, pady=5)

# Main GUI function
def main_gui_open():
    main_gui = customtkinter.CTkToplevel()
    main_gui.geometry("1000x700")
    mainframe = customtkinter.CTkFrame(master=main_gui)
    mainframe.pack(pady=20, padx=60, fill="both", expand=True)
    status_frame = customtkinter.CTkFrame(master=mainframe, width=225, height=250)
    status_frame.pack(pady=50, padx=60, fill="both", expand=True)
    status_frame.place(relx = 0.15, rely = 0.22, anchor = "center")
    status = customtkinter.CTkLabel(master=status_frame, text=f"OU Status: {ou_status}\n\n"
                                                           f"CSU Status: {csu_status}\n\n"
                                                           f"CU Status: {cu_status}\n\n"
                                                           f"Texas Tech Status: {tt_status}\n\n"
                                                           f"Trinity Status: {tr_status}\n\n"
                                                           f"DU Status: {du_status}\n\n"
                                                           f"Mines Status: {mi_status}\n\n"
                                                           , text_color="white")
    status.place(relx=0.50, rely=0.52, anchor="center")



customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

# Initialize the login page
login_page = customtkinter.CTk()
login_page.geometry("500x400")

# Variables for username and password
user_var = customtkinter.StringVar()
pass_var = customtkinter.StringVar()



# Create the login frame
frame = customtkinter.CTkFrame(master=login_page)
frame.pack(pady=20, padx=60, fill="both", expand=True)

label = customtkinter.CTkLabel(master=frame, text="Login System")
label.pack(pady=12, padx=10)

# Username Entry
user_label = customtkinter.CTkLabel(master=frame, text="Username")
user_label.pack(pady=2, padx=10)
entry = customtkinter.CTkEntry(master=frame, textvariable=user_var, placeholder_text="Username")
entry.pack(pady=12, padx=10)

# Password Entry
pass_label = customtkinter.CTkLabel(master=frame, text="Password")
pass_label.pack(pady=2, padx=10)
entryp = customtkinter.CTkEntry(master=frame, placeholder_text="Password", show="*", textvariable=pass_var)
entryp.pack(pady=12, padx=10)

# Login Button
button = customtkinter.CTkButton(master=frame, text="Login", command=login)
button.pack(pady=12, padx=10)

login_page.mainloop()
