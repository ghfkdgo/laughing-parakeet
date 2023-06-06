import tkinter as tk
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from sympy import Rational
from numpy import arange, diff, nan
from tkinter import messagebox
from PIL import Image, ImageTk

# 전역 변수로 변수 a, b, c, d 선언
a = ""
b = ""
c = ""
d = ""
x_tan = ""
x_start = ""
x_last = ""
x_cycle =""

def open_input_window(): #선택된 함수의 종류에 따라 다른 함수 실행
    
    global selected_value
    selected_value = radio_var.get()

    if selected_value == 1:
        # option = "다항함수"
        open_input_window2(selected_value)

    elif selected_value == 2:
        # option = "유리함수"
        open_input_window2(selected_value)

    elif selected_value == 3:
        # option = "무리함수"
        open_input_window2(selected_value)

    elif selected_value == 4:
        # option = "삼각함수"
        open_input_window_trigono1()

    elif selected_value == 5:
        # option = "지수함수"
        open_input_window_expo_log()

    elif selected_value == 6:
        # option = "로그함수"
        open_input_window_expo_log()

    else:
        messagebox.showerror("오류", "라디오 버튼을 선택해주세요.")
        return

def open_input_window2(selected_value) :  #다항, 유리, 무리 함수의 계수, 평행이동 정하기
    global a, b, c, d  # 전역 변수로 선언

    input_window = tk.Toplevel(window)    
    input_window.title("계수와 평행이동")
    input_window.geometry("500x300") 

    input_label = tk.Label(input_window, text="이미지를 참고해 값을 입력하세요:")
    input_label.pack()

    if selected_value == 1:
        # 이미지 1 로드 및 표시
        image_filename = "C:/Users/Min/calculus in py/calculus/image/다항함수.png"
        image = tk.PhotoImage(file=image_filename)
        image_label = tk.Label(input_window, image=image)
        image_label.pack()

    elif selected_value == 2:
        # 이미지 2 로드 및 표시
        image_filename = "C:/Users/Min/calculus in py/calculus/image/유리함수.png"
        image = tk.PhotoImage(file=image_filename)
        image_label = tk.Label(input_window, image=image)
        image_label.pack()

    elif selected_value == 3:
        # 이미지 3 로드 및 표시
        image_filename = "C:/Users/Min/calculus in py/calculus/image/무리함수.png"
        image = tk.PhotoImage(file=image_filename)
        image_label = tk.Label(input_window, image=image)
        image_label.pack()
    else :
        messagebox.showerror("오류")
        return

    label_a = tk.Label(input_window, text= "a")
    label_a.pack()
    entry_a = tk.Entry(input_window)
    entry_a.pack()

    label_b = tk.Label(input_window, text= "b")
    label_b.pack()
    entry_b = tk.Entry(input_window)
    entry_b.pack()

    label_c = tk.Label(input_window, text= "c")
    label_c.pack()
    entry_c = tk.Entry(input_window)
    entry_c.pack()

    label_d = tk.Label(input_window, text= "d")
    label_d.pack()
    entry_d = tk.Entry(input_window)
    entry_d.pack()

    next_button2 = tk.Button(input_window, text="다음", command=lambda: [process_input(entry_a.get(), entry_b.get(), entry_c.get(), entry_d.get()), open_input_window3()] )
    next_button2.pack()

    process_input()

def open_input_window_trigono1(): # 삼각함수 종류 고르기

    input_window = tk.Toplevel(window)    
    input_window.title("종류 고르기")
    input_window.geometry("500x300")

    global trigono # 전역변수로 설정
    trigono = tk.IntVar()

    input_label = tk.Label(input_window, text="함수의 종류를 고르시오")
    input_label.pack()

    # 라디오 버튼 생성
    radio_button1 = tk.Radiobutton(input_window, text="Sin", variable=trigono, value=1)
    radio_button1.pack()

    radio_button2 = tk.Radiobutton(input_window, text="Cos", variable=trigono, value=2)
    radio_button2.pack()

    radio_button3 = tk.Radiobutton(input_window, text="Tan", variable=trigono, value=3)
    radio_button3.pack()

    next_button = tk.Button(input_window, text="다음", command=open_input_window_trigono2)
    next_button.pack()

