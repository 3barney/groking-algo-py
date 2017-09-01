def binary_search(list, item_to_search):
	# Returns item index in the list
	low = 0
	high = len(list) - 1

	while low <= high:
		mid = (low + high) // 2
		guess = list[mid]

		if guess == item_to_search:
			return mid
		if guess > item_to_search:
			high = mid -1
		if guess < item_to_search:
			high = mid + 1
	return None


myList = [1,2,3,4,5,6,7,8]

print("here")
print(binary_search(myList, 3))
print(binary_search(myList, 9))
		
