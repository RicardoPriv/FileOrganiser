# Define variables
PYTHON := python3
SCRIPT := src/main.py

# Set the default goal to 'run'
.DEFAULT_GOAL := run

# Default target
.PHONY: run
run:
	@$(PYTHON) $(SCRIPT) $(ARGS)

# Usage instructions
.PHONY: help
help:
	@echo "Usage:"
	@echo "  make ARGS='/path/to/directory/to/organise yes'"
	@echo ""
	@echo "Make sure to enclose directory paths and yes/no in quotes."
	@echo "yes or no is for overwriting files within extensions folders that already exist with the same name"
	@echo "generally only neccessary if already run once before since subfolders are created when run"
	@echo "  eg: yes will have /directorySrc/exmpl.txt overwrite directorySrc/directoryDst/exmpl.txt if it exists"
