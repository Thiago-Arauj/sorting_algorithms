from random import shuffle
import timeit
import matplotlib.pyplot as plt


# Classe que implementa algoritmos de ordenação
class Sorters:

    # Verifica se todos os itens da lista são inteiros
    def input_handler(self, entry: list) -> bool:
        for item in entry:
            if type(item) is int:
                return True  # Retorna True se o item for um inteiro
            else:
                return False  # Retorna False se encontrar qualquer tipo diferente
        # OBS: Essa verificação está incorreta, pois retorna após o primeiro item. Ver comentário ao final.

    # Implementação do Heap Sort
    def heap_sort(self, entry: list) -> list | str:
        if not self.input_handler(entry):
            return "Please use a list containing only numbers"  # Validação de entrada

        arr = entry.copy()
        n = len(arr)

        # Constrói o heap máximo
        for i in range(n//2 - 1, -1, -1):
            self._heapify(arr, n, i)

        # Extrai elementos do heap um por um
        for i in range(n-1, 0, -1):
            arr[i], arr[0] = arr[0], arr[i]  # Move o maior para o final
            self._heapify(arr, i, 0)  # Reorganiza o heap

        return arr

    # Função auxiliar para manter a propriedade do heap
    def _heapify(self, arr: list, n: int, i: int) -> None:
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        # Verifica se o filho da esquerda é maior
        if left < n and arr[left] > arr[largest]:
            largest = left

        # Verifica se o filho da direita é maior
        if right < n and arr[right] > arr[largest]:
            largest = right

        # Se o maior não for o nó atual, troca e faz _heapify recursivamente
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            self._heapify(arr, n, largest)

    # Função que mescla duas listas ordenadas (parte do Merge Sort)
    def merge(self, left: list, right: list) -> list:
        merged = []
        left_idx, right_idx = 0, 0

        # Junta os dois arrays ordenadamente
        while left_idx < len(left) and right_idx < len(right):
            if left[left_idx] < right[right_idx]:
                merged.append(left[left_idx])
                left_idx += 1
            else:
                merged.append(right[right_idx])
                right_idx += 1

        # Adiciona os elementos restantes
        merged.extend(left[left_idx:])
        merged.extend(right[right_idx:])

        return merged

    # Implementação do Merge Sort
    def merge_sort(self, entry: list) -> list:
        if self.input_handler(entry):
            if len(entry) <= 1:
                return entry  # Lista já ordenada

            mid = len(entry) // 2
            left_half = entry[:mid]
            right_half = entry[mid:]

            # Recursivamente ordena as metades
            left_half = self.merge_sort(left_half)
            right_half = self.merge_sort(right_half)

            return self.merge(left_half, right_half)  # Mescla as duas metades ordenadas
        else:
            return "Please use a list containing only numbers"  # Validação de entrada


# Gera uma lista embaralhada de tamanho especificado
def generate_random_list(size: int) -> list:
    my_list = [x for x in range(size)]
    shuffle(my_list)
    return my_list


# Função que compara o desempenho dos algoritmos de ordenação
def benchmark_sorters():
    """Executa testes de tempo nos algoritmos e plota os resultados"""
    sorter = Sorters()
    sizes = [x * 1000 for x in range(51)]  # Tamanhos de entrada de 0 a 50.000 em passos de 1.000
    algorithms = ['merge_sort', 'heap_sort']  # Algoritmos testados
    times = {alg: [] for alg in algorithms}  # Dicionário para armazenar tempos

    for size in sizes:
        test_list = generate_random_list(size)

        for alg in algorithms:
            # Mede o tempo da execução do algoritmo
            timer = timeit.Timer(
                f'sorter.{alg}(test_list.copy())',
                globals={'sorter': sorter, 'test_list': test_list}
            )
            elapsed = min(timer.repeat(repeat=3, number=1)) * 1000  # Pega o menor tempo em milissegundos
            times[alg].append(elapsed)
            print(f"{alg:10} | Size {size:5} | Time: {elapsed:.2f} ms")

    # Plota os resultados
    plt.figure(figsize=(10, 6))
    for alg in algorithms:
        plt.plot(sizes, times[alg], marker='o', label=alg)

    plt.title('Sorting Algorithm Performance Comparison')
    plt.xlabel('Input Size')
    plt.ylabel('Execution Time (miliseconds)')
    plt.legend()
    plt.grid(True)
    plt.show()


# Executa o benchmark se o script for rodado diretamente
if __name__ == "__main__":
    benchmark_sorters()
