CXX=clang
CXXFLAGS=-O2 -fPIC
DEPS= 
SRCS=cmpcov.c
OBJS=$(subst .c,.o,$(SRCS))
LIBA=libcmpcov.a

.PRECIOUS: $(LIBA)
all: $(LIBA)

%.o: %.c %.h
	$(CXX) -c -o $@ $< $(CXXFLAGS)

$(LIBA): $(OBJS)
	ar cr $@ $(OBJS)

.PHONY: clean
clean:
	rm -f $(LIBA) $(OBJS)
