# Built-in Functions & String Methods Reference Guide

#### I. Built-in Functions (Universal Tools)
Functions are standalone tools. Data is passed into their parentheses as parameters.

-   `input()`:
    *   **Purpose:** To receive dynamic text input from the user via the console.
    *   **Accepted Data Types:** String (used as the prompt message). If numbers are provided, Python automatically casts them to text.
    *   **Mandatory/Optional:** Optional.
    *   **Return Type:** String.
    *   **Examples:** `name = input("Enter your name: ")` (+ve) | N/A (-ve)

-   `len()`:
    *   **Purpose:** To count the total number of items (size/length) within a collection.
    *   **Accepted Data Types:** Iterables/Collections only (Strings, Lists, Tuples, Dictionaries, Sets).
    *   **Mandatory/Optional:** Mandatory (Requires exactly 1 parameter).
    *   **Return Type:** Integer.
    *   **Examples:** `len("Python")` (+ve) | `len(5)` raises TypeError (-ve)

-   `print()`:
    *   **Purpose:** To display output results or text on the screen.
    *   **Accepted Data Types:** Any valid data type (Strings, Numbers, Lists, Booleans).
    *   **Mandatory/Optional:** Optional.
    *   **Return Type:** None.
    *   **Examples:** `print("Age:", 25)` (+ve) | `print(undeclared_var)` raises NameError (-ve)

-   `range()`:
    *   **Purpose:** To generate a sequence of numbers, primarily used for iteration in loops.
    *   **Accepted Data Types:** Strictly Integers (whole numbers).
    *   **Mandatory/Optional:** Minimum 1 parameter (stop value) is Mandatory.
    *   **Return Type:** Range Object (Sequence of integers).
    *   **Examples:** `range(5)` (+ve) | `range("5")` raises TypeError (-ve)

-   `enumerate()`:
    *   **Purpose:** To retrieve both the item and its corresponding index simultaneously during a loop.
    *   **Accepted Data Types:** 1st parameter: Iterable (String, List). 2nd parameter: Integer (start index).
    *   **Mandatory/Optional:** 1st parameter is Mandatory. 2nd parameter is Optional.
    *   **Return Type:** Enumerate Object (Iterator of index-item tuples).
    *   **Examples:** `list(enumerate("cat"))` (+ve) | `enumerate(123)` raises TypeError (-ve)

