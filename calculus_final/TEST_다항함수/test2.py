import sympy as sp
import matplotlib.pyplot as plt
import numpy as np

a, b, c, d = map(int, input( "다항식의 계수를 입력하시오 : ").split() )

# 함수식 정의하기
x = sp.Symbol('x')
f_expr = a*x**3 + b*x**2 + c*x + d  # 여기에 원하는 함수식을 입력하세요

# 함수식 그래프 그리기
f = sp.lambdify(x, f_expr, 'numpy')
x_vals = np.linspace(-10, 10, 400)
y_vals = f(x_vals)

plt.plot(x_vals, y_vals, label='f(x)')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid(True)
plt.legend()

# 함수식 미분하기
f_prime_expr = sp.diff(f_expr, x)

# 특정 점에서의 접선 그리기
e = float(input("접선을 구할 X좌표를 입력하시오 : "))
x0 = e  # 접선을 그릴 x 좌표
y0 = f(x0)  # 접선을 그릴 y 좌표
f_prime = sp.lambdify(x, f_prime_expr, 'numpy')
m = f_prime(x0)  # 기울기
b = y0 - m * x0  # y절편
tangent_line = m * x_vals + b

e_text = str(e) 

plt.plot(x_vals, tangent_line, label='Tangent at x = ' + e_text)
plt.scatter ( x0, y0, color='red', label='Point(' + e_text + ',f(' + e_text + ')') 
plt.legend()

plt.show()