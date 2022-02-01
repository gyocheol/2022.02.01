# 21 letters가 바인딩하는 문자열에서 첫번째와 세번째 문자를 출력하세요.
letter = 'python'
print(letter[0],letter[2])

# 22 자동차 번호가 다음과 같을 때 뒤에 4자리만 출력하세요.
license_plate = "24가 2210"
print(license_plate[-4:])

# 23 아래의 문자열에서 '홀' 만 출력하세요.
string = "홀짝홀짝홀짝"
print(string[::2])

# 24 문자열을 거꾸로 뒤집어 출력하세요.
string2 = "PYTHON"
print(string2[::-1])

# 25 아래의 전화번호에서 하이푼 ('-')을 제거하고 출력하세요.
phone_number = "010-1111-2222"
print(phone_number.replace('-', ' '))

# 26 25번 문제의 전화번호를 아래와 같이 모두 붙여 출력하세요.
print(phone_number.replace('-', ''))

# 27 url 에 저장된 웹 페이지 주소에서 도메인을 출력하세요.
url = "http://sharebook.kr"
url_split = url.split(".")[-1]
print(url_split)

# 28 아래 코드의 실행 결과를 예상해보세요.
# lang = 'python'
# lang[0] = 'P'
# print(lang)

# 예상 결과 : 'Python'
# 정답 : TypeError: 'str' object does not support item assignment
#       문자열은 수정할 수 없다.

# 29 아래 문자열에서 소문자 'a'를 대문자 'A'로 변경하세요.
string3 = 'abcdfe2a354a32a'
str_replace = string3.replace('a', 'A')
print(str_replace)

# 30 아래 코드의 실행 결과를 예상해보세요.
string4 = 'abcd'
string4.replace('b', 'B')
print(string4)

# 예상 결과 : 변수 지정을 하지 않았기 때문에 abcd'가 그대로 나옴
# 정답 : abcd가 그대로 출력됩니다. 왜냐하면 문자열은 변경할 수 없는 자료형이기 때문입니다.
#       replace 메서드를 사용하면 원본은 그대로 둔채로 변경된 새로운 문자열 객체를 리턴해줍니다.
