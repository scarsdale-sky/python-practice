#Day1
name = "Sky"
age = 13
print(name,age)
print(type(name),type(age))

#Day2
score = 86

if score >= 80:
    print("優")
elif score >= 60:
    print("良")
else:
    print("不可")

#Day3
for i in range(1,11):
    print(i)

#Day4
scores = [70,80,90]
scores.append(100)

print(sum(scores))
print(sum(scores)/len(scores))

#Day5
car = {
    "maker":"Toyota",
    "year":2020,
    "engine":"Hybrid"
}

print(car["maker"])

