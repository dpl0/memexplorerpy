# Macros:
CPP= g++
CFLAGS= -O3 -fopenmp
OBJECTS= SampleDecoder.o

# Targets:
all: samplecode

samplecode: $(OBJECTS)
	$(CPP) $(CFLAGS) $(OBJECTS) -o samplecode
        
SampleDecoder.o:
	$(CPP) $(CFLAGS) -c SampleDecoder.cpp

# Remove:
clean:
	rm -f sampledecode $(OBJECTS)
