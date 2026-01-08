import random
answer = random.randint(1,10)
guess = input("一から十の数字を当てて：")
print("あなたが入れた数字は",guess)
guess = int(guess)

if guess == answer:
    print("正解！🎉")
else:
    print("はずれ！正解は",answer)
