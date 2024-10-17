def number(input_list):
    multiples_count = {i: 0 for i in range(1, 10)}  # Initialize dictionary for 1-9 with values 0

    for num in input_list:
        for i in range(1, 10):
            if num % i == 0:  # Check if num is divisible by i
                multiples_count[i] += 1

    return multiples_count


# Example usage:
input_list = [1, 2, 8, 9, 12, 46, 76, 82, 15, 20, 30]
result = number(input_list)
print(result)