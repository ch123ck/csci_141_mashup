import sys

# This should be a command script rather than a function.  This means the file will execute statements,
# whereas a function definition does nothing and requires the function to be called.
#
# You've already seen an example:
print('hello, world!')
# This statement is not inside a function definition, and is therefore executed when we provoke python:
# python fgrep.py

# Observe how sys.argv captures the command line arguments.  Invoke this file with
#   python fgrep.py fee fie foe fum
# and see what is printed.
print(sys.argv)

# How to format a string:
vile = 'foo.txt'
line = 'A child of five could understand this!  Fetch me a child of five!'  # From /usr/games/fortune
print(f'{vile}: {line}')  # See the notebook string_formatting.ipynb.
# This is how the lines of your output should appear.
