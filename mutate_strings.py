start_string = input()
end_string = input()

for index in range(len(start_string)):
    if not start_string[index] == end_string[index]:
        left_side = end_string[:index + 1]
        right_side = start_string[index + 1:]
        print(left_side + right_side)
