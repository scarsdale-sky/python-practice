class Person:
  #初期設定
  def __init__(self,name,nationality,age):
    self.name = name
    self.nationality = nationality
    self.age = age

  def __call__(self):
    print("ここはcall関数です。")

  def say_hello(self,name):
    print("こんにちは、{}さん。私は{}です。".format(name,self.name))
class Sayan(Person):

  def __init__(self, name, nationality, age,strength):
    super().__init__(name,nationality,age)
    self.strength = strength
