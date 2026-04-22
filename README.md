# AI-Assisted Embedded C Documentation Generator

A Python CLI tool that parses embedded C source files and automatically generates
structured Markdown documentation from block comments above functions.

Built with GitHub Copilot assistance as part of exploring AI tooling for
embedded software development workflows.

## Usage

```bash
python doc_generator.py <your_c_file.c>
```

## Example

```bash
python doc_generator.py sensor_driver.c
# Generates: sensor_driver.md
```

## Output includes
- Function index table (name, return type, parameters)
- Detailed per-function descriptions

## Tech Stack
- Python 3.10+ (no external dependencies)
- GitHub Copilot used during development
- Tested on embedded C firmware files (Arduino/ATmega, 8051)
