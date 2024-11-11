<p align="center">
  <a href="https://github.com/AseanK/beginner-python-games" target="_blank">
    <img src="../../images/logo.png" width = "2560px" height = "200px">
  </a>
</p>


# ChinChiro

## Rules
1. The dealer and player compete against each other.
2. Three dice are rolled simultaneously. 
3. The outcome is determined by the roles of the dice.


|    Roles    |                              Dice                              | Multiplier |
|:-----------:|:--------------------------------------------------------------:|:----------:|
|  One Pair   |                           1 - 1 - 1                            |     5      |
| Other Pairs |   2 - 2 - 2 / 3 - 3 - 3 / 4 - 4 - 4 / 5 - 5 - 5 / 6 - 6 - 6    |     3      |
|   Jigoro    |                           4 - 5 - 6                            |     2      |
|   Normal    | O, O, X <br/>The player with the smaller unique number(X) wins |   1/ -1    |
|   No role   |                        e.g., 2 - 4 - 6                         |     -1     |
|   Hifumi    |                           1 - 2 - 3                            |     -2     |

## How to play
1. Fork the repo by clicking the fork logo the on top right <img src="../../images/fork.png" width="300" height="60">
2. Clone the repo `git clone git@github.com:AseanK/beginner-python-games.git`
3. Head to the checkers folder
4. Run the file using python command `python chin_chiro.py`