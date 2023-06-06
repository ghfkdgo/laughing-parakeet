import sympy as sp
import matplotlib.pyplot as plt
import numpy as np
from sympy import Rational 
import warnings
warnings.filterwarnings("ignore", category=RuntimeWarning)

bottom = int(input("지수함수의 밑 a가 \n 0 < a < 1 이면 1을 \n a > 1 이면 2를 입력하세요  "))

if bottom == 1 : 
    a_str = input("밑을 분수형태로 입력하세요 (예: 3/4) : ")
    numerator, denominator = map(int, a_str.split('/'))
    # 분자와 분모를 사용하여 SymPy의 Rational 클래스로 분수 생성
    fraction = Rational(numerator, denominator)
    # float 형태로 사용하기 위해 값 변환
    a = fraction.evalf()
elif bottom == 2 : 
    a = float(input("밑을 입력하세요 : "))

b, c = map(float, input( "X축, y축으로 몇 만큼 평행이동 하는지 x, y 순으로 입력하세요  : ").split() )

x = sp.Symbol('x')
f_expr = a**(x + b) +c 

f = sp.lambdify(x, f_expr, 'numpy')
x_vals = np.linspace(-5, 5, 100)
y_vals = f(x_vals)

plt.plot(x_vals, y_vals, label='f(x)')
plt.xlabel('x') 
plt.ylabel('f(x)')
plt.grid(True)
plt.legend()

f_prime_expr = sp.diff(f_expr, x)

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