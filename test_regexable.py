# test_regexable.py - Unit tests for the Regexable class.

import unittest
from regexable.core import Regexable

class TestRegexable(unittest.TestCase):
    
    def test_start_of_line(self):
        # Test that the pattern correctly matches at the start of the line.
        regex = Regexable().start_of_line().then("start").build()
        self.assertTrue(regex.match("start"))  # Should match because the string starts with "start".
        self.assertFalse(regex.match(" middle"))  # Should not match because "start" is not at the beginning.

    def test_end_of_line(self):
        # Test that the pattern correctly matches at the end of the line.
        regex = Regexable().then("end").end_of_line().build()
        self.assertTrue(regex.match("end"))  # Should match because the string ends with "end".
        self.assertFalse(regex.match("end "))  # Should not match because "end" is not at the end.

    def test_then(self):
        # Test that the pattern correctly appends text to the pattern.
        regex = Regexable().then("text").build()
        self.assertTrue(regex.match("text"))  # Should match exactly "text".
        self.assertFalse(regex.match("nottext"))  # Should not match because the string doesn't start with "text".

    def test_maybe(self):
        # Test that the pattern optionally matches the given text.
        regex = Regexable().maybe("maybe").build()
        self.assertTrue(regex.match("maybe"))  # Should match "maybe".
        self.assertTrue(regex.match(""))  # Should also match an empty string because "maybe" is optional.

    def test_anything(self):
        # Test that the pattern matches any sequence of characters.
        regex = Regexable().anything().build()
        self.assertTrue(regex.match("anything at all"))  # Should match any string.

    def test_anything_but(self):
        # Test that the pattern matches anything except the specified text.
        regex = Regexable().anything_but("x").build()
        self.assertTrue(regex.match("anything but x"))  # Should match because "x" is not present.
        self.assertFalse(regex.match("xxxx"))  # Should not match because the string only contains "x".

    def test_something(self):
        # Test that the pattern matches any non-empty sequence of characters.
        regex = Regexable().something().build()
        self.assertTrue(regex.match("something"))  # Should match any non-empty string.
        self.assertFalse(regex.match(""))  # Should not match an empty string.

    def test_something_but(self):
        # Test that the pattern matches any non-empty sequence except the specified text.
        regex = Regexable().something_but("x").build()
        self.assertTrue(regex.match("something but x"))  # Should match because it doesn't consist only of "x".
        self.assertFalse(regex.match("xxxx"))  # Should not match because the string only contains "x".

    def test_digit(self):
        # Test that the pattern matches any digit.
        regex = Regexable().digit().build()
        self.assertTrue(regex.match("1"))  # Should match any digit.
        self.assertFalse(regex.match("a"))  # Should not match a non-digit character.

    def test_whitespace(self):
        # Test that the pattern matches any whitespace character.
        regex = Regexable().whitespace().build()
        self.assertTrue(regex.match(" "))  # Should match a space.
        self.assertFalse(regex.match("a"))  # Should not match a non-whitespace character.

    def test_tab(self):
        # Test that the pattern matches a tab character.
        regex = Regexable().tab().build()
        self.assertTrue(regex.match("\t"))  # Should match a tab character.
        self.assertFalse(regex.match(" "))  # Should not match a space instead of a tab.

    def test_newline(self):
        # Test that the pattern matches a newline character.
        regex = Regexable().newline().build()
        self.assertTrue(regex.match("\n"))  # Should match a newline character.
        self.assertFalse(regex.match(" "))  # Should not match a space instead of a newline.

    def test_word(self):
        # Test that the pattern matches any word character (letters, digits, and underscores).
        regex = Regexable().word().build()
        self.assertTrue(regex.match("a"))  # Should match a single word character.
        self.assertFalse(regex.match(" "))  # Should not match a non-word character.

    def test_ignore_case(self):
        # Test that the pattern matches regardless of case sensitivity.
        regex = Regexable().ignore_case().then("text").build()
        self.assertTrue(regex.match("TEXT"))  # Should match "TEXT" in a case-insensitive manner.
        self.assertFalse(regex.match("nottext"))  # Should not match a string that doesn't contain "text".

    def test_multiline(self):
        # Test that the pattern matches across multiple lines.
        regex = Regexable().multiline().then("text").build()
        self.assertTrue(regex.match("text\ntext"))  # Should match across lines with the multiline flag.
        self.assertFalse(regex.match("nottext"))  # Should not match because it doesn't start with "text".

    def test_word_boundary(self):
        # Test that the pattern matches a word boundary.
        regex = Regexable().word_boundary().then("word").word_boundary().build()
        self.assertTrue(regex.search(" word "))  # Should match "word" with boundaries on both sides.
        self.assertTrue(regex.search("word!"))  # Should match "word" with a boundary before it.
        self.assertFalse(regex.search("sword"))  # Should not match "sword" because "word" isn't at a boundary.
        self.assertFalse(regex.search("words"))  # Should not match "words" because "word" isn't at a boundary.

    def test_not_word_boundary(self):
        # Test that the pattern does not match at a word boundary.
        regex = Regexable().not_word_boundary().then("word").build()
        self.assertTrue(regex.search("password"))  # Should match "word" within "password" as it's not a boundary.
        self.assertTrue(regex.search("sword"))  # Should match "word" within "sword".
        self.assertFalse(regex.search("wordsmith"))  # Should not match "word" in "wordsmith" due to the boundary.

    def test_zero_or_more(self):
        # Test that the pattern matches zero or more occurrences of the preceding element.
        regex = Regexable().then("a").zero_or_more().build()
        self.assertTrue(regex.match("aaa"))  # Should match one or more "a".
        self.assertTrue(regex.match(""))  # Should match zero occurrences.

    def test_one_or_more(self):
        # Test that the pattern matches one or more occurrences of the preceding element.
        regex = Regexable().then("a").one_or_more().build()
        self.assertTrue(regex.match("aaa"))  # Should match one or more "a".
        self.assertFalse(regex.match(""))  # Should not match zero occurrences.

    def test_exactly(self):
        # Test that the pattern matches exactly a specified number of occurrences.
        regex = Regexable().then("a").exactly(3).build()
        self.assertTrue(regex.match("aaa"))  # Should match exactly three "a".
        self.assertFalse(regex.match("aa"))  # Should not match fewer than three "a".

    def test_at_least(self):
        # Test that the pattern matches at least a specified number of occurrences.
        regex = Regexable().then("a").at_least(3).build()
        self.assertTrue(regex.match("aaaa"))  # Should match three or more "a".
        self.assertFalse(regex.match("aa"))  # Should not match fewer than three "a".

    def test_between(self):
        # Test that the pattern matches between a specified range of occurrences.
        regex = Regexable().then("a").between(2, 4).build()
        self.assertTrue(regex.match("aaa"))  # Should match between two and four "a".
        self.assertFalse(regex.match("a"))  # Should not match fewer than two "a".

    def test_group(self):
        # Test that the pattern correctly groups a sub-pattern.
        regex = Regexable().group("abc").build()
        self.assertTrue(regex.match("abc"))  # Should match the exact group "abc".
        self.assertFalse(regex.match("ab"))  # Should not match if the entire group is not matched.

    def test_or(self):
        # Test that the pattern matches one of two alternatives.
        regex = Regexable().then("a").or_("b").build()
        self.assertTrue(regex.match("a"))  # Should match "a".
        self.assertTrue(regex.match("b"))  # Should match "b".
        self.assertFalse(regex.match("c"))  # Should not match anything other than "a" or "b".

    def test_range(self):
        # Test that the pattern matches a character within a specified range.
        regex = Regexable().range("a", "c").build()
        self.assertTrue(regex.match("a"))  # Should match "a".
        self.assertTrue(regex.match("b"))  # Should match "b".
        self.assertTrue(regex.match("c"))  # Should match "c".
        self.assertFalse(regex.match("d"))  # Should not match a character outside the range.
        
if __name__ == '__main__':
    unittest.main()
