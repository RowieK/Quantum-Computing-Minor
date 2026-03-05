import random

def generate_random_numbers(n):
    random_numbers = []
    for _ in range(n):
        random_numbers.append(random.randint(1, 100))
    return random_numbers

def trace(matrix):
    trace = 0
    for i in range(len(matrix)):
        trace += matrix[i][i]
    return trace

def main():
    n = int(input("Enter the size of the matrix (n x n): "))
    matrix = []
    
    for i in range(n):
        row = generate_random_numbers(n)
        matrix.append(row)
    
    print("Generated Matrix:")
    for row in matrix:
        print(row)
    
    trace_value = trace(matrix)
    print(f"The trace of the matrix is: {trace_value}")

if __name__ == "__main__":
    main()