"""Add the element ‘Python’ to a tuple input_tuple = ('Monty Python', 'British', 1969). Since tuples are immutable, one way to do this is to convert the tuple to a list, add the element, and convert it back to a tuple.
Sample Input:

('Monty Python', 'British', 1969)

Sample Output:

﻿('Monty Python', 'British', 1969, 'Python')"""

input_tuple = ('Monty Python', 'British', 1969)

# Write your code here

tuple_2 = input_tuple[:] + ("Python",)

# Make sure to name the final tuple 'tuple_2'
print(tuple_2)