def open_input_window_trigono2() : # 삼각함수 계수, 평행이동 정하기
    global selected_value2
    selected_value2 = trigono.get()

    input_window3 = tk.Toplevel(window)    
    input_window3.title("계수와 평행이동")
    input_window3.geometry("500x300") 

    input_label = tk.Label(input_window3, text="이미지를 참고해 값을 입력하세요:")
    input_label.pack()

    if selected_value2 == 1:
        # 이미지 1 로드 및 표시
        image_filename = "C:/Users/Min/calculus in py/calculus/image/삼각함수_sin.png"
        image = tk.PhotoImage(file=image_filename)
        image_label = tk.Label(input_window3, image=image)
        image_label.pack()

    elif selected_value2 == 2:
        # 이미지 2 로드 및 표시
        image_filename = "C:/Users/Min/calculus in py/calculus/image/삼각함수_cos.png"
        image = tk.PhotoImage(file=image_filename)
        image_label = tk.Label(input_window3, image=image)
        image_label.pack()

    elif selected_value2 == 3:
        # 이미지 3 로드 및 표시
        image_filename = "C:/Users/Min/calculus in py/calculus/image/삼각함수_tan.png"
        image = tk.PhotoImage(file=image_filename)
        image_label = tk.Label(input_window3, image=image)
        image_label.pack()
    else :
        messagebox.showerror("오류")
        return

    label_a = tk.Label(input_window3, text= "a")
    label_a.pack()
    entry_a = tk.Entry(input_window3)
    entry_a.pack()

    label_b = tk.Label(input_window3, text= "b")
    label_b.pack()
    entry_b = tk.Entry(input_window3)
    entry_b.pack()

    label_c = tk.Label(input_window3, text= "c")
    label_c.pack()
    entry_c = tk.Entry(input_window3)
    entry_c.pack()

    label_d = tk.Label(input_window3, text= "d")
    label_d.pack()
    entry_d = tk.Entry(input_window3)
    entry_d.pack()

    next_button2 = tk.Button(input_window3, text="다음", command=lambda: [process_input(entry_a.get(), entry_b.get(), entry_c.get(), entry_d.get()), open_input_window_trigono3()] )
    next_button2.pack()

    process_input()
    
def open_input_window_expo_log() : # 지수, 로그의 밑 종류 구하기
    input_window = tk.Toplevel(window)    
    input_window.title("종류 고르기")
    input_window.geometry("500x300")

    global base # 전역변수로 설정
    base = tk.IntVar()

    input_label = tk.Label(input_window, text="밑의 종류를 고르시오")
    input_label.pack()

    # 라디오 버튼 생성
    radio_button1 = tk.Radiobutton(input_window, text="e", variable=base, value=1)
    radio_button1.pack()

    radio_button2 = tk.Radiobutton(input_window, text="0<a<1", variable=base, value=2)
    radio_button2.pack()

    radio_button3 = tk.Radiobutton(input_window, text="a>1", variable=base, value=3)
    radio_button3.pack()

    next_button = tk.Button(input_window, text="다음", command=open_input_window_expo_log2)
    next_button.pack()

def open_input_window_expo_log2() : #지수, 로그함수 계수, 평행이동 구하기
    global selected_value3
    selected_value3 = base.get()

    input_window3 = tk.Toplevel(window)    
    input_window3.title("계수와 평행이동")
    input_window3.geometry("500x400") 

    input_label = tk.Label(input_window3, text="이미지를 참고해 값을 입력하세요:")
    input_label.pack()

    if selected_value3 == 1:

        image_filename1 = "C:/Users/Min/calculus in py/calculus/image/지수함수_e.png"
        image_filename2 = "C:/Users/Min/calculus in py/calculus/image/로그함수_e.png"
        
        image1 = tk.PhotoImage(file=image_filename1)
        image2 = tk.PhotoImage(file=image_filename2)

        image_label1 = tk.Label(input_window3, image=image1)
        image_label1.pack()

        image_label2 = tk.Label(input_window3, image=image2)
        image_label2.pack()


    elif selected_value3 == 2 or 3:

        image_filename1 = "C:/Users/Min/calculus in py/calculus/image/지수함수_상수.png"
        image_filename2 = "C:/Users/Min/calculus in py/calculus/image/로그함수_상수.png"
        
        image1 = tk.PhotoImage(file=image_filename1)
        image2 = tk.PhotoImage(file=image_filename2)

        image_label1 = tk.Label(input_window3, image=image1)
        image_label1.pack()

        image_label2 = tk.Label(input_window3, image=image2)
        image_label2.pack()

    else :
        messagebox.showerror("오류")
        return
    
    label_a = tk.Label(input_window3, text= "a \n (밑이 0 < x < 1 인경우 분수꼴(3/4)로 입력하시오) \n( 밑이 x > 1 인경우 분모가 1인 분수꼴로 입력하시오 \n 예 : 2/1 ) \n (밑이 e 인경우 아무 분수를 입력하시오)")
    label_a.pack()
    entry_a = tk.Entry(input_window3)
    entry_a.pack()

    label_b = tk.Label(input_window3, text= "b")
    label_b.pack()
    entry_b = tk.Entry(input_window3)
    entry_b.pack()

    label_c = tk.Label(input_window3, text= "c")
    label_c.pack()
    entry_c = tk.Entry(input_window3)
    entry_c.pack()

    label_d = tk.Label(input_window3, text= "d")
    label_d.pack()
    entry_d = tk.Entry(input_window3)
    entry_d.pack()

    next_button2 = tk.Button(input_window3, text="다음", command=lambda: [process_input_expo_log(entry_a.get(), entry_b.get(), entry_c.get(), entry_d.get()), open_input_window3()] )
    next_button2.pack()

    process_input()