-   `sorted()`:
    *   **Purpose:** To return a new sorted list from the elements of any iterable (e.g., sorting a string's characters alphabetically).
    *   **Accepted Data Types:** Iterables (Strings, Lists, Tuples, Dictionaries, Sets).
    *   **Mandatory/Optional:** Mandatory (Requires exactly 1 iterable parameter).
    *   **Return Type:** List.
    *   **Examples:** `sorted("cba")` (+ve) | `sorted(5)` raises TypeError (-ve)

-   `max()`:
    *   **Purpose:** To find and return the largest item in an iterable, or the largest of two or more arguments. A `key` function can be provided to customize the sorting logic (e.g., `key=len` to find the longest string).
    *   **Accepted Data Types:** Iterables (Lists, Tuples, Strings, Sets) or multiple comma-separated values.
    *   **Mandatory/Optional:** Mandatory (Requires at least one non-empty iterable or two distinct arguments). The `key` parameter is Optional.
    *   **Return Type:** Any (Matches the data type of the largest element found).
    *   **Examples:** `max(["apple", "cat"], key=len)` (+ve) | `max([])` raises ValueError (-ve)

-   `set()`:
    *   **Purpose:** To create an unordered collection of unique elements. Automatically removes any duplicate items.
    *   **Accepted Data Types:** Iterables (Strings, Lists, Tuples).
    *   **Mandatory/Optional:** Optional (Providing an iterable converts it to a set; leaving it empty creates an empty set).
    *   **Return Type:** Set.
    *   **Examples:** `set("apple")` (+ve) | `set(123)` raises TypeError (-ve)

---

#### II. String-Specific Methods
Methods are behaviors attached to specific objects. They are called using the dot syntax directly on the target string.

-   `.upper()`:
    *   **Purpose:** To convert all characters in a string to uppercase.
    *   **Accepted Data Types:** Strictly Zero Parameters.
    *   **Mandatory/Optional:** Must remain empty `()`.
    *   **Return Type:** String.
    *   **Examples:** `"hello".upper()` (+ve) | `"hello".upper(1)` raises TypeError (-ve)

-   `.lower()`:
    *   **Purpose:** To convert all characters in a string to lowercase.
    *   **Accepted Data Types:** Strictly Zero Parameters.
    *   **Mandatory/Optional:** Must remain empty `()`.
    *   **Return Type:** String.
    *   **Examples:** `"HELLO".lower()` (+ve) | `"HELLO".lower("H")` raises TypeError (-ve)

-   `.casefold()`:
    *   **Purpose:** To handle Unicode characters for strict ignore-case comparisons (e.g., converting the German 'ß' to 'ss').
    *   **Accepted Data Types:** Strictly Zero Parameters.
    *   **Mandatory/Optional:** Must remain empty `()`.
    *   **Return Type:** String.
    *   **Examples:** `"ß".casefold()` (+ve) | `"ß".casefold(1)` raises TypeError (-ve)

-   `.isalpha()`:
    *   **Purpose:** Returns `True` if all characters are alphabetic.
    *   **Accepted Data Types:** Strictly Zero Parameters.
    *   **Mandatory/Optional:** Must remain empty `()`.
    *   **Return Type:** Boolean.
    *   **Examples:** `"abc".isalpha()` (+ve) | `"abc".isalpha(1)` raises TypeError (-ve)

-   `.isdigit()`:
    *   **Purpose:** Returns `True` if all characters are numeric digits.
    *   **Accepted Data Types:** Strictly Zero Parameters.
    *   **Mandatory/Optional:** Must remain empty `()`.
    *   **Return Type:** Boolean.
    *   **Examples:** `"123".isdigit()` (+ve) | `"123".isdigit(1)` raises TypeError (-ve)

-   `.isspace()`:
    *   **Purpose:** Returns `True` if all characters are whitespaces.
    *   **Accepted Data Types:** Strictly Zero Parameters.
    *   **Mandatory/Optional:** Must remain empty `()`.
    *   **Return Type:** Boolean.
    *   **Examples:** `"   ".isspace()` (+ve) | `"   ".isspace(1)` raises TypeError (-ve)

-   `.split()`:
    *   **Purpose:** To cut a string into multiple pieces based on a specified separator.
    *   **Accepted Data Types:** String (used as the delimiter).
    *   **Mandatory/Optional:** Optional (defaults to whitespaces if omitted).
    *   **Return Type:** List (containing Strings).
    *   **Examples:** `"a,b".split(",")` (+ve) | `"a b".split(2)` raises TypeError (-ve)

-   `.strip()`:
    *   **Purpose:** To remove unwanted characters from the beginning and end of a string.
    *   **Accepted Data Types:** String (exact characters to remove).
    *   **Mandatory/Optional:** Optional (defaults to whitespaces if omitted).
    *   **Return Type:** String.
    *   **Examples:** `" hello ".strip()` (+ve) | `"hello".strip(1)` raises TypeError (-ve)

-   `.join()`:
    *   **Purpose:** To glue a list of items together into a single string, using the caller string as the separator.
    *   **Accepted Data Types:** An Iterable (List, Tuple) containing only Strings.
    *   **Mandatory/Optional:** Mandatory (Requires exactly 1 parameter).
    *   **Return Type:** String.
    *   **Examples:** `"-".join(["A", "B"])` (+ve) | `"-".join([1, 2])` raises TypeError (-ve)

-   `.replace()`:
    *   **Purpose:** To replace occurrences of a specific sub-string or character within a string with a new string.
    *   **Accepted Data Types:** 1st parameter (old): String. 2nd parameter (new): String. 3rd parameter (count): Integer.
    *   **Mandatory/Optional:** 1st and 2nd parameters are Mandatory. 3rd parameter is Optional (replaces all occurrences if omitted).
    *   **Return Type:** String.
    *   **Examples:** `"Hello World".replace("World", "Python")` (+ve) | `"Hello".replace("H", 1)` raises TypeError (-ve)
    
-   `.count()`:
    *   **Purpose:** To count the exact number of times a specific character or sub-string appears within a string.
    *   **Accepted Data Types:** 1st parameter: String (the character or substring to search for). Optional start and end integer indices can also be specified.
    *   **Mandatory/Optional:** Mandatory (Requires at least the target character/substring parameter).
    *   **Return Type:** Integer.
    *   **Examples:** `"apple".count("p")` (+ve) | `"apple".count(5)` raises TypeError (-ve)

-   `.find()`:
    *   **Purpose:** To find the lowest index in the string where a specific substring is located. It safely returns `-1` if the substring is not found.
    *   **Accepted Data Types:** 1st parameter: String (the substring to search for). 2nd and 3rd parameters: Integers (start and end indices for slicing).
    *   **Mandatory/Optional:** 1st parameter is Mandatory. 2nd and 3rd parameters are Optional.
    *   **Return Type:** Integer (Index position or `-1`).
    *   **Examples:** `"hello world".find("world")` (+ve) | `"hello".find(123)` raises TypeError (-ve)

-   `.capitalize()`:
    *   **Purpose:** To convert the first character of a string to uppercase and the rest to lowercase.
    *   **Accepted Data Types:** Strictly Zero Parameters.
    *   **Mandatory/Optional:** Must remain empty `()`.
    *   **Return Type:** String.
    *   **Examples:** `"hello world".capitalize()` (+ve) | `"hello".capitalize(1)` raises TypeError (-ve)

-   `.title()`:
    *   **Purpose:** To convert the first character of each word in a string to uppercase and the remaining characters to lowercase.
    *   **Accepted Data Types:** Strictly Zero Parameters.
    *   **Mandatory/Optional:** Must remain empty `()`.
    *   **Return Type:** String.
    *   **Examples:** `"hello world".title()` (+ve) | `"hello".title(1)` raises TypeError (-ve)

-   `.startswith()`:
    *   **Purpose:** To evaluate whether a string begins with a specified prefix text.
    *   **Accepted Data Types:** String (or a tuple of strings). Optional integer parameters for start and stop positions can be provided.
    *   **Mandatory/Optional:** 1st parameter (prefix) is Mandatory.
    *   **Return Type:** Boolean.
    *   **Examples:** `"python".startswith("py")` (+ve) | `"python".startswith(1)` raises TypeError (-ve)

---

#### III. Dictionary-Specific Methods
Methods are behaviors attached specifically to Python dictionaries (Hash Maps). They are called using the dot syntax directly on the target dictionary object.

-   `.get()`:
    *   **Purpose:** To retrieve the value for a specified key. It safely returns a default value if the key does not exist, preventing a program-crashing KeyError.
    *   **Accepted Data Types:** 1st parameter: Key to search for (String, Integer, etc.). 2nd parameter: Default value to return if missing.
    *   **Mandatory/Optional:** 1st parameter (key) is Mandatory. 2nd parameter (default value) is Optional (defaults to None).
    *   **Return Type:** Any (Returns the value associated with the key, or the default value).
    *   **Examples:** `my_dict.get("a", 0)` (+ve) | `"string".get("a")` raises AttributeError (-ve)

-   `dict.fromkeys()`:
    *   **Purpose:** To create a new dictionary using the elements of an iterable as keys. Since dictionary keys must be unique, it automatically removes duplicates while preserving the original insertion order (in Python 3.7+).
    *   **Accepted Data Types:** 1st parameter: Iterable (String, List) for keys. 2nd parameter: Any data type for the default value.
    *   **Mandatory/Optional:** 1st parameter is Mandatory. 2nd parameter is Optional (defaults to None).
    *   **Return Type:** Dictionary.
    *   **Examples:** `dict.fromkeys("apple")` (+ve) | `dict.fromkeys(123)` raises TypeError (-ve)

---

#### IV. Imported Classes (Standard Library)
Advanced blueprints (Classes) that are not loaded by default and must be brought into the program using import statements.

-   `Counter()` (requires `from collections import Counter`):
    *   **Purpose:** A specialized dictionary (Hash Map) subclass designed for rapid, automatic frequency counting of elements.
    *   **Accepted Data Types:** Iterables (Strings, Lists, Tuples) or mapping objects.
    *   **Mandatory/Optional:** Optional (Providing an iterable counts its items automatically; leaving it empty creates an empty Counter).
    *   **Return Type:** Counter Object (A specialized Dictionary).
    *   **Examples:** `Counter("apple")` (+ve) | `Counter(123)` raises TypeError (-ve)

-   `re.sub()` (requires `import re`):
    *   **Purpose:** To substitute occurrences of a regular expression pattern (or exact substring) in a string with a replacement string.
    *   **Accepted Data Types:** 1st parameter: String (pattern). 2nd parameter: String (replacement). 3rd parameter: String (target text). Optional parameters: `count` (Integer) and `flags` (Integer).
    *   **Mandatory/Optional:** The first 3 parameters are Mandatory.
    *   **Return Type:** String.
    *   **Examples:** `re.sub("a", "o", "cat")` (+ve) | `re.sub("a", 1, "cat")` raises TypeError (-ve)

-   `re.escape()` (requires `import re`):
    *   **Purpose:** To escape special characters (like `.`, `*`, `?`) in a string so it can be safely used as a literal, normal text pattern in regex operations.
    *   **Accepted Data Types:** String.
    *   **Mandatory/Optional:** Mandatory (Requires exactly 1 string parameter).
    *   **Return Type:** String.
    *   **Examples:** `re.escape("hello.world")` (+ve) | `re.escape(123)` raises TypeError (-ve)

## V. List-Specific Methods

-   `.append()`:
    *   **Purpose:** To add a single item to the very end of an existing list. It modifies the original list in place.
    *   **Accepted Data Types:** Any valid Python data type (String, Integer, List, Dictionary, Object, etc.).
    *   **Mandatory/Optional:** Mandatory (Requires exactly 1 parameter).
    *   **Return Type:** None (Modifies the original list directly).
    *   **Examples:** `my_list.append("apple")` (+ve) | `my_list.append(1, 2)` raises TypeError (-ve)