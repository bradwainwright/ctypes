CC = gcc
COPT = -Wall -Wextra -pedantic-errors -std=c99 -fpic
SOFLAG = -shared
OPTIMISE = 
TARGET = bin/_trans.so
OBJS = bin/transpose.o
SRC = src/transpose.c

all:	o1 
	$(CC) $(SOFLAG) -o $(TARGET) $(OBJS)

o1:    $(SRC)
	$(CC) -c $(SRC) $(COPT) -o $(OBJS)
clean: 
	rm -rf $(OBJS) && rm -rf $(TARGET) && rm -rf src/*.pyc 