def process_input(a_val, b_val, c_val, d_val): ## a,b,c,d 를 실수형으로 전환 (다항,유리,무리,삼각)
    global a, b, c, d  # 전역 변수로 선언

    try:
        a = float(a_val)
        b = float(b_val)
        c = float(c_val)
        d = float(d_val)

        # 변환된 값을 변수에 저장하여 활용할 수 있음
        # 값이 맞나 출력해봄
        print("a:", a)
        print("b:", b)
        print("c:", c)
        print("d:", d)

    except ValueError:
        messagebox.showerror("오류", "입력값을 확인하세요.")

def process_input_expo_log(a_val, b_val, c_val, d_val): ## a,b,c,d 를 실수형으로 전환 (지수, 로그)
    global a, b, c, d  # 전역 변수로 선언

    try:
        a = str(a_val)
        numerator, denominator = map(int, a.split('/'))
        # 분자와 분모를 사용하여 SymPy의 Rational 클래스로 분수 생성
        fraction = Rational(numerator, denominator)
        # float 형태로 사용하기 위해 값 변환
        a = fraction.evalf()
        b = float(b_val)
        c = float(c_val)
        d = float(d_val)

        # 변환된 값을 변수에 저장하여 활용할 수 있음
        # 여기서는 예시로 출력만 함
        print("a:", a)
        print("b:", b)
        print("c:", c)
        print("d:", d)

    except ValueError:
        messagebox.showerror("오류", "입력값을 확인하세요.")


def open_input_window3() : # 다항, 유리, 무리, 지수, 로그 접선좌표와 범위
    input_window2 = tk.Toplevel(window)
    input_window2.title("접선의 x좌표와 x 값 범위")
    input_window2.geometry("500x300")

    input_label = tk.Label(input_window2, text="접선을 그릴 x좌표, \n x 값의 범위를 입력하시오:")
    input_label.pack()

    label_x_tan = tk.Label(input_window2, text= "접선을 그릴 x좌표")
    label_x_tan.pack()

    entry_x_tan = tk.Entry(input_window2)
    entry_x_tan.pack()

    label_x_start = tk.Label(input_window2, text= "x 값의 범위")
    label_x_start.pack()
    

    entry_x_start = tk.Entry(input_window2)
    entry_x_start.pack()
    

    label_x = tk.Label(input_window2, text= " < x < ")
    label_x.pack()
    

    entry_x_last = tk.Entry(input_window2)
    entry_x_last.pack()

    next_button2 = tk.Button(input_window2, text="다음", command=lambda :[process_input2(entry_x_tan.get(), entry_x_start.get(), entry_x_last.get()), graphing_final() ])
    next_button2.pack()

