def say_hello():
  print("みなさん、こんにちは。")

from datetime import date

base = 10
height = "5"

try:
  result = calc_tri(base,height)
  print("計算結果:{}".format(result))
except Exception as e:
  print("計算できません")
  print(e)
