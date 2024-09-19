
# lucky digit 

import pdb
pdb.set_trace()

def generate_lucky_numbers(limit):
    numbers = list(range(1, limit + 1))
    index = 1  # Start with the second position (index 1, value 2)
    
    while index < len(numbers):
        step = numbers[index]
        if step > len(numbers):
            break
        # Remove every `step`th number from the list
        numbers = [num for i, num in enumerate(numbers) if (i + 1) % step != 0]
        index += 1
    
    return numbers

def is_lucky_number(n):
    # Generate lucky numbers up to a reasonable limit
    limit = max(n, 100)  # Ensure we generate enough numbers
    lucky_numbers = generate_lucky_numbers(limit)
    
    # Check if the given number n is in the list of lucky numbers
    return n in lucky_numbers

# Main function to get user input and check if it is a lucky number
if __name__ == "__main__":
    try:
        user_input = int(input("Enter a number to check if it's a lucky number: "))
        if is_lucky_number(user_input):
            print(f"{user_input} is a lucky number.")
        else:
            print(f"{user_input} is not a lucky number.")
    except ValueError:
        print("Please enter a valid integer.")