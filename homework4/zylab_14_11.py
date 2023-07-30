def selection_sort_descend_trace(numbers):
    for i in range(len(numbers) - 1):
        # Find index of largest remaining element for descending order
        index_largest = i
        for j in range(i + 1, len(numbers)):
            if numbers[j] > numbers[index_largest]:  # Compare for descending order
                index_largest = j

        # Swap numbers[i] and numbers[index_largest]
        temp = numbers[i]
        numbers[i] = numbers[index_largest]
        numbers[index_largest] = temp

        for index in numbers:
            print(index, end=' ')
        print()


if __name__ == "__main__":
    user_input = list(map(int, input().split()))
    selection_sort_descend_trace(user_input)

