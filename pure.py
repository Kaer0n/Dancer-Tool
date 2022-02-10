from util.massban import *
import logging
import time
from tkinter import *

logging.basicConfig(level=logging.INFO)

def btn_clicked():
    bot_token = entry0.get()
    user_token = entry1.get()
    guild_id = entry2.get()
    channel_id = entry3.get()
    time.sleep(0.2)
    window.destroy()
    ob1 = banclass(user_token, guild_id, channel_id) # instantiates class
    ob1.scrapeusers() # scrapes users
    ob1.ban_all(guild_id, bot_token) # executes ban method

window = Tk()
window.title('Dancer - Weapon of Mass Destruction')
window.geometry("600x200")
window.configure(bg = "#2b2b2b")
canvas = Canvas(
    window,
    bg = "#2b2b2b",
    height = 200,
    width = 600,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = PhotoImage(file = f"./package/img0.png")
background = canvas.create_image(
    300.0, 100.0,
    image=background_img)

img0 = PhotoImage(file = f"./package/img1.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b0.place(
    x = 225, y = 151,
    width = 150,
    height = 27)

entry0_img = PhotoImage(file = f"./package/img2.png")
entry0_bg = canvas.create_image(
    157.0, 51.5,
    image = entry0_img)

entry0 = Entry(
    bd = 0,
    fg = '#D9D9D9',
    bg = "#151515",
    highlightthickness = 0)

entry0.place(
    x = 51.5, y = 40,
    width = 211.0,
    height = 21)

entry1_img = PhotoImage(file = f"./package/img3.png")
entry1_bg = canvas.create_image(
    157.0, 121.5,
    image = entry1_img)

entry1 = Entry(
    bd = 0,
    fg = '#D9D9D9',
    bg = "#151515",
    highlightthickness = 0)

entry1.place(
    x = 51.5, y = 110,
    width = 211.0,
    height = 21)

entry2_img = PhotoImage(file = f"./package/img4.png")
entry2_bg = canvas.create_image(
    437.0, 51.5,
    image = entry2_img)

entry2 = Entry(
    bd = 0,
    fg = '#D9D9D9',
    bg = "#151515",
    highlightthickness = 0)

entry2.place(
    x = 331.5, y = 40,
    width = 211.0,
    height = 21)

entry3_img = PhotoImage(file = f"./package/img5.png")
entry3_bg = canvas.create_image(
    437.0, 121.5,
    image = entry3_img)

entry3 = Entry(
    bd = 0,
    fg = '#D9D9D9',
    bg = "#151515",
    highlightthickness = 0)

entry3.place(
    x = 331.5, y = 110,
    width = 211.0,
    height = 21)

window.resizable(False, False)
window.mainloop()