def open_input_window_trigono3() : #삼각함수 접선좌표와 범위
    input_window2 = tk.Toplevel(window)
    input_window2.title("접선의 x좌표와 x 값 범위")
    input_window2.geometry("500x300")

    input_label = tk.Label(input_window2, text="접선을 그릴 x좌표, \n 표시할 주기 수를 입력하세요:")
    input_label.pack()

    label_x_tan = tk.Label(input_window2, text= "접선을 그릴 x좌표")
    label_x_tan.pack()

    entry_x_tan = tk.Entry(input_window2)
    entry_x_tan.pack()

    label_x_cycle = tk.Label(input_window2, text= "주기 ( 예 : '2' 입력 -> 2주기 )")
    label_x_cycle.pack()
    
    entry_x_cycle = tk.Entry(input_window2)
    entry_x_cycle.pack()

    next_button2 = tk.Button(input_window2, text="다음", command=lambda : [process_input3(entry_x_tan.get(), entry_x_cycle.get()), graphing_final() ])
    next_button2.pack()

def process_input2(x_tan_val, x_start_val, x_last_val): ## x_tan, x_start, x_last를 실수형으로 전환 (다항,유리,무리,지수,로그)
    global x_tan, x_start, x_last  # 전역 변수로 선언

    try:
        x_tan = float(x_tan_val)
        x_start = float(x_start_val)
        x_last = float(x_last_val)

        print("x_tan:", x_tan)
        print("x_start:", x_start)
        print("x_last:", x_last)
    

    except ValueError:
        messagebox.showerror("오류", "입력값을 확인하세요.")

def process_input3(x_tan_val, x_cycle_val): ## x_tan, x_cycle 를 실수형으로 전환 (삼각)
    global x_tan, x_cycle  # 전역 변수로 선언

    try:
        x_tan = float(x_tan_val)
        x_cycle = float(x_cycle_val)

        print("x_tan:", x_tan)
        print("x_cycle:", x_cycle)

    except ValueError:
        messagebox.showerror("오류")

def graphing(f_expr) :
    global a, b, c, d, x_tan, x_start, x_last # 전역 변수로 접근

    x = sp.Symbol('x')
    # 함수식 그래프 그리기
    f = sp.lambdify(x, f_expr, 'numpy') # sympy에서 만든 함수식을 numpy 로 변경해주기
    x_vals = np.linspace(x_start, x_last, 400)
    y_vals = f(x_vals) # x에 상응하는 y

    plt.plot(x_vals, y_vals, label='f(x)')
    plt.xlabel('x') 
    plt.ylabel('f(x)')
    plt.grid(True)
    plt.legend() # 오른 쪽에 뭐가 그려졌는지 표시해줌

    # 함수식 미분하기   
    f_prime_expr = sp.diff(f_expr, x)

    x0 = x_tan  # 접선을 그릴 x 좌표
    y0 = f(x0)  # 접선을 그릴 y 좌표
    f_prime = sp.lambdify(x, f_prime_expr, 'numpy')
    m = f_prime(x0)  # 기울기
    b = y0 - m * x0  # y절편 (접선의 방정식의 형태 : y= mx + b -> b = y-mx 의 형태로 씀)
    tangent_line = m * x_vals + b

    X_tan_text = str(x_tan) 

    plt.plot(x_vals, tangent_line, label='Tangent at x = ' + X_tan_text)
    plt.scatter ( x0, y0, color='red', label='Point(' + X_tan_text + ',f(' + X_tan_text + ')') 
    plt.legend()
    plt.title(f_expr)

    plt.show()

def graphing_trigono(f_expr) : # 삼각함수 그리는 함수
    global a, b, c, d, x_tan, x_cycle  # 전역 변수로 접근

    x = sp.Symbol('x')
    # 함수식 그래프 그리기
    abs_b = np.abs(b)
    f = sp.lambdify(x, f_expr, 'numpy') 

    if selected_value2 == 1 :
            x_vals = np.linspace((-1*x_cycle*np.pi)/(abs_b),(x_cycle*np.pi)/(abs_b), 100)
            
    elif selected_value2 == 2 : 
            x_vals = np.linspace((-1*x_cycle*np.pi)/(abs_b),(x_cycle*np.pi)/(abs_b), 100) 

    elif selected_value2 == 3 :
            x_vals = np.linspace((-0.5*x_cycle*np.pi)/(abs_b),(0.5*x_cycle*np.pi)/(abs_b), 50)
            plt.ylim(ymin=-10, ymax=10) # 탄젠트 함수의 y축을 과장되게 늘림 
    else :
            messagebox.showerror("오류")
            return
    
    y_vals = f(x_vals)

    plt.plot(x_vals, y_vals, label='f(x)')
    plt.xlabel('x') 
    plt.ylabel('f(x)')
    plt.grid(True)
    plt.legend()

    # 함수식 미분하기
    f_prime_expr = sp.diff(f_expr, x)
    x0 = x_tan  # 접선을 그릴 x 좌표
    y0 = f(x0)  # 접선을 그릴 y 좌표
    f_prime = sp.lambdify(x, f_prime_expr, 'numpy')
    m = f_prime(x0)  # 기울기
    b = y0 - m * x0  # y절편 (접선의 방정식의 형태 : y= mx + b -> b = y-mx 의 형태로 씀)
    tangent_line = m * x_vals + b

    X_tan_text = str(x_tan) 

    plt.plot(x_vals, tangent_line, label='Tangent at x = ' + X_tan_text)
    plt.scatter ( x0, y0, color='red', label='Point(' + X_tan_text + ',f(' + X_tan_text + ')') 
    plt.legend()
    plt.title(f_expr)

    plt.show()


