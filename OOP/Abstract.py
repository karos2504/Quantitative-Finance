class Sort:
    def sort(self):
        pass

class SelectionSort(Sort):
    def sort(self):
        print('Selection Sort')

class QuickSort(Sort):
    def sort(self):
        print('Quick Sort')

num = int(input('Input a number for sort: 0: selection sort, 1: quick sort '))

sort = Sort()
sort = None

if num == 0:
    sort = SelectionSort()
if num == 1:
    sort = QuickSort()

sort.sort()