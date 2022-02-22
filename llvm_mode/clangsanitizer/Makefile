CXX=clang++
CXXFLAGS=-O2 -fPIC
DEPS=common.h tracking.h 
SRCS=common.cc tracking.cc cmpcov.cc 
OBJS=$(subst .cc,.o,$(SRCS))
LIBA=libcmpcov.a

.PRECIOUS: $(LIBA)
all: $(LIBA)

%.o: %.cc %.h
	$(CXX) -c -o $@ $< $(CXXFLAGS)

$(LIBA): $(OBJS)
	ar cr $@ $(OBJS)
	# rm -f $(OBJS)

.PHONY: clean
clean:
	rm -f $(LIBA) $(OBJS)
