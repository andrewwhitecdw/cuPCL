#!/bin/bash
set -e

cd "$(dirname "$0")/.."

# Fail if the aarch64 library path is hard-coded on a single LIBRARIES line.
if grep -E '^LIBRARIES[[:space:]]*\+=[[:space:]]*-L/usr/lib/aarch64-linux-gnu/.*lboost_system' Makefile >/dev/null; then
    echo "ERROR: aarch64 library path is hard-coded unconditionally"
    exit 1
fi

# Verify the path is guarded by an aarch64 conditional.
if ! grep -B2 -A1 -E 'LIBRARIES[[:space:]]*\+=[[:space:]]*-L/usr/lib/aarch64-linux-gnu/' Makefile | grep -q 'ifeq ($(TARGET_ARCH), aarch64)'; then
    echo "ERROR: aarch64 library path is not guarded by TARGET_ARCH conditional"
    exit 1
