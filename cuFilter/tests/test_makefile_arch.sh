#!/bin/bash
set -euo pipefail

MAKEFILE=${0%/*}/../Makefile

# PCL/Boost library path must be architecture-agnostic, not hard-coded to aarch64.
grep -q 'PCL_LIB_DIR := /usr/lib/' $MAKEFILE
if grep -q '/usr/lib/aarch64-linux-gnu/' $MAKEFILE; then
    echo 'ERROR: Makefile hardcodes aarch64 library path' >&2
    exit 1
fi
