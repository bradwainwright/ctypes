# ctypes - comparison of matrix transpose, native python list, numpy, numpy with embedded ctypes and cyptes

# Linux example.. havent tried other OS 
# First compile shared object .. ctypes seems to only work with .so
make all
# gcc command should look like this 
gcc -c src/transpose.c -Wall -Wextra -pedantic-errors -std=c99 -fpic -o bin/transpose.o
gcc -shared -o bin/_trans.so bin/transpose.o
# run the test python script which uses timeit on test_ctypes.py 
python src/test_ctypes.py 5 10
 shared object file is <your path>bin/_trans.so

test 1 - c transpose with ctypes and standard list: 
 10000 loops, best of 3: 1.56049728394 usec per loop 
test 1.5 - c transpose with ctypes and standard list include ctype array conversion: 
 10000 loops, best of 3: 32.4353933334 usec per loop 
test 2 - zip(*list) transpose: 
 10000 loops, best of 3: 1.23710632324 usec per loop 
test 3 - list comprehension transpose: 
 10000 loops, best of 3: 11.0550165176 usec per loop 
test 4 - c transpose with np array native ctypes api: 
 10000 loops, best of 3: 11.899805069 usec per loop 
test 5 - transpose with nested for loop: 
 10000 loops, best of 3: 11.2527132034 usec per loop 
test 6 - transpose with numpy.transpose builtin: 
 10000 loops, best of 3: 0.394606590271 usec per loop 

