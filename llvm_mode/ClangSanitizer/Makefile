CXX=clang
CXXFLAGS=-O2 -fPIC
DEPS= 
# cmpcovterm.c  cmpcovredis.c
SRCS=cmpcovshm.c
OBJS=$(subst .c,.o,$(SRCS))
LIBA=libcmpcov.a

.PRECIOUS: $(LIBA)
all: $(LIBA)

# %.o: %.c %.h
$(OBJS): $(SRCS)
	$(CXX) -c -o $@ $< $(CXXFLAGS)

$(LIBA): $(OBJS)
	ar cr $@ $(OBJS)

.PHONY: clean
clean:
	rm -f $(LIBA) $(OBJS)
