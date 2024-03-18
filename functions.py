def fibonacci_sequence(n):
    sequence = [0, 1]  # Initialize the sequence with the first two terms
    for i in range(2, n):
        next_term = sequence[-1] + sequence[-2]  # Calculate the next term
        sequence.append(next_term)  # Append the next term to the sequence
    return sequence

def main():
    try:
        n = int(input("Enter the number of terms in the Fibonacci sequence: "))
        if n <= 0:
            print("Please enter a positive integer.")
            return
        fib_sequence = fibonacci_sequence(n)
        print("Fibonacci sequence up to term", n, "is:", fib_sequence)
    except ValueError:
        print("Please enter a valid integer.")

if __name__ == "__main__":
    main()
