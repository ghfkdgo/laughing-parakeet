from sympy import Rational

# 사용자로부터 분수를 문자열로 입력받기
fraction_str = input("분수를 입력하세요 (예: 3/4): ")

# 입력된 문자열을 '/'를 기준으로 분리하여 분자와 분모 추출
numerator, denominator = map(int, fraction_str.split('/'))

# 분자와 분모를 사용하여 SymPy의 Rational 클래스로 분수 생성
fraction = Rational(numerator, denominator)

# float 형태로 사용하기 위해 값 변환
fraction_float = fraction.evalf()

# float 형태로 사용
print(fraction_float)  # 출력: float 형태로 변환된 값

