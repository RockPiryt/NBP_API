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

I created this project to complete intern task.

## Technologies Used

- Python - version 3.11
- Flask - version 2.2.2
- SQLAlchemy - version 1.4.45
- WTForms - version  3.0.1
- PostgreSQL database

## Features

List the ready features here:

1. Given a date (formatted YYYY-MM-DD) and a currency code (list: [https://nbp.pl/en/statistic-and-financial-reporting/rates/table-a/](https://nbp.pl/en/statistic-and-financial-reporting/rates/table-a/)), provide its average exchange rate.
2. Given a currency code and the number of last quotations N (N <= 255), provide the max and min average value (every day has a different average).
3. Given a currency code and the number of last quotations N (N <= 255), provide the major difference between the buy and ask rate (every day has different rates).

## Previews

### Home Page

![Home Page Preview](myproject/static/img/previews/prev_home_page.jpg)

### Section 1 - aaaa

![Section 1 Preview - Stock trading information using API](myproject/static/img/previews/prev_section_1_stock_trading.jpg)

## Setup

- Clone This Project git clone
- Enter Project Directory cd NBP_API
- Create a Virtual Environment (for Windows) python -m venv (name your virtual enviroment :) venv

'EXAMPLE: python -m venv venv'

- Activate Virtual Environment source: venv/Scripts/activate
- Install Requirements Package pip install -r requirements.txt
- Finally Run The Project: python app.py

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
