<p align="center">
  <a href="https://github.com/AseanK/beginner-python-games" target="_blank">
    <img src="../../images/logo.png" width = "2560px" height = "200px">
  </a>
</p>


# ChinChiro

## Rules
1. The dealer and player each roll three dice.
2. The outcome is determined by the combination of the dice.
3. If the player wins, the payout is calculated by the score of the role.
4. If the player loses, the bet is lost.
5. If the role a has negative score, the player loses the bet multiplied by the score.


|  **Role**   |                   **Dice Combination**                    | **Score** |
|:-----------:|:---------------------------------------------------------:|:---------:|
| **Pinzoro** |               1 - 1 - 1 (A triplet of ones)               |     5     |
| **Triplet** | 2 - 2 - 2 / 3 - 3 - 3 / 4 - 4 - 4 / 5 - 5 - 5 / 6 - 6 - 6 |     3     |
| **Jigoro**  |             4 - 5 - 6 (A straight of 4, 5, 6)             |     2     |
| **Normal**  |                      e.g., 2 - 2 - 5                      |     1     |
| **No Role** |                      e.g., 2 - 4 - 6                      |    -1     |
| **Hifumi**  |             1 - 2 - 3 (A straight of 1, 2, 3)             |    -2     |

### Same Role Comparison
**Triplet**: The higher number wins. (e.g., 6 - 6 - 6 > 3 - 3 - 3)
**Normal**:
1. The higher unique number wins. (e.g., 2 - 2 - 4 > 5 - 5 - 1)
2. If the unique numbers are the same, the higher total wins. (2 - 6 - 6 > 2 - 3 - 3)

## How to play
1. Fork the repo by clicking the fork logo the on top right <img src="../../images/fork.png" width="300" height="60">
2. Clone the repo `git clone git@github.com:AseanK/beginner-python-games.git`
3. Head to the checkers folder
4. Run the file using python command `python chin_chiro.py`