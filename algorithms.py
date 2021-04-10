def array_advance(arr):
    furthest = 0
    for i in range(len(arr)):
        if i > furthest:
            return False
        furthest = max(furthest, i+arr[i])
    return furthest >= len(arr)-1

def plus_one(arr):
    carry_one = 1
    for ptr in range(len(arr)-1,-1, -1):
        if arr[ptr] < 9:
            arr[ptr] += 1
            carry_one = 0
            return arr
        else:
            arr[ptr] = 0
            ptr -= 1
    return [1] + arr

def plus_one_linkedlist(ll):
    if ll.head:
        curr = ll.head

        res = recursive_plus_one(curr)

        if res:
            ll.prepend(1)
    return ll

def recursive_plus_one(node):
    if node.next is None:
        node.data =  node.data + 1 if node.data < 9 else 0
        return 0 if node.data else 1
    else:
        carry_one = recursive_plus_one(node.next)
        if carry_one:
            node.data = node.data + 1 if node.data < 9 else 0
            carry_one = 0 if node.data else 1
        return carry_one

def two_sum(arr, sum_val):
    seen = dict()
    for elem in arr:
        if seen.get(sum_val - elem):
            return (sum_val-elem, elem)
        else:
            seen[elem] = 1
    return False

def find_closest_num(arr, val):
    low = 0
    high = len(arr)-1
    diff = float("inf")
    closest = 0

    while low < high-1:
        mid = (low+high)//2
        if arr[mid] == val:
            return val
        elif arr[mid] > val:
            high = mid-1
        else:
            low = mid+1
    
    mini =  min(abs(arr[low] - val), min(abs(arr[high] - val), abs(arr[mid] - val)))

    if mini == abs(arr[low]-val):
        return arr[low]
    elif mini == abs(arr[high]-val):
        return arr[high]
    else:
        return arr[mid]

def find_fixed_point(arr):
    low = 0
    high = len(arr)-1

    while low < high:
        mid = (low+high)//2
        if arr[mid] == mid:
            return mid
        elif arr[mid] < mid:
            low = mid+1 
        else:
            high = mid-1

#bisect_left, bisect_right, insort_left, insort_right

def look_and_say(s):
    output = []
    count = 1
    i = 0

    while i < len(s):
        while i+1 < len(s) and s[i] == s[i+1]:
            count += 1
            i += 1
        output.append(str(count) + s[i])
        i += 1

    return ''.join(output)

def spreadsheet_encode_column(col_str):
    output = 0
    count = len(col_str)-1
    for char in col_str:
        output += (ord(char)-64)* (26**count)
        count -=1
    return output


