

class Sorting(object):
    random_arr : []

    @property
    def random_arr(self) -> []: return self._random_arr

    @random_arr.setter
    def random_arr(self, random_arr):self._random_arr = random_arr

    def bubble_sort(self):
        n = len(self.random_arr)
        array = self.random_arr
        for i in range(n - 1):
            for j in range(n -i -1):
                if array[j] > array [j+1]:
                    array[j],array[j+1] = array[j+1],array[j]
        return array

    @staticmethod
    def merge_sort(param:[]):
        arr = param
        if len(arr) < 2:
            return arr
        mid = len(arr) // 2
        print(f'mid: {mid}')
        low_arr = Sorting.merge_sort(arr[:mid])
        high_arr = Sorting.merge_sort(arr[mid:])

        arr = []
        l = h = 0
        while l < len(low_arr) and h < len(high_arr):
            if low_arr[l] < high_arr[h] :
                arr.append(low_arr[l])
                l += 1
            else:
                arr.append(high_arr[h])
                h += 1
        arr += low_arr[l:]
        arr += high_arr[h:]
        return arr

    @staticmethod
    def quick_sort(param):
        arr = param
        if len(arr) < 2:
            return arr
        pivot = len(arr) // 2
        arr1, arr2, arr3 = [] , [], []
        for value in arr:
            if value < arr[pivot]:
                arr1.append(value)
            elif value > arr[pivot]:
                arr3.append(value)
            else:
                arr2.append(value)
        return Sorting.quick_sort(arr1) + Sorting.quick_sort(arr2) + Sorting.quick_sort(arr3)
