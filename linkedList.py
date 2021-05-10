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

    def append(self, elem):
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


lista = LinkedList()
lista.append(7)
