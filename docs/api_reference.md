# API Reference

## Regexable Class

### Methods

- **`start_of_line()`**: Appends the start-of-line anchor `^` to the pattern.
- **`end_of_line()`**: Appends the end-of-line anchor `$` to the pattern.
- **`then(text)`**: Appends the given text to the pattern, escaping any special characters.
- **`maybe(text)`**: Appends an optional occurrence of the given text to the pattern.
- **`anything()`**: Appends a wildcard pattern that matches any character zero or more times (`.*`).
- **`anything_but(text)`**: Appends a pattern that matches any character except the specified text one or more times.
- **`something()`**: Appends a wildcard pattern that matches any character one or more times (`.+`).
- **`something_but(text)`**: Appends a pattern that matches any character except the specified text one or more times.
- **`digit()`**: Appends a pattern that matches any digit (`\d`).
- **`whitespace()`**: Appends a pattern that matches any whitespace character (`\s`).
- **`tab()`**: Appends a pattern that matches a tab character (`\t`).
- **`newline()`**: Appends a pattern that matches a newline character (`\n`).
- **`word()`**: Appends a pattern that matches any word character (`\w`).
- **`ignore_case()`**: Appends a flag to the pattern to ignore case sensitivity (`(?i)`).
- **`multiline()`**: Appends a flag to the pattern to treat the target as multiline (`(?m)`).
- **`word_boundary()`**: Appends a pattern that matches a word boundary (`\b`).
- **`not_word_boundary()`**: Appends a pattern that matches a non-word boundary (`\B`).
- **`zero_or_more()`**: Appends a quantifier that matches the preceding element zero or more times (`*`).
- **`one_or_more()`**: Appends a quantifier that matches the preceding element one or more times (`+`).
- **`exactly(n)`**: Appends a quantifier that matches the preceding element exactly `n` times (`{n}`).
- **`at_least(n)`**: Appends a quantifier that matches the preceding element at least `n` times (`{n,}`).
- **`between(m, n)`**: Appends a quantifier that matches the preceding element between `m` and `n` times (`{m,n}`).
- **`group(pattern)`**: Appends a group pattern to the current pattern.
- **`or_(pattern)`**: Appends an alternative pattern (OR) to the current pattern.
- **`range(char1, char2)`**: Appends a character range pattern to the current pattern.
- **`build()`**: Compiles the current pattern into a regular expression object.
- **`match(text)`**: Attempts to match the compiled pattern against the given text.

Each method returns an instance of `Regexable`, allowing method chaining.

## Examples

See [Examples](examples.md) for more detailed examples.
