import string

string.ascii_lowercase
# 'abcdefghijklmnopqrstuvwxyz'
string.ascii_uppercase
# 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
string.ascii_letters
# The concatenation of the ascii_lowercase and ascii_uppercase constants described below
# 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
string.digits
# '0123456789'
string.hexdigits
#'0123456789abcdefABCDEF'
string.octdigits
# '01234567'
string.punctuation
# '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
string.whitespace
# A string containing all ASCII characters that are considered whitespace. 
# This includes the characters space, tab, linefeed, return, formfeed, and vertical tab.
# ' \t\n\r\x0b\x0c'
string.printable
# String of ASCII characters which are considered printable. This is a combination of digits, ascii_letters, punctuation, and whitespace.
#'0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ \t\n\r\x0b\x0c'
