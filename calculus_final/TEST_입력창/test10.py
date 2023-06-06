import tkinter as tk
from tkinter import messagebox

# 전역 변수로 변수 a, b, c, d 선언
a = ""
b = ""
c = ""
d = ""

def submit():
    global a, b, c, d  # 전역 변수를 사용하기 위해 선언
    
    # 사용자가 선택한 함수 종류 가져오기
    selected_function = function_var.get()
    
    # 선택된 함수에 따라 변수 입력 받기
    if selected_function == "Function 1":
        a = entry_a.get()
        b = entry_b.get()
        # 여기서 함수 1 실행
        messagebox.showinfo("결과", f"Function 1 실행 결과: a={a}, b={b}")
    elif selected_function == "Function 2":
        c = entry_c.get()
        d = entry_d.get()
        # 여기서 함수 2 실행
        messagebox.showinfo("결과", f"Function 2 실행 결과: c={c}, d={d}")
    else:
        # 선택된 함수가 없을 경우 경고 메시지 표시
        messagebox.showwarning("경고", "함수를 선택해주세요!")

def other_function():
    global a, b, c, d  # 전역 변수를 사용하기 위해 선언
    
    # 전역 변수 a, b, c, d를 사용하는 다른 함수
    # 예시로 a와 b를 더한 값을 출력해보겠습니다.
    result = int(a) + int(b)
    print(f"a + b = {result}")

# Tkinter 윈도우 생성
window = tk.Tk()
window.title("함수 선택 및 변수 입력")
window.geometry("300x200")

# 함수 선택을 위한 라디오 버튼 생성
function_var = tk.StringVar()

radio_button1 = tk.Radiobutton(window, text="Function 1", variable=function_var, value="Function 1")
radio_button1.pack()

radio_button2 = tk.Radiobutton(window, text="Function 2", variable=function_var, value="Function 2")
radio_button2.pack()

# 변수 입력을 위한 Entry 위젯 생성
entry_a = tk.Entry(window)
entry_a.pack()

entry_b = tk.Entry(window)
entry_b.pack()

entry_c = tk.Entry(window)
entry_c.pack()

entry_d = tk.Entry(window)
entry_d.pack()

# Submit 버튼 생성
submit_button = tk.Button(window, text="Submit", command=submit)
submit_button.pack()

# Tkinter 이벤트 루프 시작
window.mainloop()


