def generate_series(a):
    # If a is even, treat it as a-1 for generating the series
    if a % 2 == 0:
        a -= 1

    series = []
    for i in range(1, a + 1, 2):  # Generate odd numbers from 1 up to a
        series.append(i)

    return series


# Example usage:
a = int(input("Enter a number (a): "))
output = generate_series(a)
print(", ".join(map(str, output)))
