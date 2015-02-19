Merge algorithm for a 2048 game.
===

Models the process of merging all of the tile values in a single row or column. This function takes the list line as a parameter and returns a new list with the tile values from line slid towards the front of the list and merged.

In this function, you are always sliding the values in the list towards the front of the list (the list position with index 0). Empty grid squares with no displayed value will be assigned a value of zero.

- [2, 0, 2, 4] should return [4, 4, 0, 0]
- [0, 0, 2, 2] should return [4, 0, 0, 0]
- [2, 2, 0, 0] should return [4, 0, 0, 0]
- [2, 2, 2, 2] should return [4, 4, 0, 0]
- [8, 16, 16, 8] should return [8, 32, 8, 0]