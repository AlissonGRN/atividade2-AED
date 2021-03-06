from node import Node


class LinkedList():
    def __init__(self):
        self.head = None
        self._size = 0

    def __len__(self):
        """Retorna o tamanho da lista"""
        return self._size

    def __getitem__(self, index):
        """Retorna o elemento no index especificado"""
        pointer = self.head
        for i in range(index):
            if pointer:
                pointer = pointer.next
            else:
                raise IndexError("list index out of range")
        if pointer:
            return pointer.data
        raise IndexError("list index out of range")

    def __setitem__(self, index, elem):
        """Adiciona um elemento na posição especificada"""
        pointer = self.head
        for i in range(index):
            if pointer:
                pointer = pointer.next
            else:
                raise IndexError("list index out of range")
        if pointer:
            pointer.data = elem
        else:
            raise IndexError("list index out of range")

    def append(self, elem):
        """Adiciona um elemento ao final da lista"""
        if self.head:
            # inserção enquanto a lista já possui elementos
            pointer = self.head
            while(pointer.next):
                pointer = pointer.next
            pointer.next = Node(elem)
        else:
            # primeira inserção na lista
            self.head = Node(elem)
        self._size += 1

    def index(self, elem):
        """Retorna a posição do elemento especificado"""
        pointer = self.head
        i = 0
        while(pointer):
            if pointer.data == elem:
                return i
            pointer = pointer.next
            i = i+1
        raise ValueError(f"{elem} is no in list")


lista = LinkedList()
lista.append(7)
