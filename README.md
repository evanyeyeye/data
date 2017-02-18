# Data Alexa Skill #
Data Alexa Skill for Big Parser

## Setup ##

* dryscrape requires webkit-server which in turn requires qt5. Ensure you have qt5 installed on your system before installing dryscrape.

* Install required initial packages `pip install --user virtualenv autoenv`

* Add `source /usr/bin/activate.sh` to `~/.bashrc`

* Create a virtualenv using `virtualenv --no-site-packages --distribute -p <PATH TO PYTHON 3 EXECUTABLE> <NAME>`

* `cd` into the project root directory and autoenv should activate

* Install the required packages using `pip install -r requirements.txt`

* Go to the [pygsheets documentation](http://pygsheets.readthedocs.io/en/latest/authorizing.html) and follow the instructions for OAuth Credentials

* Run `auth.py` and copy the url from the program to browser and authorize the application with Google

* The url should give a verification code to be pasted back into the program

* Rename `client_secretxxx.json` to `client_secret.json`

* Edit `.env` and change the empty strings to their appropriate values
