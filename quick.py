def quick_sort(arr):
    if len(arr) <= 1:  # Base case: arrays with 0 or 1 elements are already sorted
        return arr
    else:
        pivot = arr[len(arr) // 2]  # Choose the middle element as the pivot
        left = [x for x in arr if x < pivot]  # Elements less than the pivot
        middle = [x for x in arr if x == pivot]  # Elements equal to the pivot
        right = [x for x in arr if x > pivot]  # Elements greater than the pivot
        return quick_sort(left) + middle + quick_sort(right)  # Recursively sort the sub-arrays

def main():
    # Take user input for the list of numbers
    user_input = input("Enter numbers separated by spaces: ")
    
    # Convert the input string into a list of integers
    arr = list(map(int, user_input.split()))
    
    print("Original array:", arr)
    
    # Perform Quick Sort
    sorted_array = quick_sort(arr)
    
    print("Sorted array:", sorted_array)

if __name__ == "__main__":
    main()
