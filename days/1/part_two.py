
input_list: list = open("days/1/input.txt").read().strip().split()

left_list: list = []
right_list: list = []
total_count: int = 0

for i in range(len(input_list)):
    if i % 2 == 0:
        left_list.append(input_list[i])
    else:
        right_list.append(input_list[i])

for num in left_list:
    print(f"num: {num}")
    print(f"num occurences: {sum([1 for n in right_list if n == num])}")
    total_count += (int(num) * sum([1 for n in right_list if n == num]))

print(total_count)