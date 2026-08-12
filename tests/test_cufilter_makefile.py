#!/usr/bin/env python3
"""Regression test that cuFilter/Makefile passes LDFLAGS when linking."""

import os
import re


def test_link_rule_uses_ldflags():
    test_dir = os.path.dirname(os.path.abspath(__file__))
    makefile = os.path.join(test_dir, '..', 'cuFilter', 'Makefile')
    assert os.path.exists(makefile), f"Makefile not found: {makefile}"

    with open(makefile) as f:
        content = f.read()

    # Find the $(TARGET) explicit rule and its indented recipe lines.
    match = re.search(r'^\$\(TARGET\):[^\n]*\n((?:\t[^\n]*\n)+)', content, re.MULTILINE)
    assert match, "Could not find $(TARGET) link rule"

    recipe = match.group(1)
    assert '$(LDFLAGS)' in recipe, \
        "cuFilter/Makefile $(TARGET) link recipe does not reference $(LDFLAGS)"


if __name__ == '__main__':
    test_link_rule_uses_ldflags()
