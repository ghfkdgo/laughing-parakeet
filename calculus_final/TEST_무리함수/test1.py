import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

def graphing_rational(expr, x_vals):
    x = sp.Symbol('x')
    f_expr = sp.lambdify(x, expr, 'numpy')
    y_vals = f_expr(x_vals)

    plt.plot(x_vals, y_vals, label='f(x)')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.grid(True)
    plt.legend()
    plt.title('Rational Function')

    plt.show()

# 평행이동한 무리함수 표현
x = sp.Symbol('x')
a = 2  # 계수
expr = sp.sqrt(a * x) / (x**2 + 1) + 5  # 평행이동한 식

# x 범위 설정
x_vals = np.linspace(0, 10, 400)

# 그래프 출력
graphing_rational(expr, x_vals)
