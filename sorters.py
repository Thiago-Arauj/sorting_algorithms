from random import shuffle
import timeit
import matplotlib.pyplot as plt


class Sorters:

    def input_handler(self, entry: list) -> bool:
        for item in entry:
            if type(item) is int:
                return True
            else:
                return False

    def heap_sort(self, entry: list) -> list | str:
        if not self.input_handler(entry):
            return "Please use a list containing only numbers"

        arr = entry.copy()
        n = len(arr)

        for i in range(n//2 - 1, -1, -1):
            self._heapify(arr, n, i)

        for i in range(n-1, 0, -1):
            arr[i], arr[0] = arr[0], arr[i]
            self._heapify(arr, i, 0)

        return arr

    def _heapify(self, arr: list, n: int, i: int) -> None:
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and arr[left] > arr[largest]:
            largest = left

        if right < n and arr[right] > arr[largest]:
            largest = right

        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            self._heapify(arr, n, largest)

    def merge(self, left: list, right: list) -> list:
        merged = []
        left_idx, right_idx = 0, 0

        while left_idx < len(left) and right_idx < len(right):
            if left[left_idx] < right[right_idx]:
                merged.append(left[left_idx])
                left_idx += 1
            else:
                merged.append(right[right_idx])
                right_idx += 1

        merged.extend(left[left_idx:])
        merged.extend(right[right_idx:])

        return merged

    def merge_sort(self, entry: list) -> list:
        if self.input_handler(entry):
            if len(entry) <= 1:
                return entry

            mid = len(entry) // 2
            left_half = entry[:mid]
            right_half = entry[mid:]

            left_half = self.merge_sort(left_half)
            right_half = self.merge_sort(right_half)

            return self.merge(left_half, right_half)

        else:
            return "Please use a list containing only numbers"


def generate_random_list(size: int) -> list:
    my_list = [x for x in range(size)]
    shuffle(my_list)
    return my_list


def benchmark_sorters():
    """Benchmarks all sort methods and plots their performance"""
    sorter = Sorters()
    sizes = [x*1000 for x in range(51)]
    algorithms = ['merge_sort', 'heap_sort']
    times = {alg: [] for alg in algorithms}

    for size in sizes:
        test_list = generate_random_list(size)

        for alg in algorithms:

            timer = timeit.Timer(
                f'sorter.{alg}(test_list.copy())', 
                globals={'sorter': sorter, 'test_list': test_list}
            )
            elapsed = min(timer.repeat(repeat=3, number=1)) * 1000
            times[alg].append(elapsed)
            print(f"{alg:10} | Size {size:5} | Time: {elapsed:.2f} ms")

    plt.figure(figsize=(10, 6))
    for alg in algorithms:
        plt.plot(sizes, times[alg], marker='o', label=alg)

    plt.title('Sorting Algorithm Performance Comparison')
    plt.xlabel('Input Size')
    plt.ylabel('Execution Time (miliseconds)')
    plt.legend()
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    benchmark_sorters()