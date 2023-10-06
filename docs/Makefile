# SPDX-FileCopyrightText: 2019 Veit Schiele
#
# SPDX-License-Identifier: BSD-3-Clause

# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line, and also
# from the environment for the first two.
SPHINXOPTS    ?=
SPHINXBUILD   ?= sphinx-build
SOURCEDIR     = .
BUILDDIR      = _build
FILENAMES     = $(shell git diff --name-only --staged)
CLEAN_NAMES := $(foreach FILENAME,$(FILENAMES),$(shell echo $(FILENAME) | cut -c6-))

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: help Makefile

# check links only in staged files
diff_linkcheck:
	sphinx-build -b linkcheck -W $(SOURCEDIR) $(BUILDDIR) $(CLEAN_NAMES)

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
