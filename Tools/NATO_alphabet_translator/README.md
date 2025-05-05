<p align="center">
  <a href="https://github.com/AseanK/beginner-python-games" target="_blank">
    <img src="../../images/tools_logo.png" width = "2560px" height = "200px">
  </a>
</p>

# NATO Alphabet Translator
<!-- Game Rules -->
## Features
1. This program converts the normal alphabet into the NATO phonetic alphabet which is commonly used by militaries and other organisations that communicate via radio
2. Enter a word and it'll do the rest for you!

## How to install and run
1. Fork the repo by clicking the fork logo on the top right <img src="../../images/fork.png" width="300" height="60">
2. Clone the repo `git clone git@github.com:AseanK/beginner-python-games.git`
3. Head to the NATO_alphabet_translator folder
4. Run the file using python command `python translator.py`

## Slight adjustments for readability
1) Added single check statement that will check if letter is entered
2) Removed redundant while loop (outer) because there is no way to break out of program once you start it
3) Removed redundant quit statement in Intro() function
4) Moved intro() inside single function as its all prints statements