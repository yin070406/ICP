from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import random

root = Tk()
root.title("AI Project completed by Ng Tsz Yin (20307097)")
root.geometry("600x600")

images = {
    "Dragonfly": "./Images/dragonfly.jpg",
    "Flower": "./Images/flower.jpg",
    "Green Chip": "./Images/Green Chip.jpg",
    "Swan": "./Images/swan.jpg"
}

loaded_images = []

for name, path in images.items():
    img = Image.open(path)
    img = img.resize((300, 300))
    photo = ImageTk.PhotoImage(img)
    loaded_images.append(photo)

image_labels = []
for i, photo in enumerate(loaded_images):
    label = Label(root, image=photo)
    row = (1 + i // 2) + 1  
    col = (i % 2) + 1   
    label.grid(row=row, column=col)
    image_labels.append(label)

def shuffle():
    random.shuffle(loaded_images)
    for i, photo in enumerate(loaded_images):
        image_labels[i].configure(image=photo)
        image_labels[i].image = photo

exit_btn = Button(root, width=15, text="Exit Program", command=root.quit)
shuffle_btn = Button(root, width=15, text="Shuffle", command=shuffle)

exit_btn.grid(row=0, column=1)
shuffle_btn.grid(row=0, column=2)

root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)
root.grid_columnconfigure(3, weight=1)

root.mainloop()