import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

# 변수 정의
x = sp.symbols('x')

# 함수 정의
f_log = sp.log(x-5, 10)  # 밑이 10인 로그 함수

# 함수를 numpy 함수로 변환
f_np_log = sp.lambdify(x, f_log, 'numpy')

# x값 생성
x_vals = np.linspace(5, 15, 100)

# y값 계산
y_log = f_np_log(x_vals)

# 그래프 그리기
plt.figure(figsize=(8, 6))
plt.plot(x_vals, y_log, label='log_10(x)')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Logarithm Function (Base 10)')
plt.legend()
plt.grid(True)
plt.show()