def graphing_final(): #그래프 그리기
    global a, b, c, d , x_tan, x_start, x_last ,x_cycle # 전역 변수로 접근

    selected_value = radio_var.get()

    if selected_value == 1: #다항함수
        x = sp.Symbol('x')
        f_expr = a*x**3 + b*x**2 + c*x + d 
        graphing(f_expr)

    elif selected_value == 2: #유리함수 
        x = sp.Symbol('x')
        numerator = a*x + b
        denominator = c*x + d
        f_expr =  numerator / denominator  
        graphing(f_expr)
        
    elif selected_value == 3: #무리함수
        x = sp.Symbol('x')
        f_expr = a * sp.sqrt(b*x + c) + d 
        graphing(f_expr)

    elif selected_value == 4: #삼각함수
        global selected_value2

        if selected_value2 == 1 :
            x = sp.Symbol('x')
            f_expr = a*sp.sin(b*x + c) + d
            graphing_trigono(f_expr)

        elif selected_value2 == 2 : 
            x = sp.Symbol('x')
            f_expr = a*sp.cos(b*x + c) + d 
            graphing_trigono(f_expr)

        elif selected_value2 == 3 :
            x = sp.Symbol('x')
            f_expr = a*sp.tan(b*x + c) + d
            graphing_trigono(f_expr)
        else :  
            messagebox.showerror("오류")
            return
            
    elif selected_value == 5: # 지수함수
        global selected_value3 

        if selected_value3 == 1 :
            x = sp.Symbol('x')
            f_expr = d*sp.exp(x - b) + c
            graphing(f_expr)

        elif selected_value3 == 2 or 3 : 
            x = sp.Symbol('x')
            f_expr = d*(a**(x - b)) + c 
            graphing(f_expr)

        else :  
            messagebox.showerror("오류")
            return

    elif selected_value == 6: #로그함수

        if selected_value3 == 1 :
            x = sp.Symbol('x')
            f_expr = d*sp.log(x - b) + c
            graphing(f_expr)

        elif selected_value3 == 2 or 3 : 
            x = sp.Symbol('x')
            f_expr = d*sp.log(x-b, a) + c 
            graphing(f_expr)

        else :  
            messagebox.showerror("오류")
            return

    else:
        messagebox.showerror("오류")
        return 
   
# Tkinter 창 생성

window = tk.Tk()
window.title("그래프 그리기") #창 제목
window.geometry("500x300") # 창 사이즈 

# 라디오 버튼 변수
radio_var = tk.IntVar()

# 라디오 버튼 생성
radio_button1 = tk.Radiobutton(window, text="다항함수", variable=radio_var, value=1)
radio_button1.pack()

radio_button2 = tk.Radiobutton(window, text="유리함수", variable=radio_var, value=2)
radio_button2.pack()

radio_button3 = tk.Radiobutton(window, text="무리함수", variable=radio_var, value=3)
radio_button3.pack()

radio_button4 = tk.Radiobutton(window, text="삼각함수", variable=radio_var, value=4)
radio_button4.pack()

radio_button5 = tk.Radiobutton(window, text="지수함수", variable=radio_var, value=5)
radio_button5.pack()

radio_button6 = tk.Radiobutton(window, text="로그함수", variable=radio_var, value=6)
radio_button6.pack()

# 다음 버튼 생성
next_button = tk.Button(window, text="다음", command=open_input_window)
next_button.pack()

# Tkinter 창 실행
window.mainloop()