# rock-paper-scissors

##Setup
Thanks for playing! When opening the terminal for the first time, navigate to the repo. Then, create a new virtual environment with the below command. This will ensure you are running the correct version of Python.
```sh
conda create -n my-gam-env python=3.8
```
Once the virtual environment is created, activate it with the following command:
```sh
conda activate my-gam-env
```

Once the environment is activated successfully, input your player name and run the following code to start the game
```sh
player_name="Your name here" python game.py
```

##Playing
When prompted, enter rock, paper, or scissors to play against the computer. Hit enter. If you receive an 'invalid' response, start the game over with the following command:
```sh
python game.py
```

##Winner
The code will tell you who won the game. If you would like to play again, start over with:
```sh
python game.py
```