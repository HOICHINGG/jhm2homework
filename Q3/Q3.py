Addition_table_size = int(input("Input Addition Table Size smaller 10 : "))

print("Addition Table")
for x in range(1, Addition_table_size + 1):
    for y in range(1, Addition_table_size + 1):
        result = x + y
        if result < 10:
            print(f"{x} + {y} = {result}  ", end="")
        else:
            print(f"{x} + {y} = {result} ", end="")
    print()