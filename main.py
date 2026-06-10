N = int(input("N ni kiriting: "))

yigindi = 0

for i in range(1, N + 1):
    yigindi += i

print("Yig'indi:", yigindi)


matn = input("Matn kiriting: ")

sanoq = 0

for harf in matn.lower():
    if harf in "aeiou":
        sanoq += 1

print("Unlilar soni:", sanoq)


for son in range(10, 100):
    birlik = son % 10
    onlik = son // 10

    if birlik + onlik == 10:
        print(son)


n = int(input("Son kiriting: "))

faktorial = 1

for i in range(1, n + 1):
    faktorial *= i

print("Faktorial:", faktorial)


for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
