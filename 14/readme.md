## Day 14 Debug Log

I struggled a lot with parsing the given input.

The major error that I made was with 2D matrix initialization in Python. To map out the cave map, I started out with populating an 2D array of adequate size (`700`, which is larger than all coordinates in the input) with `0`s to represent an empty cave. Below is my code for doing this:
```python
rows, cols = 700, 700
cave_map = [[0]*cols]*rows
```
The problem with this approach is that each row will be referencing the same column due to Python usage of shallow lists. So when I update only one element in a specific row, all the elements in the same column of the map got updated as well. This resulted in an incorrect parsing of the map since all the rows in the map ended up looking the same.

The solution is to initialize the 2D matrix with List Comprehension:
```python
cave_map = [[0 for _ in range(cols)] for _ in range(rows)]
```
In this way, `700` separate list objects will be created, and updating any element in the map will not affect the other rows in the map.