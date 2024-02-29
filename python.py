# print("hello, world")

# for i in range(10):
#   print(f'Hello {i}')

# def seperate():
#   a = int(input('자연수 중 하나를 입력하세요: '))
#   if a % 2 == 0:
#     print('짝수')
#   else:
#     print('홀수')

# seperate()

# for i in [1,2,3,4,5,6,7,8,9]:
#   if i % 2 == 0:
#     print(i, '짝수')
#   else:
#     print(i, '홀수')

def package_price():
  service = input('패키지 종류를 입력하세요, 유럽/일본/홍콩: ')
  valueAdded = input('부가세를 포함합니까? y/n: ')
  price = [5000000, 2500000, 1800000]
  if valueAdded == 'y':
    if service == '유럽':
      result = price[0] * 1.1
    if service == '일본':
      result = price[1] * 1.1
    if service == '홍콩':
      result = price[2] * 1.1
  if valueAdded == 'n':
    if service == '유럽':
      result = price[0]
    if service == '일본':
      result = price[1]
    if service == '홍콩':
      result = price[2]
  print(round(result, 1), '만 원입니다.')

package_price()