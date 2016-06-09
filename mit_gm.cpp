#include <iostream>
#include <chrono>
#include <dai/alldai.h>

using namespace std;
using namespace dai;

// def y_id(i, j, n_obj, n_loc):
//     return n_obj + (i * n_loc) + j

int main(int argc, char *argv[]) {
    FactorGraph fg;
    fg.ReadFromFile(argv[1]);
    int n_obj = atoi(argv[2]);
    int n_loc = atoi(argv[3]);

    PropertySet opts;

    JTree jt(fg, opts("updates",string("HUGIN")));

    // Set some evidence
//     jt.clamp(2, 1);
//     jt.clamp(2, 1);

    auto t1 = chrono::high_resolution_clock::now();
    jt.init();
    jt.run();
    auto t2 = chrono::high_resolution_clock::now();
    int t = chrono::duration_cast<chrono::milliseconds>(t2-t1).count();
    cout << n_obj << " " << n_loc << " " << t << endl;

//     for (size_t i = 0; i < fg.nrVars(); i++) {
//         cout << jt.belief(fg.var(i));
//     }

}

