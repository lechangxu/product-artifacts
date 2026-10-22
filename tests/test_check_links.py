import os
import sys
import tempfile
import unittest

sys.path.insert(
    0,
    os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "scripts"),
)
import check_links


def write(root, name, text):
    path = os.path.join(root, name)
    parent = os.path.dirname(path)
    if parent and not os.path.isdir(parent):
        os.makedirs(parent)
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(text)


class CheckLinksTest(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.root = self._tmp.name

    def tearDown(self):
        self._tmp.cleanup()

    def test_all_links_good(self):
        write(self.root, "ok.md", "# ok\n")
        write(self.root, "a.md", "# a\n\n[x](ok.md)\n[y](ok.md#frag)\n")
        self.assertEqual(check_links.scan([self.root]), (2, []))

    def test_missing_relative_file_reported(self):
        write(self.root, "a.md", "# a\n\n[bad](missing.md)\n")
        self.assertEqual(check_links.scan([self.root]), (1, ["a.md:3 -> missing.md"]))

    def test_external_links_ignored(self):
        write(
            self.root,
            "a.md",
            "# a\n\n[h](http://x)\n[s](https://x)\n[m](mailto:a@b)\n[p](#top)\n",
        )
        self.assertEqual(check_links.scan([self.root]), (0, []))

    def test_multiple_files_scanned(self):
        write(self.root, "a.md", "# a\n\n[x](a.md)\n")
        write(self.root, "b.md", "# b\n\n[y](b.md)\n")
        self.assertEqual(check_links.scan([self.root]), (2, []))

    def test_broken_line_format(self):
        write(self.root, "sub/deep.md", "# d\n\n[b](gone.md)\n")
        self.assertEqual(check_links.scan([self.root]), (1, ["sub/deep.md:3 -> gone.md"]))


if __name__ == "__main__":
    unittest.main()
