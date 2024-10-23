def bubble_sort(arr):
    n = len(arr)
    # Traverse through all elements in the array
    for i in range(n):
        # Last i elements are already sorted
        for j in range(0, n - i - 1):
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

def main():
    # Take user input for the list of numbers
    user_input = input("Enter numbers separated by spaces: ")
    
    # Convert the input string into a list of integers
    arr = list(map(int, user_input.split()))
    
    print("Original array:", arr)
    
    # Perform Bubble Sort
    bubble_sort(arr)
    
    print("Sorted array:", arr)

if __name__ == "__main__":
    main()
