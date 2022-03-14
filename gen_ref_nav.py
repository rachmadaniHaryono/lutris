#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Generate the code reference pages and navigation."""

from pathlib import Path

import mkdocs_gen_files

nav = mkdocs_gen_files.Nav()

for path in sorted(Path("lutris").glob("**/*.py")):
    module_path = path.with_suffix("")
    doc_path = path.with_suffix(".md")
    full_doc_path = Path("reference", doc_path)

    parts = list(module_path.parts)
    if parts[-1] in ("__init__" ,"__main__"):
        continue
    nav_parts = list(parts)
    nav[nav_parts] = doc_path

    with mkdocs_gen_files.open(full_doc_path, "w") as fd:
        ident = ".".join(parts)
        print("::: " + ident, file=fd)

    mkdocs_gen_files.set_edit_path(full_doc_path, path)

with mkdocs_gen_files.open("reference/SUMMARY.md", "w") as nav_file:
    nav_file.writelines(nav.build_literate_nav())
