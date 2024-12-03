
input_list: list = open("days/1/input.txt").read().strip().split()

left_list: list = []
right_list: list = []
total_distance: int = 0

for i in range(len(input_list)):
    if i % 2 == 0:
        left_list.append(input_list[i])
    else:
        right_list.append(input_list[i])

for _ in range(len(left_list)):
    print(f"left list: {left_list}")
    print(f"right list: {right_list}")
    print(f"min left list: {min(left_list)}")
    print(f"min right list: {min(right_list)}")
    total_distance += abs(int(min(left_list)) - int(min(right_list)))
    
    print(f"Distance: {abs(int(min(left_list)) - int(min(right_list)))}")

    print(abs(int(min(left_list)) - int(min(right_list))))

    left_list.remove(min(left_list))
    right_list.remove(min(right_list))
    print(f"new left list: {left_list}")
    print(f"new right list: {right_list}")
    
    



print(total_distance)