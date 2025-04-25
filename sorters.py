from random import randint


class Sorters:

    def input_handler(self, entry: list) -> bool:
        for item in entry:
            if type(item) is int:
                pass
            else:
                return False

        return True

    def heap_sort(self, entry: list) -> list | str:
        if self.input_handler(entry):
            to_order = entry
            last_node = (len(to_order)//2)-1
            just_ordered = len(to_order)

            while True:
                child_left = last_node*2 + 1
                child_right = last_node*2 + 2

                if child_left >= just_ordered:
                    child_left = None

                if child_right >= just_ordered or child_right >= len(to_order):
                    child_right = None

                if child_left and child_right:

                    if (to_order[last_node] <= to_order[child_left]
                            or to_order[last_node] <= to_order[child_right]):

                        if (to_order[child_left]
                                >= to_order[child_right]):
                            temp = to_order[last_node]
                            to_order[last_node] = to_order[child_left]
                            to_order[child_left] = temp

                        elif (to_order[child_right]
                                >= to_order[child_left]):
                            temp = to_order[last_node]
                            to_order[last_node] = to_order[child_right]
                            to_order[child_right] = temp

                elif child_left:
                    if to_order[last_node] <= (to_order[child_left]):
                        temp = to_order[last_node]
                        to_order[last_node] = to_order[child_left]
                        to_order[child_left] = temp

                last_node -= 1

                if last_node < 0:
                    just_ordered -= 1
                    temp = to_order[0]
                    to_order[0] = to_order[just_ordered]
                    to_order[just_ordered] = temp
                    last_node = len(to_order[0:just_ordered:])//2-1
                    if just_ordered < 1:
                        break
            return to_order

        else:
            return "Please use a list containing just numbers"


def generate_random_list(size: int) -> list:
    my_list = []
    for i in range(size):
        while True:
            random = randint(0, size)
            if random in my_list:
                pass
            else:
                my_list.append(random)
                break

    return my_list


if __name__ == "__main__":
    sorter = Sorters()
    my_list = generate_random_list(1000)
    ordered = sorter.heap_sort(my_list)
    print(ordered)
