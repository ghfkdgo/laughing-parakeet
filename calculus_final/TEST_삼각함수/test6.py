import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

# 변수 정의
x = sp.symbols('x')

# 함수 정의
f_sin = sp.sin(x)
f_cos = sp.cos(x)

# 함수를 numpy 함수로 변환
f_np_sin = sp.lambdify(x, f_sin, 'numpy')
f_np_cos = sp.lambdify(x, f_cos, 'numpy')

# x값 생성
x_vals = np.linspace(-2*np.pi, 2*np.pi, 100)

# y값 계산
y_sin = f_np_sin(x_vals)
y_cos = f_np_cos(x_vals)

# 그래프 그리기
plt.figure(figsize=(8, 6))
plt.plot(x_vals, y_sin, label='sin(x)')
plt.plot(x_vals, y_cos, label='cos(x)')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Trigonometric Functions')
plt.legend()
plt.grid(True)
plt.show()
