# Bot-Assignments

<p> ** This bot was only possibly easy made using the https://github.com/luisbrandino/team-scrap repository. **

This bot was created for sending all assignments on a telegram chat </p>

## Setup

Before executing this bot you need to install the following things:

### Python

This bot was made with Python so you need to download it<br>
:snake: Download Python3 [here](https://www.python.org/downloads/)

Inside the project folder, on cmd or terminal, this this code to install the dependencies: 

#### Windows
~~~python
python -m pip install -r requirements.txt
~~~

#### Linux and Mac
~~~python3
python3 -m pip install -r requirements.txt
~~~

## Running

#### Windows
```
src\main.py
```

#### Linux e Mac
```
python3 src/main.py
```

### How to use

When the script is started for the first time, it will be necessary to inform your Token that gives access to the API `onenote.com`

To obtain this Token you need to find one file inside google devtools, here is a tutorial with images:

- Log in to your Microsoft Teams account and go to the teams page <br>

- After that, press ** F12 ** and go to the ** Network ** tab on devtools <br>

- Then go to the ** Tasks ** tab and wait for an item called ** classes ** or ** work?... ** to appear on devtools <br>

- Click on that item, go to the ** Headers ** tab and scroll down until you find ** Request headers **, then view the header ** authorization ** and copy all letters and numbers after the word ** Carrier * * or ** Bearer * *<br>

After following these steps, you have your Token! <br>
To start using the program, just paste this code when prompted

NOTE: This Token may expire after some time and you will need to redo these steps, as long as the Token is valid, it will be saved on your machine encrypted for use
