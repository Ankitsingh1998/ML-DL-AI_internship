#some regex examples
"""

[abc]{3} - a|b|c pair of 3
\.\.\. o \.{3}
\D - all except digit
\d - all digit
\d\d\d or \d{3} - 3 digits consecutively
\d{2-4} - two to four digits consecutively
[a-z]{3} or [a-z][a-z][a-z] - a to z three times consecutively
[a-z0-9A-Z] - all digits and letters whether uppercase or lowercase
[^abc] - everything except a|b|c (like negation) - ^ inside class will revert it
\w - any alphanumeric character ([a-zA-Z0-9])
\W - all except alphanumeric characters or any non-alphanumeric character
\s - whitespaces (spacebar, \n, \t,etc)
^ before any character it means search all that starts wih that chracter (^ metacharacter)
$ at last of a regex means search all that ends with that character ($ metacharactyer)
Example (+) metacharacter: [a-c]+\.{4}[d-f]+  , here (+) means repetition one or more time or atleast one character present
Example (*) metacharacter: [a-c]*\.{4}[d-f]*  , here (*) means repetition zero or more time
Example (?) metacharacter: [a-c]?\.{4}[d-f]?  , here (?) means repetition zero or one time

"""
