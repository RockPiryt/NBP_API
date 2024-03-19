# NBP_API

REST_API to query data from the Narodowy Bank Polski's public APIs and return relevant information from them.

## Table of Contents

* [General Info](#general-information)
* [Technologies Used](#technologies-used)
* [Features](#features)
* [Previews](#Previews)
* [Setup](#setup)
* [Project Status](#project-status)
* [Room for Improvement](#room-for-improvement)
* [Contact](#contact)
* [License](#license)

## General Information

REST API to query data from the NBP public API. The documentation can be found https://documenter.getpostman.com/view/24234549/2sA2xpTpBw

## Technologies Used

* Python 3.11
* Flask 2.2.2
* Alembic 1.8.1
* SQLAlchemy 1.4.43
* Pytest 7.2.0
* PostgreSQL
* AWS
* Postman

## Features

List the ready features here:

1. Given a date (formatted YYYY-MM-DD) and a currency code (list: [https://nbp.pl/en/statistic-and-financial-reporting/rates/table-a/](https://nbp.pl/en/statistic-and-financial-reporting/rates/table-a/)), provide its average exchange rate.
2. Given a currency code and the number of last quotations N (N <= 255), provide the max and min average value (every day has a different average).
3. Given a currency code and the number of last quotations N (N <= 255), provide the major difference between the buy and ask rate (every day has different rates).

## Previews

### Average exchange rate

![Average exchange rate Preview](Documentation/screenshots/first_request.jpg)

### The max and min average value

![The max and min average value Preview ](Documentation/screenshots/second_request.jpg)

### The major difference between the buy and ask rate

![The major difference between the buy and ask rate Preview ](Documentation/screenshots/third_request.jpg)


## Setup

- Clone repository NBP_API

```buildoutcfg

git clone NBP_API

```

- Enter Project Directory cd NBP_API

```buildoutcfg

cd NBP_API

```

- Create  database and user
- Rename .env.example to .env and set your calues

```buildoutcfg

# SQLALCHEMY_DATABASE_URI template

SQLALCHEMY_DATABASE_URI = mysql+pymysql://{db_user}:{db_password}@{db_host}/{database}?charset=utf8mb4

```

- Create a virtual evironment

```buildoutcfg

python -m venv venv

```

- Activate Virtual Environment

```buildoutcfg

source: venv/Scripts/activate

```

- Install packages from requirements.txt

```buildoutcfg

pip install -r requirements.txt

```

- Migrate database

```buildoutcfg

flask db upgrade

```

- Run command

```buildoutcfg

python nbp.py

```

## Project Status

Project is: _in progress_

## Room for Improvement

Room for improvement:

* Unit/integration tests.
* Docker image of the whole application.
* Swagger UI or any other simple front-end (with e.g. React, Angular).

## Contact

- Created by [@RockPiryt Github](https://github.com/RockPiryt)
- My Resume [@RockPiryt Resume](https://rockpiryt.github.io/Personal_Site/)

Feel free to contact me!

## License

This project is open source and available under the [aa]
