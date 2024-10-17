def generate_series(a):
    series = []
    for i in range(a):
        series.append(2 * i + 1)  # Generates odd numbers: 1, 3, 5, 7, etc.
    return series

# Example usage:
a = int(input("Enter a number (a): "))
output = generate_series(a)
print(", ".join(map(str, output)))