time = [54,94,65,92]
distance = [302,1476,1029,1404]

# Brute Force for Part One
count_prod = 1
for i in range(4):
  count = 0
  for t in range(1,time[i]+1):
    T, D = time[i], distance[i]
    if( (T - t) * t > D):
      count += 1
  print(f"{i}: {count}")
  count_prod *= count
print(f"Part One: {count_prod}")

# t₁: time accelerating (acceleration = 1)
# t₂: time running
# T: total time
# v: velocity
# d: total distance
# v = t₁
# d = v⋅t₂ = t₁⋅t₂ = t₁⋅(T-t₁)
# D: record distance
# We want to find out what are the conditions to solve
# d > D
# t₁⋅(T-t₁) > D
# t₁⋅T - t₁² > D
# t₁² - T⋅t₁ + D < 0
# It's a concave upward parabola and we want to find out when it's below zero
# t₁ = [T ± √(T² - 4⋅D)]/2

# Let's compare with the theory
import math

for i in range(4):
  T, D = time[i], distance[i]
  t1 = math.ceil( ( T - math.sqrt(T*T-4*D) ) / 2) # rounding up
  t2 = math.floor( (T + math.sqrt(T*T-4*D) ) / 2) # rounding down

  print(f"{i}: {t1} ~ {t2} : {t2-t1+1}")

# OK, let's consider the input as one race
T = 54946592
D = 302147610291404
t1 = math.ceil( ( T - math.sqrt(T*T-4*D) ) / 2)
t2 = math.floor( (T + math.sqrt(T*T-4*D) ) / 2)
print(f"{t1} ~ {t2} : {t2-t1+1}")

print(f"Part Two {t2-t1+1}")

