# python code implementation (FULL)
def main():
	arr = [1,5,2,9,1]
	bubble_sort(arr)
	print(arr)

def bubble_sort(arr):
	n = len(arr)
	for i in range(n):
		for j in range(0, n-i-1):
			if(arr[j] > arr[j+1]):
				swap(arr, j, j+1)
			else:
				pass

def swap(arr, i, j):
	temp = arr[i]
	arr[i] = arr[j]
	arr[j] = temp
	
main()
