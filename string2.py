import math

# !/usr/bin/env python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

# Additional basic string exercises

# D. verbing
# Given a string, if its length is at least 3,
# add 'ing' to its end.
# Unless it already ends in 'ing', in which case
# add 'ly' instead.
# If the string length is less than 3, leave it unchanged.
# Return the resulting string.


def verbing(s):
    # Your code goes here.  Edit this docstring.
    resulting_string = s
    if len(s) > 2:
        if s[-3:] == 'ing':
            resulting_string = s + 'ly'
        else:
            resulting_string = s + 'ing'

    return resulting_string


# E. not_bad
# Given a string, find the first appearance of the
# substring 'not' and 'bad'. If the 'bad' follows
# the 'not', replace the whole 'not'...'bad' substring
# with 'good'.
# Return the resulting string.
# So 'This dinner is not that bad!' yields:
# This dinner is good!
def not_bad(s):
    # Your code goes here.  Edit this docstring.
    result_string = s
    nindex = s.find('not')
    bindex = s.find('bad')
    if bindex > nindex:
        rep_string = s[nindex:bindex + 3]
        result_string = result_string.replace(rep_string, 'good')
    return result_string


# F. front_back
# Consider dividing a string into two halves.
# If the length is even, the front and back halves are the same length.
# If the length is odd, we'll say that the extra char goes in the front half.
# e.g. 'abcde', the front half is 'abc', the back half 'de'.
# Given 2 strings, a and b, return a string of the form
#  a-front + b-front + a-back + b-back


def front_back(a, b):
    # Your code goes here.  Edit this docstring.
    a_front = ''
    b_front = ''
    a_back = ''
    b_back = ''
    if len(a) % 2 == 0:
        a_front = a[:int(len(a) / 2)]
        a_back = a[int(len(a) / 2):]
    else:
        a_front = a[:math.ceil(len(a) / 2)]
        a_back = a[math.floor(len(a) / 2) + 1:]

    if len(b) % 2 == 0:
        b_front = b[:int(len(b) / 2)]
        b_back = b[int(len(b) / 2):]
    else:
        b_front = b[:math.ceil(len(b) / 2)]
        b_back = b[math.floor(len(b) / 2) + 1:]

    return a_front + b_front + a_back + b_back


# Provided simple test() function used in main() to print
# what each function returns vs. what it's supposed to return.
def test(got, expected):
    # Your code goes here.  Edit this docstring.
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {} expected: {}'.format(prefix, repr(got), repr(expected)))


# main() calls the above functions with interesting inputs,
# using the above test() to check if the result is correct or not.
def main():
    # Your code goes here.  Edit this docstring.
    print('verbing')
    test(verbing('hail'), 'hailing')
    test(verbing('swiming'), 'swimingly')
    test(verbing('do'), 'do')

    print()
    print('not_bad')
    test(not_bad('This movie is not so bad'), 'This movie is good')
    test(not_bad('This dinner is not that bad!'), 'This dinner is good!')
    test(not_bad('This tea is not hot'), 'This tea is not hot')
    test(not_bad("It's bad yet not"), "It's bad yet not")

    print()
    print('front_back')
    test(front_back('abcd', 'xy'), 'abxcdy')
    test(front_back('abcde', 'xyz'), 'abcxydez')
    test(front_back('Kitten', 'Donut'), 'KitDontenut')


# Standard boilerplate (python idiom) to call the main() function.
if __name__ == '__main__':
    main()
