# John Rebeles
# PSID: 2039426

# Global variable
num_calls = 0


# TODO: Write the partitioning algorithm - pick the middle element as the
#       pivot, compare the values using two index variables l and h (low and high),
#       initialized to the left and right sides of the current elements being sorted,
#       and determine if a swap is necessary
def partition(user_ids, i, k):
    # Pick middle value as pivot
    mid = i + (k - i) // 2
    pivot = user_ids[mid]

    # Initialize variables
    done = False
    l = i
    h = k

    while not done:
        while user_ids[l] < pivot:
            l += 1
        while pivot < user_ids[h]:
            h -= 1

        if l >= h:
            done = True
        else:
            temp = user_ids[l]
            user_ids[l] = user_ids[h]
            user_ids[h] = temp
            l += 1
            h -= 1

    return h


# TODO: Write the quicksort algorithm that recursively sorts the low and
#       high partitions. Add 1 to num_calls each time quisksort() is called


def quicksort(user_ids, i, k):
    global num_calls
    num_calls += 1

    if i >= k:
        return

    j = partition(user_ids, i, k)
    quicksort(user_ids, i, j)
    quicksort(user_ids, j + 1, k)
    return


if __name__ == "__main__":
    user_ids = []
    user_id = input()
    while user_id != "-1":
        user_ids.append(user_id)
        user_id = input()

    # Initial call to quicksort
    quicksort(user_ids, 0, len(user_ids) - 1)

    # Print number of calls to quicksort
    print(num_calls)

    # Print sorted user ids
    for user_id in user_ids:
        print(user_id)
