from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk  # pip3 install Pillow

root = Tk()
root.title("AI Project completed by Ng Tsz Yin (20307097)")
root.geometry("600x600")

images = {
    "Dragonfly": "./Images/dragonfly.jpg",
    "Flower": "./Images/flower.jpg",
    "Green Chip": "./Images/Green Chip.jpg",
    "Swan": "./Images/swan.jpg"
}

loaded_images = {}

for name, path in images.items():
    img = Image.open(path)
    loaded_images[name] = ImageTk.PhotoImage(img)

option = StringVar()
option.set("Select an image")

def show_image(selected):
    image_label.config(image=loaded_images[selected])
    image_label.image = loaded_images[selected] 

dropdown = OptionMenu(root, option, *images.keys(), command=show_image)
exit_btn = Button(root, width=15, text="Exit Program", command=root.quit)
selected_value = Label(root, text=" ")
image_label = Label(root)

exit_btn.grid(row=0, column=1)
dropdown.grid(row=1, column=1)
selected_value.grid(row=2, column=1)
image_label.grid(row=3, column=1)

root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)

root.mainloop()