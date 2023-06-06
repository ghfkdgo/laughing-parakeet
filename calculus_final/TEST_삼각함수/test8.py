import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

x = sp.symbols('x')
f_expr = sp.tan(x)

f = sp.lambdify(x, f_expr, 'numpy')
x_vals = np.linspace(-np.pi / 2, np.pi / 2, 100)
y_vals = f(x_vals)

# 그래프 그리기
plt.plot(x_vals, y_vals, linestyle='-', color='blue', linewidth=2, label='tan(x)')
plt.xlabel('x')
plt.ylabel('tan(x)')
plt.title('Graph of tan(x)')
plt.grid(True)

plt.xlim(-2*np.pi, 2*np.pi)  # x축 범위 설정

plt.legend()
plt.show()
