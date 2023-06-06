import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

x = sp.Symbol('x')
numerator = 1
denominator = x 

f_expr = numerator / denominator

f = sp.lambdify(x, f_expr, 'numpy')  # sympy 함수를 numpy 함수로 변환

x_vals = np.linspace(-10, 10, 400)  # x값 범위 설정
y_vals = f(x_vals)  # x에 대한 y값 계산

plt.plot(x_vals, y_vals)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid(True)
plt.show()
