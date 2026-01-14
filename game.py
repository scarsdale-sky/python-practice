import random
answer = random.randint(1,10)

while True:
    guess = int(input("一から十の数字を当てて："))

    if guess == answer:
        print("正解！🎉")
        break
    else:
        print("はずれ！正解は",answer)
        print("もう一回挑戦してみよう！")
