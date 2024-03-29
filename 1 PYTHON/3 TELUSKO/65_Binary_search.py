#   in binary search u r values should be in sorted order

pos = -1


def search(list, n):
    l = 0
    u = len(list) - 1

    while l <= u:
        mid = (l + u) // 2
        if list[mid] == n:
            globals()['pos'] = mid
            return True
        else:
            if list[mid] < n:
                l = mid + 1
            else:
                u = mid - 1
    return False


list = [4, 7, 8, 12, 46, 99]
n = 12

if search(list, n):
    print("Found at", pos)
else:
    print("Not Found")
