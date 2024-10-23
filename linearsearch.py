def linear_search(arr, target):
    for index, value in enumerate(arr):
        if value == target:
            return index  # Return the index if the target is found
    return -1  # Return -1 if the target is not found

def main_linear():
    # Take user input for the list of numbers
    user_input = input("Enter numbers separated by spaces: ")
    
    # Convert the input string into a list of integers
    arr = list(map(int, user_input.split()))
    
    target = int(input("Enter the number to search for: "))
    
    # Perform Linear Search
    result = linear_search(arr, target)
    
    if result != -1:
        print(f"Number {target} found at index {result}.")
    else:
        print(f"Number {target} not found in the array.")

if __name__ == "__main__":
    main_linear()
