def solve(jug1_capacity, jug2_capacity, target_amount):
    small_jug = 0
    large_jug = 0
    small_capacity = min(jug1_capacity, jug2_capacity)
    large_capacity = max(jug1_capacity, jug2_capacity)

    print("\nInitial Values  :")
    print("small jug : ", small_jug, "\nlarge jug : ", large_jug)
    count = 0
    while small_jug != target_amount:
        count += 1
        if count == 7:
            return False

        if small_jug == 0:
            print("\nFilling small jug ")
            small_jug += small_capacity
        elif small_jug == small_capacity:
            print("\nPouring small jug into large jug until possible")
            while small_jug != 0 and large_jug != large_capacity:
                large_jug += 1
                small_jug -= 1

        print("small jug : ", small_jug, "\nlarge jug : ", large_jug)

    large_jug = small_jug
    small_jug = 0
    print("\nFinal Result : ")
    print("small jug : ", small_jug, "\nlarge jug : ", large_jug)
    return True



jug1_capacity = int(input("Enter the capacity of the first jug: "))
jug2_capacity = int(input("Enter the capacity of the second jug: "))
target = int(input("Enter the target amount of water to be left in the larger jug: "))

if solve(jug1_capacity, jug2_capacity, target):
    print("\nSolution exist")
else:
    print("\nSolution does not exist")
