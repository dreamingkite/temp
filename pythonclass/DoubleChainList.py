class DoubleLinkNode:
    def __init__(self,data = None):
        self.__former = None
        self.__data = data
        self.__after = None

    @property
    def former(self):
        return self.__former
    @former.setter
    def former(self,value):
        self.__former = value

    @property
    def data(self):
        return self.__data
    @data.setter
    def data(self,value):
        self.__data = value

    @property
    def after(self):
        return self.__after
    @after.setter
    def after(self,value):
        self.__after = value

class DoubleLinkList:
    def __init__(self):
        self._seq = 0
        self._container = {}  # datastructer {seq:{former:x,data:x,after:x},seq:{former:x,data:x,after:x})
        self._left_tail = 0
        self._right_tail = 0

    def _genSeq(self):
        self._seq += 1
        return self._seq

    def append(self,value,reverse=False,index=None):
        _tmpSeq = self._genSeq() if not index else index
        if not reverse:
            if self._container:
                self._container[_tmpSeq] = DoubleLinkNode(value)
                self._container[_tmpSeq].former = self._right_tail
                self._container[self._right_tail].after = _tmpSeq
            else:
                self._container[_tmpSeq] = DoubleLinkNode(value)
                self._left_tail = _tmpSeq
            self._right_tail = _tmpSeq
        else:
            if self._container:
                self._container[_tmpSeq] = DoubleLinkNode(value)
                self._container[_tmpSeq].after = self._left_tail
                self._container[self._left_tail].former = _tmpSeq
            else:
                self._container[_tmpSeq] = DoubleLinkNode(value)
                self._right_tail = _tmpSeq
            self._left_tail = _tmpSeq

    def iternodes(self,reverse=False):
        tmp_point = self._left_tail if not reverse else self._right_tail
        tmp_end = self._right_tail if not reverse else self._left_tail
        while self._container:
            yield (tmp_point,self._container[tmp_point].data)
            if not reverse:
                if self._container[tmp_point].after == None:
                    break
                else:
                    tmp_point = self._container[tmp_point].after
            else:
                if self._container[tmp_point].former == None:
                    break
                tmp_point = self._container[tmp_point].former

    def pop(self,reverse=False):
        if not reverse:
            tmp_point = self._container[self._right_tail].former
            self._container[tmp_point].after = None
            self._container.pop(self._right_tail)
            self._right_tail = tmp_point
        else:
            tmp_point = self._container[self._left_tail].after
            self._container[tmp_point].former  = None
            self._container.pop(self._left_tail)
            self._left_tail = tmp_point

    def insert(self,index,object):
        _tmpSeq = self._genSeq()
        self._container[_tmpSeq] = DoubleLinkNode(self._container[index].data)
        self._container[_tmpSeq].former = index
        self._container[_tmpSeq].after = self._container[index].after
        self._container[index].data = object
        self._container[index].after = _tmpSeq

    def remove(self,index):
        def _remove(index):
            self._container[self._container[index].former].after = self._container[index].after
            self._container[self._container[index].after].former = self._container[index].former
            self._container.pop(index)
        if index == self._right_tail:
            self.pop()
        elif index == self._left_tail:
            self.pop(False)
        else:
            _remove(index)

    def __getitem__(self, item):
        ret = self._container.get(item,None)
        if ret:
            return (ret.former,ret.data,ret.after)
        else:
            return

    def __iter__(self):
        return self.iternodes()

    def __setitem__(self, key, value):
        if key in self._container.keys():
            self._container[key].data = value
        else:
            self.append(value,index=key)

a = DoubleLinkList()
a.append("abc")
a.append("bcd")
a.append("3",reverse=True)
a.append("10000",reverse=True)
a.append("celpphone")
a.append(list("abd"))
print(a._container)
print(a[2])
for x in a:
    print(x)
a[3] = "abcefgd"
print(a[3])