CC=g++
CCFLAGS=-Wno-deprecated -Wall -W -Wextra -fPIC -DMACOSX -arch x86_64 -O3
CCINC=-I../../libdai/include # -I/opt/local/include
CCLIB=-L../../libdai/lib # -L/opt/local/lib

# LINKER
# Standard libraries to include
LIBS=-ldai -lgmpxx -lgmp -arch x86_64
# For linking with BOOST libraries
BOOSTLIBS_PO=-lboost_program_options
BOOSTLIBS_UTF=-lboost_unit_test_framework
# Additional library search paths for linker

all:
	$(CC) $(CCINC) $(CCFLAGS) $(CCLIB) -o mit_gm mit_gm.cpp $(LIBS)

# g++ -Iinclude -I/opt/local/include -Wno-deprecated -Wall -W -Wextra -fPIC -DMACOSX -arch x86_64 -O3 -g -DDAI_DEBUG  -Llib -L/opt/local/lib -o examples/example_sprinkler_gibbs examples/example_sprinkler_gi bbs.cpp -ldai -lgmpxx -lgmp -arch x86_64
