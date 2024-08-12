# Examples

## Basic Example

Here's a simple example demonstrating how to use Regexable to create and match a regex pattern:

```python
from regexable import Regexable

pattern = Regexable()\
    .start_of_line()\
    .then("Hello")\
    .whitespace()\
    .then("World")\
    .end_of_line()\
    .build()

text = "Hello World"
match = pattern.match(text)

if match:
    print(f"Matched: {match.group(0)}")  # Output: Matched: Hello World
else:
    print("No match found")
```

## Common Patterns

### Matching an Email Address

```python
email_pattern = Regexable()\
    .start_of_line()\
    .word()\
    .then("@")\
    .word()\
    .then(".")\
    .word()\
    .end_of_line()\
    .build()

email = "example@example.com"
match = email_pattern.match(email)

if match:
    print(f"Valid email: {match.group(0)}")
else:
    print("Invalid email")

```

This is much more readable and intuitive compared to writing the equivalent regex pattern directly:

```python
import re

email_pattern = r"^\w+@\w+\.\w+$"
email = "

match = re.match(email_pattern, email)

if match:
    print(f"Valid email: {match.group(0)}")
else:
    print("Invalid email")
```

### Matching a Phone Number

```python
phone_pattern = Regexable()\
    .start_of_line()\
    .digit().exactly(3)\
    .then("-")\
    .digit().exactly(3)\
    .then("-")\
    .digit().exactly(4)\
    .end_of_line()\
    .build()

phone = "123-456-7890"
match = phone_pattern.match(phone)

if match:
    print(f"Valid phone number: {match.group(0)}")
else:
    print("Invalid phone number")
```

## Using Modifiers

### Case Insensitive Matching

```python
case_insensitive_pattern = Regexable()\
    .ignore_case()\
    .then("hello")\
    .build()

text = "Hello"
match = case_insensitive_pattern.match(text)

if match:
    print("Case insensitive match found!")
```

### Multiline Matching

```python
multiline_pattern = Regexable()\
    .multiline()\
    .start_of_line()\
    .then("Start")\
    .build()

text = "Start\nAnother line"
matches = multiline_pattern.search(text)

if matches:
    print("Multiline match found!")
```

Explore more advanced usage in the [API Reference](api_reference.md).
