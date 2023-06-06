import sympy as sp
import matplotlib.pyplot as plt
import numpy as np

# 함수식 정의하기
x = sp.Symbol('x') ## symbols()는 기호를 선언 하는데 사용됨
f_expr = x**3 + 2*x**2 - 3*x + 5  # 여기에 원하는 함수식을 입력하세요

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
x0 = 2  # 접선을 그릴 x 좌표
y0 = f(x0)  # 접선을 그릴 y 좌표
f_prime = sp.lambdify(x, f_prime_expr, 'numpy')
m = f_prime(x0)  # 기울기
b = y0 - m * x0  # y절편
tangent_line = m * x_vals + b

plt.plot(x_vals, tangent_line, label='f_prime_(x) at x = 2', linestyle='dashed')
plt.scatter(x0, y0, color='red', label='Point (2, f(2))')
plt.legend()

plt.show()

