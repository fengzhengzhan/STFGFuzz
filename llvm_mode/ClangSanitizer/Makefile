CXX=clang++
CXXFLAGS=-O2 -fPIC
DEPS= 
# SRCS=cmpcov.cc
SRCS=cmpcovshm.cc
OBJS=$(subst .cc,.o,$(SRCS))
LIBA=libcmpcov.a

.PRECIOUS: $(LIBA)
all: $(LIBA)

%.o: %.cc %.h
	$(CXX) -c -o $@ $< $(CXXFLAGS)

$(LIBA): $(OBJS)
	ar cr $@ $(OBJS)

.PHONY: clean
clean:
	rm -f $(LIBA) $(OBJS)
