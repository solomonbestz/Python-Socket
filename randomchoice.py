import random

enemy_x = []
enemy_y = []

x = range(1, 735, 100)
y = range(1, 50)

enemy_x.append(random.sample(x, 5))
enemy_y.append(random.sample(y, 5))

print(enemy_x)
print(enemy_y)
