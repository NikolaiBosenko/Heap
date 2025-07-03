def get_info():
    """Куча это бинарное дерево, где родитель меньше каждого из своих детей"""

def get_min(Heap) -> int | float: #получаем минимум
    return print(Heap[0])

def add(x, Heap) -> list: #добавляем элемент в кучу
    if x in Heap:
        raise ValueError("Куча должна содержать уникальный элементы!")
    Heap.append(x)
    return swift_up(x, Heap)  #дабвляем элемент в конец и просеиваем наверх

def extract_min(Heap): # удаление минимума
    print(Heap[0])
    Heap[0] = Heap[len(Heap)-1]
    del Heap[len(Heap)-1]
    return swift_down(Heap[0], Heap) #меняем местами последний и первый элемент, а потом просеиваем его вниз



def swift_up(x, Heap, index=None): #операция просеивания вверх поднимает элемент, оставляя за собой нормальную кучу

    if index is None:
        index = len(Heap)-1
    x = Heap[index]
    if index == 0: #если элемент в корне - просеивать наверх некуда и данный элемент минимум, поэтому завершаем просеивание
        return Heap
    elif x < Heap[index//2]: #если предок текущей вершины больше, то неравенство кучи нарушено и мы меняем текущий элемент с его предком
        Heap[index//2], Heap[index] = Heap[index], Heap[index//2]
        index = index//2
    else:
        return Heap #если для текущей (вершины, которую просеиваем) неравенство кучи выполняется, мы завершаем просеивание - куча корректна
    return swift_up(Heap[index], Heap, index) #рекурсивно вызываем сортировку, пока не отсортируем


def swift_down(x, Heap, index = None): #просеивание вниз опускает элемент вниз пока не получится корректная куча

    if index is None:
        index = 0
    x = Heap[index] #элемент, который будем просеивать
    if len(Heap)-1 < 2*index+1 or (x < min(Heap[2*index+1], Heap[2*index+2])): #если у вершины нет потомков или неравенство кучи выполняется завершаем сортировку
        return Heap
    elif 2*index+1 == len(Heap)-1 and x > Heap[index+1]: #если один больший потомок, то меняем местами
        Heap[index], Heap[2*index+1] = Heap[2*index+1], Heap[index]
        index = 2*index + 1
    elif 2*index+2 <= len(Heap)-1: #если два сына меньших
        if x > Heap[2*index+1] and x > Heap[2*index+2]:
            if Heap[2*index+1] < Heap[2*index+2]: #меняем местами с меньшим
                Heap[2 * index + 1], Heap[index] = Heap[index], Heap[2*index+1]
                index = 2*index+1
            elif Heap[2 * index + 2] <= Heap[2 * index + 1]:
                Heap[2 * index + 2], Heap[index] = Heap[index], Heap[2 * index + 2]
                index = 2 * index + 2
        elif x > Heap[2*index+1]: #если меньше только один
            Heap[2 * index + 1], Heap[index] = Heap[index], Heap[2 * index + 1]
            index = 2 * index + 1
        elif x > Heap[2*index + 2]:
            Heap[2 * index + 2], Heap[index] = Heap[index], Heap[2 * index + 2]
            index = 2 * index + 2
    return swift_down(x, Heap, index) #вызываем рекурсивно пока не просеим
Heap: list = []
add(3, Heap)
add(5, Heap)
add(7, Heap)
add(2, Heap)
add(9, Heap)
add(11, Heap)
print(Heap)
get_min(Heap)
extract_min(Heap)
print(Heap)

