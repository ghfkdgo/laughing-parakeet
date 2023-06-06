import sympy as sp
import matplotlib.pyplot as plt
import numpy as np

a, b, c, d, e = map(int, input( "다항식의 계수를 입력하시오 : ").split() )

# 함수식 정의하기
x = sp.Symbol('x')
f_expr = a*x**4 + b*x**3 + c*x**2 + d*x + e # 여기에 원하는 함수식을 입력하세요

# 함수식 그래프 그리기
f = sp.lambdify(x, f_expr, 'numpy') # sympy에서 만든 함수식을 numpy 로 변경해주기
x_vals = np.linspace(-10, 10, 400) # x : -10 ~ 10 사이를 400으로 균등하게 나눔
y_vals = f(x_vals) # x에 상응하는 y

plt.plot(x_vals, y_vals, label='f(x)')
plt.xlabel('x') 
plt.ylabel('f(x)')
plt.grid(True)
plt.legend() # 오른 쪽 상단에 뭐가 그려졌는지 표시해줌

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