import tkinter as tk
import time
import threading
from tkinter import messagebox

class Writer():
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("700x500")

        self.textbox = tk.Text(self.root)
        # self.text = "De tetten van sanne"
        # self.textbox.insert(tk.END, self.text)
        # self.textbox.config(foreground='blue')
        self.textbox.bind('<KeyRelease>', self.keypress_in_textbox)
        self.textbox.pack(pady=20, padx=20)
        self.start_time = time.time()
        self.end_time = time.time()

        self.btn_exit = tk.Button(self.root, text="exit", command=self.close)
        self.btn_exit.pack(side='right', padx=20)

        self.btn_save_file = tk.Button(self.root, text="save file", command=self.save_file)
        self.btn_save_file.pack(side='right', padx=20)

        self.textbox.focus()
        self.safe_time = 3
        self.timer_running = False
        # self.start_timer()
        self.root.mainloop()



    def turn_text_invisible(self):
        contents = self.textbox.get("1.0", tk.END)
        print(contents)
        self.textbox.delete("1.0", tk.END)
        # self.textbox.config(foreground='#D6D6D6')

    def close(self):
        self.root.destroy()

    def save_file(self):
        time.sleep(1)
        messagebox.showinfo(title="save file", message="there is no text to save!")

    def keypress_in_textbox(self, event):
        print(f"in keypress {event.keysym}")
        print(f"in keypress ")
        if self.timer_running:
            print(f"timer already running")
        else:
            self.start_timer()

    def start_timer(self):
            timer_thread = threading.Thread(target=self.timer)
            timer_thread.daemon = True
            timer_thread.start()
            # self.start_timer()

    def timer(self):
        print(f"timer started--------------------")
        self.start_time = time.time()
        self.timer_running = True
        while self.end_time < self.start_time + self.safe_time:
            # print(f"run timer: {int(self.end_time)} - {int(self.start_time)} = {int(self.end_time - self.start_time)}")
            self.end_time = time.time()
        self.turn_text_invisible()
        self.timer_running = False


Writer()