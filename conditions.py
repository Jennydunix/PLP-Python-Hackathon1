def main():
    try:
        age = int(input("Enter your age: "))  # Prompt the user to enter their age
        if age >= 18:  # Check if age is greater than or equal to 18
            print("You are eligible to vote.")
        else:
            print("You are not eligible to vote.")
    except ValueError:
        print("Please enter a valid age.")

if __name__ == "__main__":
    main()
