CFLAGS=-Wall

.PHONY: all clean cleanall

all: main

main: main.cpp
	g++ $(CFLAGS) -o main main.cpp

clean:
	rm -f main

cleanall:
	rm -f main
