import unittest
from linkedlist import Node
from linkedlist import LinkedList

class TestNodeAndList(unittest.TestCase):
    def test01_get_Data( self ):
        firstnode = Node(17)
        self.assertEqual( firstnode.getData() , 17)

    def test02_set_data(self):
        firstnode = Node(17)
        firstnode.setData(20)
        self.assertEqual(firstnode.getData(), 20)

    def test03_get_next_and_Set_Next(self):
        a = Node(12)
        a.setNext(14)
        self.assertEqual(a.getNext(), 14)

class TestLinkedList(unittest.TestCase):
    def test01_is_Empty(self):
        a = LinkedList()
        self.assertEqual(a.isEmpty(),True)

    def test02_Test_Add(self):
        a = LinkedList()
        a.add(1)
        a.add(2)
        a.add(3)
        self.assertEqual(a.add(4),4)

    def test03_Test_Size(self):
        a = LinkedList()
        a.add(1)
        a.add(2)
        a.add(3)
        self.assertEqual(a.size(), 3)

    def test04_Test_ToList(self):
        a = LinkedList()
        a.add(1)
        a.add(2)
        a.add(3)
        self.assertEqual(a.toList(),[3,2,1])

    def test05_Test_Search(self):
        a = LinkedList()
        a.add(1)
        a.add(2)
        a.add(3)
        self.assertEqual(a.search(2), True)

    def test06_Test_incert(self):
        a = LinkedList()
        a.add(1)
        a.add(2)
        a.add(3)
        self.assertEqual(a.insert(3,1), 3)

    def test02_Test_Remove(self):
        a = LinkedList()
        a.add(1)
        a.add(2)
        a.add(3)
        self.assertEqual(a.remove(2),True )





if __name__ == '__main__':
    unittest.main(verbosity=2)

lili = LinkedList()
lili.add(1)
lili.add(2)

lili.print()