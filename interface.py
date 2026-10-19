#Making a user interface
import tkinter as tk
from authentication import user, password

#Making the main window
root = tk.Tk()
root.title("Login Interface")
 #Sets the size of the window
root.geometry("1024x768")
#Sets color of the background
root.configure(bg = "lightblue")

#Making title
title_label = tk.Label(root, text = "Login Interface", font = ("Arial", 24), bg = "lightblue")
title_label.pack(pady=20)

#Making status label
status_label = tk.Label(root, text = "Please enter your username and password", font = ("Arial", 14), bg = "lightblue")
status_label.pack(pady=10)

root.mainloop()
