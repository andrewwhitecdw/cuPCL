import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parent.parent
MAKEFILE = REPO_ROOT / 'cuCluster' / 'Makefile'


class TestCuClusterMakefile(unittest.TestCase):
    def test_ldflags_used_in_target_link_rule(self):
        self.assertTrue(MAKEFILE.exists(), f'Makefile not found at {MAKEFILE}')
        text = MAKEFILE.read_text()

        # LDFLAGS must be defined somewhere in the Makefile
        self.assertIn(
            'LDFLAGS',
            text,
            'LDFLAGS should be defined in the Makefile',
        )

        # The final link recipe for $(TARGET) must reference $(LDFLAGS)
        in_target_rule = False
        for line in text.splitlines():
            if line.startswith('$(TARGET):'):
                in_target_rule = True
                continue
            if in_target_rule:
                if not line.startswith('\t'):
                    break
                if '$(CC)' in line and '$^' in line:
                    self.assertIn(
                        '$(LDFLAGS)',
                        line,
                        'Target link rule must include $(LDFLAGS)',
                    )
                    return
        self.fail('Could not find $(TARGET) link recipe with $(LDFLAGS)')


if __name__ == '__main__':
    unittest.main()
