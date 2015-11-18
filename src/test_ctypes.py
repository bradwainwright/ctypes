import os,sys
import ct_transTest as tr
import numpy as np
import ctypes as ct
class test_matrix(object):
    def __init__(self,row,col):
        self.r = row
        self.c = col
        self.theList = tr.make2Darray(self.r,self.c)
        self.outList = tr.make2Darray(self.c,self.r,True)
        self.np_in_array = tr.make2dNpArray(self.r,self.c)
        self.np_out_array = tr.make2dNpArray(self.c,self.r,True)
        self.ct_in_array = tr.convert2DtoCtypeArray(self.theList,self.r,self.c)
        self.ct_out_array = tr.convert2DtoCtypeArray(self.outList,self.c,self.r)
    def test_transpose2DMatrixPyArr(self):
        return tr.transpose2DMatrixPyArr(self.ct_in_array,self.ct_out_array,self.r,self.c)
    def test_transpose2DMatrixIncCtypeConv(self):
        ct_in_array = tr.convert2DtoCtypeArray(self.theList,self.r,self.c)
        ct_out_array = tr.convert2DtoCtypeArray(self.outList,self.c,self.r)
        return tr.transpose2DMatrixPyArr(ct_in_array,ct_out_array,self.r,self.c)
    def test_transpose2DwithZip(self):
        return zip(*self.theList)
    def test_transpose2DlistComp(self):
        return [ [ self.theList[j][i] for j in range(len(self.theList))] for i in range(len(self.theList[0]))]
    def test_transpose2DMatrixNdarrayCtype(self):
        return tr.transpose2DMatrixNdarray(self.np_in_array,self.np_out_array,self.r,self.c)
    def test_transpose2DMatrixNdarrayNative(self):
        TP =  self.np_in_array.T
        return TP
    def test_transpose2DforLoop(self):
        for i in range(len(self.theList)):
            for j in range(len(self.theList[0])):
                self.outList[j][i] = self.theList[i][j]
        return 


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print "usage: test_ctypes <row> <col>"
        exit(1)
    else:
        r = int(sys.argv[1])
        c = int(sys.argv[2])
        num =10000 
        rep = 3
        import timeit
        tm = test_matrix(r,c)
        t = timeit.Timer(tm.test_transpose2DMatrixPyArr).repeat(rep,num)
        print "test 1 - c transpose with ctypes and standard list: \n {} loops, best of {}: {} usec per loop ".format(num,rep,(min(t)/num)*1000000)
        t = timeit.Timer(tm.test_transpose2DMatrixIncCtypeConv).repeat(rep,num)
        print "test 1.5 - c transpose with ctypes and standard list include ctype array conversion: \n {} loops, best of {}: {} usec per loop ".format(num,rep,(min(t)/num)*1000000)
        t = timeit.Timer(tm.test_transpose2DwithZip).repeat(rep,num)
        t = timeit.Timer(tm.test_transpose2DwithZip).repeat(rep,num)
        print "test 2 - zip(*list) transpose: \n {} loops, best of {}: {} usec per loop ".format(num,rep,(min(t)/num)*1000000)
        t = timeit.Timer(tm.test_transpose2DlistComp).repeat(rep,num)
        print "test 3 - list comprehension transpose: \n {} loops, best of {}: {} usec per loop ".format(num,rep,(min(t)/num)*1000000)
        t = timeit.Timer(tm.test_transpose2DMatrixNdarrayCtype).repeat(rep,num)
        print "test 4 - c transpose with np array native ctypes api: \n {} loops, best of {}: {} usec per loop ".format(num,rep,(min(t)/num)*1000000)
        t = timeit.Timer(tm.test_transpose2DforLoop).repeat(rep,num)
        print "test 5 - transpose with nested for loop: \n {} loops, best of {}: {} usec per loop ".format(num,rep,(min(t)/num)*1000000)
        t = timeit.Timer(tm.test_transpose2DMatrixNdarrayNative).repeat(rep,num)
        print "test 6 - transpose with numpy.transpose builtin: \n {} loops, best of {}: {} usec per loop ".format(num,rep,(min(t)/num)*1000000)





    
