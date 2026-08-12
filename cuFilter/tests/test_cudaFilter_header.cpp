// Compile-only regression test for missing <iostream>/<cstdlib> includes.
// Including the public header by itself must expand checkCudaErrors without
// compile errors. The error-reporting branch aborts at runtime, so this test
// should be compiled but not executed.
#include "cudaFilter.h"

int main() {
    checkCudaErrors(1);  // exercise the error-reporting branch
}
