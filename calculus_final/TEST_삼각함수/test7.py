import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

x = sp.Symbol('x') 

funtion_type = input("sin, cos, tan 함수중에 고르세요 (예: sin) : ")
a, b, c = map(float, input( "삼각함수의 계수, \n 몇 만큼 평행이동 했는지 x y 순으로 \n 입력하시오 : ").split() )

if funtion_type == "sin" :
    f_expr = a*sp.sin(x) + c 

elif funtion_type == "cos" :
    f_expr = a*sp.cos(x) + c

elif funtion_type == "tan" :
    f_expr = a*sp.tan(x) + c

else:
    print("잘못된 함수 종류입니다.")
    exit()

f = sp.lambdify(x, f_expr, 'numpy') 
x_vals = np.linspace(-2*np.pi, 2*np.pi, 100)
y_vals = f(x_vals + b)

plt.plot(x_vals, y_vals, label='f(x)')
plt.xlabel('x') 
plt.ylabel('f(x)')
plt.grid(True)
plt.legend()

# 함수식 미분하기
f_prime_expr = sp.diff(f_expr, x)

# 특정 점에서의 접선 그리기
X_tan = float(input("접선을 구할 X좌표를 입력하시오 : "))
x0 = X_tan  # 접선을 그릴 x 좌표
y0 = f(x0)  # 접선을 그릴 y 좌표
f_prime = sp.lambdify(x, f_prime_expr, 'numpy')
m = f_prime(x0)  # 기울기
b = y0 - m * x0  # y절편
tangent_line = m * x_vals + b

X_tan_text = str(X_tan) 

plt.plot(x_vals, tangent_line, label='Tangent at x = ' + X_tan_text)
plt.scatter ( x0, y0, color='red', label='Point(' + X_tan_text + ',f(' + X_tan_text + ')') 
plt.legend()
plt.title(f_expr)

plt.show()


