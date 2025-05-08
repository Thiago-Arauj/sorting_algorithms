from random import shuffle
import timeit
import matplotlib.pyplot as plt


class Sorters:
    def __init__(self):
        self.comparisons = 0  # contador de comparações

    def input_handler(self, entry: list) -> bool:
        return all(isinstance(item, int) for item in entry)

    def heap_sort(self, entry: list) -> list | str:
        if not self.input_handler(entry):
            return "Please use a list containing only numbers"

        self.comparisons = 0  # reseta o contador
        arr = entry.copy()
        n = len(arr)

        for i in range(n // 2 - 1, -1, -1):
            self._heapify(arr, n, i)

        for i in range(n - 1, 0, -1):
            arr[i], arr[0] = arr[0], arr[i]
            self._heapify(arr, i, 0)

        return arr

    def _heapify(self, arr: list, n: int, i: int) -> None:
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n:
            self.comparisons += 1
            if arr[left] > arr[largest]:
                largest = left

        if right < n:
            self.comparisons += 1
            if arr[right] > arr[largest]:
                largest = right

        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            self._heapify(arr, n, largest)

    def merge(self, left: list, right: list) -> list:
        merged = []
        left_idx, right_idx = 0, 0

        while left_idx < len(left) and right_idx < len(right):
            self.comparisons += 1
            if left[left_idx] < right[right_idx]:
                merged.append(left[left_idx])
                left_idx += 1
            else:
                merged.append(right[right_idx])
                right_idx += 1

        merged.extend(left[left_idx:])
        merged.extend(right[right_idx:])

        return merged

    def merge_sort(self, entry: list) -> list | str:
        if not self.input_handler(entry):
            return "Please use a list containing only numbers"

        self.comparisons = 0  # reseta o contador
        return self._merge_sort_recursive(entry)

    def _merge_sort_recursive(self, entry: list) -> list:
        if len(entry) <= 1:
            return entry

        mid = len(entry) // 2
        left_half = self._merge_sort_recursive(entry[:mid])
        right_half = self._merge_sort_recursive(entry[mid:])

        return self.merge(left_half, right_half)


def generate_random_list(size: int) -> list:
    my_list = [x for x in range(size)]
    shuffle(my_list)
    return my_list


def benchmark_sorters():
    sorter = Sorters()
    sizes = [x * 1000 for x in range(1, 51)]  # de 1000 a 20000
    algorithms = ['merge_sort', 'heap_sort']
    times = {alg: [] for alg in algorithms}
    comparisons = {alg: [] for alg in algorithms}

    for size in sizes:
        test_list = generate_random_list(size)

        for alg in algorithms:
            sorter.comparisons = 0  # reseta antes de cada chamada

            # Mede tempo de execução
            timer = timeit.Timer(
                f'sorter.{alg}(test_list.copy())',
                globals={'sorter': sorter, 'test_list': test_list}
            )
            elapsed = min(timer.repeat(repeat=3, number=1)) * 1000  # milissegundos

            times[alg].append(elapsed)
            comparisons[alg].append(sorter.comparisons)

            print(
                f"{alg:10} | Size {size:5} |"
                f" Time: {elapsed:.2f} ms | Comparisons: {sorter.comparisons}"
            )

    # Gráfico de tempo
    plt.figure(figsize=(12, 6))
    for alg in algorithms:
        plt.plot(sizes, times[alg], marker='o', label=f"{alg} - tempo")
    plt.title("Tempo de Execução dos Algoritmos de Ordenação")
    plt.xlabel("Tamanho da Entrada")
    plt.ylabel("Tempo (ms)")
    plt.legend()
    plt.grid(True)
    plt.show()

    # Gráfico de comparações
    plt.figure(figsize=(12, 6))
    for alg in algorithms:
        plt.plot(
            sizes,
            comparisons[alg],
            marker='x',
            label=f"{alg} - comparações"
        )
    plt.title("Número de Comparações dos Algoritmos de Ordenação")
    plt.xlabel("Tamanho da Entrada")
    plt.ylabel("Comparações")
    plt.legend()
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    benchmark_sorters()
