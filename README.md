# data
Data Alexa Skill for Big Parser

### Setup ###

* Create a virtualenv using `virtualenv --no-site-packages --distribute -p <PATH TO PYTHON EXECUTABLE> <NAME>`

* `cd` into the project root directory and autoenv should activate

* Install the required packages using `pip install -r requirements.txt`

* Go to the [http://pygsheets.readthedocs.io/en/latest/authorizing.html](pygsheets documentation) and follow the instructions for authorization

* Rename `client_secretxxx.json` to `client_secret.json`

* Edit `.env` and change the empty strings to their appropriate values
