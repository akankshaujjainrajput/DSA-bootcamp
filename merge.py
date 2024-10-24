def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2  # Finding the mid of the array
        left_half = arr[:mid]  # Dividing the elements into 2 halves
        right_half = arr[mid:]

        # Recursively sorting the first half
        merge_sort(left_half)
        # Recursively sorting the second half
        merge_sort(right_half)

        i = j = k = 0

        # Copy data to temp arrays L[] and R[]
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

def main():
    # Take user input for the list of numbers
    user_input = input("Enter numbers separated by spaces: ")
    
    # Convert the input string into a list of integers
    arr = list(map(int, user_input.split()))
    
    print("Original array:", arr)
    
    # Perform Merge Sort
    merge_sort(arr)
    
    print("Sorted array:", arr)

if __name__ == "__main__":
    main()
