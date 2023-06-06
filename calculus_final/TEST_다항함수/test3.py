import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

# 함수식 정의하기
x = sp.Symbol('x')
f_expr = (3*x + 2) / (x - 1)

# 함수식을 NumPy 함수로 변환하기
f = sp.lambdify(x, f_expr, 'numpy')

# x 값 생성하기
x_vals = np.linspace(-10, 10, 400)

# y 값 계산하기
y_vals = f(x_vals)

# 그래프 그리기
plt.plot(x_vals, y_vals, label='f(x)')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid(True)
plt.legend()

plt.show()

## chatGPT가 써준 유리함수 출력 코드 , 점근선이 함께 출력 되는 문제가 있음