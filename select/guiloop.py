import tkinter
import tkinter.scrolledtext


def gui_loop():
    win = tkinter.Tk()
    win.configure(bg="lightgray")


    chat_label = tkinter.Label(win, text="Chat:", bg="lightgray")
    chat_label.config(font=("Arial", 12))
    chat_label.pack(padx=20, pady=5)

    text_area = tkinter.scrolledtext.ScrolledText(win)
    text_area.pack(padx=20, pady=5)
    text_area.config(state='disabled')

    msg_label = tkinter.Label(win, text="Message:", bg="lightgray")
    msg_label.config(font=("Arial", 12))
    msg_label.pack(padx=20, pady=5)

    input_area = tkinter.Text(win, height=3)
    input_area.pack(padx=20, pady=5)

    send_button = tkinter.Button(win, text = "Send", command="write")
    send_button.config(font=("Arial", 12))
    send_button.pack(padx=20, pady=5)
    win.mainloop()

# def write():
#     message = f"{}: {}"


gui_loop()