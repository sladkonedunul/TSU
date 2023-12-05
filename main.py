import tkinter as tk

root = tk.Tk()
def button_click():
  input_text = entry.get()
  print(f"Полученный текст: {input_text}")

entry = tk.Entry(root)
button = tk.Button(root, text="Отправить", command=button_click)

entry.pack()
button.pack()

root.mainloop()
