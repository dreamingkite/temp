import datetime

class  SingleLinkList:
    def __init__(self):
        self._seq = 0
        self._head = self._seq
        self._tail = self._seq
        self._container = {}            #datastructre {seq:[data,next_seq]}

    def _genSeq(self):
        self._seq += 1
        return self._seq

    def append(self,value):
        _temp_count = self._genSeq()
        if self._container:
            self._container[self._tail] = [self._container[self._tail][0],_temp_count]
        else:
            self._head = _temp_count
        self._container[_temp_count] = [value, None]
        self._tail = _temp_count

    def iternodes(self):
        self._tempPoint = self._head
        while self._container:
            yield self._container.get(self._tempPoint)[0]
            if self._container[self._tempPoint][1] == None:
                break
            self._tempPoint = self._container.get(self._tempPoint)[1]





