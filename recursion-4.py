def unique_ways_to_climb_stairs(n):
    if n <= 1:
        return 1
    return unique_ways_to_climb_stairs(n - 1) + unique_ways_to_climb_stairs(n - 2)

n1 = 2
n2 = 3
print("Для n = 2:", unique_ways_to_climb_stairs(n1))
print("Для n = 3:", unique_ways_to_climb_stairs(n2))
