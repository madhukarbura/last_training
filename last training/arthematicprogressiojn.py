def is_arithmetic_progression(arr):
    if len(arr) < 2:
        return True  # An array with less than 2 elements is trivially in AP

    # Calculate the common difference
    common_difference = arr[1] - arr[0]

    # Check if every consecutive pair of elements has the same difference
    for i in range(2, len(arr)):
        if arr[i] - arr[i - 1] != common_difference:
            return False

    return True

# Example usage:
array = list(map(int,input().split()))
print(is_arithmetic_progression(array))  # Output should be True
