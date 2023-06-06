import tkinter as tk
from tkinter import messagebox

def open_input_window():
    selected_value = radio_var.get()

    if selected_value == 1:
        option = "옵션 1"
    elif selected_value == 2:
        option = "옵션 2"
    elif selected_value == 3:
        option = "옵션 3"
    else:
        messagebox.showerror("오류", "라디오 버튼을 선택해주세요.")
        return

    input_window = tk.Toplevel(window)
    input_window.title(option)
    
    input_label = tk.Label(input_window, text="값을 입력하세요:")
    input_label.pack()

    input_entry = tk.Entry(input_window)
    input_entry.pack()

    submit_button = tk.Button(input_window, text="확인", command=lambda: submit_input(option, input_entry.get()))
    submit_button.pack()

def submit_input(option, value):
    messagebox.showinfo("결과", f"{option} 선택 - 입력값: {value}")


# Tkinter 창 생성
window = tk.Tk()

# 라디오 버튼 변수
radio_var = tk.IntVar()

# 라디오 버튼 생성
radio_button1 = tk.Radiobutton(window, text="옵션 1", variable=radio_var, value=1)
radio_button1.pack()

radio_button2 = tk.Radiobutton(window, text="옵션 2", variable=radio_var, value=2)
radio_button2.pack()

radio_button3 = tk.Radiobutton(window, text="옵션 3", variable=radio_var, value=3)
radio_button3.pack()

# 다음 버튼 생성
next_button = tk.Button(window, text="다음", command=open_input_window)
next_button.pack()

# Tkinter 창 실행
window.mainloop()


