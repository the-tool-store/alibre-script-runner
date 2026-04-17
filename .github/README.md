# Alibre Script Runner

> Note: This repository is undergoing significant changes and is currently a work in progress.

| Item | Value |
| --- | --- |
| Type | Script collection / prototype repository |
| Primary stack | Python, Alibre automation |

## Overview
This repository contains Alibre-oriented Python scripts, prototypes, and supporting assets organized under the standardized repository layout.

## Repository Layout
- source/: project source, solution or project files, and runtime assets.
- submodules/: external git submodules used by the repository when required.
- documentation/: supplementary notes, changelogs, and non-GitHub documentation.
- .github/: repository README, templates, and GitHub-specific community files.
- `source/main.py`: key source or build entry point.
- `source/main_ex1.py`: key source or build entry point.
- `source/main_ex2.py`: key source or build entry point.
- `source/main_ex3.py`: key source or build entry point.
- `source/prototypes/Equation-Editor-Function-Calling.py`: key source or build entry point.
- `LICENSE`: repository license file kept at the root.

## Requirements
- Windows development environment.
- Python installed if you need to run or modify the Python components under source/.
- Alibre Design installed if you need to run, debug, or validate the Alibre integration.

## Build and Use
1. Review the entry points under source/.
2. Configure the required Python and Alibre environment.
3. Run `source/main.py` or the script that matches your workflow.
3. Use the notes in documentation/ and .github/README.md as the primary repository guide.

## Current Limitations
- The repository has been normalized for layout consistency; any path-sensitive tooling should be revalidated against the new folder structure.
- Existing runtime behavior and project-specific limitations remain unchanged.

## License
See [LICENSE](../LICENSE).

