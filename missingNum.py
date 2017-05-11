def find_missing(arr1, arr2):
    if len(arr1)==0 or len(arr2)==0:
        return 0
    if len(arr1)==len(arr2):
        return 0

# Set longer array to lst1, shorter to lst2
    if len(arr1) > len(arr2):
        list1 = arr1
        list2 = arr2
    else:
        list1 = arr2
        list2 = arr1
        for element in list1:
            if element not in list2:
                return element
