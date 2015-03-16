Algorithms for scoring a Yhatzee hand.
===

The algorithm returns the highest score, must be able to score these combinations.

Upper section combinations:
---

Get as many of one value as possible. The score is value * repeats. E.g.
if you get 1, 3, 3, 3, 5 and you choose Threes you will get 3 * 3 = 9 points.

- Ones
- Twos
- Threes
- Fours
- Fives
- Sixes

Lower section combinations:
---

- Three of a kind: Get three dice with the same number. Score is the sum of 
all dice (not just the three of a kind).

- Four of a kind: Get four dice with the same number. Score is the sum of all
dice (not just the four of a kind).

- Full house: Get three of a kind and a pair, e.g. 1, 1, 3, 3, 3. Scores 25
points.

- Small straight: Get four sequential dice, 1, 2, 3, 4 or 2, 3, 4, 5 or
3, 4, 5, 6. Scores 30 points.

- Large straight: Get five sequential dice, 1, 2, 3, 4, 5 or 2, 3, 4, 5, 6.
Scores 30 points.

- YAHTZEE: Five of a kind. Scores 50 points.
