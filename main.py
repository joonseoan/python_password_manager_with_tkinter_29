# https://tkdocs.com/tutorial/canvas.html
import tkinter as ti

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
# 1) Window
window = ti.Tk()
window.title("Password Manager")
# 200 * 190
window.config(padx=20, pady=20, bg="white")

# 2) Canvas and Image (Photo)
canvas = ti.Canvas(width=200, height=200, bg="white", highlightthickness=0)
lock_mage = ti.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_mage)
# should be changed
canvas.grid()


window.mainloop()
