class BinarySearchTree:
    def __init__(self, data=None):
        self._data = data
        self._left = None
        self._right = None

    def getData(self):
        return self._data

    def setData(self, d):
        self._data = d

    def isEmpty(self):
        return self._left == self._right == self._data == None

    def size(self):
        sz = 0
        if self._left:
            sz += self._left.size()
        if self.getData():
            sz += 1
        if self._right:
            sz += self._right.size()
        return sz

    def insert(self, x):
        if self.isEmpty():
            self.setData(x)
        elif x < self.getData():
            if self._left:
                self._left.insert(x)
            else:
                self._left = BinarySearchTree(x)
        else:  # x >= data
            if self._right:
                self._right.insert(x)
            else:
                self._right = BinarySearchTree(x)

    def delete(self,x, parrent=0):
        if x < self.getData():  # sök till vänster
            self._left = self._left.delete(x, self)
        elif x > self.getData():  # sök till höger
            self._right = self._right.delete(x, self)
        else:
            if not self._left and not self._right and parrent==None:
                self.setData(None)
            elif not self._left:
                return self._right
            elif not self._right:
                return self._left
            else:
                (psucc,succ) = self._right._finMin(self)
                if psucc.lef == succ:
                    psucc.left = succ._right
                else:
                    psucc.right = succ._right
                succ.left = self._left
                succ.right=self._right
                return succ
            return self





