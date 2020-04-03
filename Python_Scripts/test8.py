friends = ["Kevin", "Karen", "Jim", "Oscar"]

print(friends)
print(friends[1])
print(friends[-1])
print(friends[1:])
print(friends[1:3])

friends[1] = "Mike"
print(friends[1:])
print(friends[1:3])

lucky_numbers = [4, 8, 15, 16, 23, 42]

#friends.extend(lucky_numbers)
print(friends)

friends.append("Creed")
print(friends)

friends.insert(1, "Kelly")
print(friends)

friends.remove("Jim")
print(friends)

friends.pop()
print(friends)

print(friends.index("Kevin"))

friends.append("Kevin")
print(friends.count("Kevin"))

friends.sort()
print(friends)

lucky_numbers.sort()
print(lucky_numbers)

lucky_numbers.reverse()
print(lucky_numbers)

friends2 = friends.copy()
print(friends2)

friends3 = friends
print(friends3)

friends3.append("Boo Boo")
print(friends3)
print(friends)
print(friends2)

friends.clear()
print(friends)