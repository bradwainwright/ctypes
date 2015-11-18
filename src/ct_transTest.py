import ctypes as ct
import numpy as np
import os

def get_so_path(soFile):
    for root,dirs,files in os.walk('.'):
        for file in files:
            if file in soFile:
                soPath = os.path.abspath(os.path.join(root,file))
                return soPath

soFile  = '_trans.so'
if get_so_path(soFile) is None:
    print " couldn't find {} ".format(soFile)
    exit(1)
else:
    print " shared object file is {}".format(get_so_path(soFile))


""" load *.so binary"""
_trans_lib = ct.cdll.LoadLibrary(get_so_path(soFile))


def make2Darray(r,c,zeros=False):
    """
    convenience function .. create 2d array
    """
    if zeros:
        return [[ 0 for j in range(c)] for i in range(r)]
    else:
        return [[i*c+j for j in range(c)] for i in range(r)]
def make2dNpArray(r,c,zeros=False):
    """
    create a numpy 2 array
    """
    if zeros:
        x = np.arange(r*c,dtype=np.double).reshape(r,c)
        x.fill(0)
        return x
    else:
        return np.arange(r*c,dtype=np.double).reshape(r,c)
def convert2DtoCtypeArray(in_array,r,c):
    """
    take a list and convert to ctype pyArr
    fill with accumulative ints 
    """
    if (r*c != len(in_array)) and (type(in_array[0]) != list):
        raise ValueError('row and col is not == to len(in_array)')
    else:
        ctArr = (ct.c_double * c * r)()
        for i in range(r):
            for j in range(c):
                ctArr[i][j] = in_array[i][j]
    return ctArr

def printMatrix(np_arr,r,c):
    """
    this expects a numpy array
    """
    return _trans_lib.printArray(np_arr.ctypes.data_as(ct.c_void_p),r,c)
def transpose2DMatrixNdarray(in_nparray,out_nparray,r,c):
    """"
    this expects two numpy arrays

    """
    return  _trans_lib.transpose(in_nparray.ctypes.data_as(ct.c_void_p),out_nparray.ctypes.data_as(ct.c_void_p),r,c)
def transpose2DMatrixPyArr(in_array,out_array,r,c):
    """
    expects a ctype array and passes to c code 
    passes to c prototype:
     void transpose(const double  *input,double * output, int w, int l) 

    """
    if (r != len(in_array)) and (c !=len(in_array[0])):
        raise ValueError('row and col is not == to len(in_array)')
    else:
       return _trans_lib.transpose(in_array,out_array,r,c)
def transpase2DlistComp(in_array):
    return [ [in_array[j][i] for j in range(len(in_array))] for i in range(len(in_array[0]))]





