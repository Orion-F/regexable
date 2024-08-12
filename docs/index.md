# Regexable Documentation

Welcome to the official documentation for [**Regexable**](https://github.com/Orion-F/regexable) - a Python package designed to simplify the creation and management of regular expressions. Regexable provides an intuitive, readable, and chainable interface that makes working with regex easier for both beginners and experienced developers.

## Features

- **Chainable Methods**: Construct regex patterns step by step using a clean, chainable syntax.
- **Anchors and Boundaries**: Easily add start-of-line, end-of-line, word boundary, and other anchors to your patterns.
- **Text Matching**: Add specific text or optional text segments, and define characters to match or exclude.
- **Quantifiers**: Specify how many times a character or group should be matched (e.g., zero or more, one or more, exactly n times).
- **Modifiers**: Apply flags for case-insensitive or multiline matching.
- **Grouping and Alternation**: Group patterns together or create alternatives using the `group` and `or_` methods.
- **Utilities**: Match, search, and compile patterns into regex objects.

## Quick Start

Here’s a quick example to get you started with Regexable:

```python
from regexable import Regexable

# Construct a regex pattern
pattern = Regexable()\
    .start_of_line()\
    .then("Hello")\
    .whitespace()\
    .one_or_more()\
    .then("World")\
    .end_of_line()\
    .build()

# Match a string
match = pattern.match("Hello World")
print(match)  # Output: <re.Match object; span=(0, 11), match='Hello World'>

# Check if a string matches the pattern
if pattern.match("Hello World"):
    print("Match found!")
```

## Installation

Install Regexable via pip:

```sh
pip install regexable
```

## Contributing

We welcome contributions! If you find a bug or have a feature request, please create an issue on our [GitHub repository](https://github.com/Orion-F/regexable).

## License

Regexable is licensed under the MIT License.
