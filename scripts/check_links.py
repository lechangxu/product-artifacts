#!/usr/bin/env python3
"""Check relative links in Markdown files.

Usage: check_links.py [PATH ...] -- each PATH is a file (checked alone) or a
directory (recursive *.md); no argument means this script's repository. Links
resolve against their own Markdown file's directory, never the scan root.
http(s), mailto and #anchor targets are ignored. Broken links print
"path:line -> target" and exit 1; else "OK <n> links checked" and exit 0.
"""
import os
import re
import sys

LINK_RE = re.compile(r"\[[^\]]*\]\(([^)\s]+)\)")
SKIP_PREFIX = ("http://", "https://", "mailto:", "#")


def md_files(target):
    if os.path.isfile(target):
        return [target]
    found = []
    for root, dirs, files in os.walk(target):
        dirs[:] = sorted(d for d in dirs if d != ".git")
        found += [os.path.join(root, n) for n in sorted(files) if n.endswith(".md")]
    return found


def scan(paths):
    """Return (checked, broken) for the given file/directory paths."""
    checked, broken = 0, []
    for path in paths:
        path = os.path.abspath(path)
        single = os.path.isfile(path)
        root = os.path.dirname(path) if single else path
        for md in md_files(path):
            label = os.path.basename(md) if single else os.path.relpath(md, root)
            with open(md, encoding="utf-8") as fh:
                for lineno, line in enumerate(fh, 1):
                    for target in LINK_RE.findall(line):
                        if target.startswith(SKIP_PREFIX):
                            continue
                        rel = target.split("#", 1)[0]
                        checked += 1
                        if not os.path.exists(os.path.join(os.path.dirname(md), rel)):
                            broken.append("%s:%d -> %s" % (label, lineno, target))
    return checked, broken


def main(argv):
    paths = argv or [os.path.dirname(os.path.dirname(os.path.abspath(__file__)))]
    checked, broken = scan(paths)
    if broken:
        print("\n".join(broken))
        return 1
    print("OK %d links checked" % checked)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
