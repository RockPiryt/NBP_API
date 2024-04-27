# NBP_API

This API allows us to query data from the Narodowy Bank Polski's public APIs and return relevant information from them.

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

FLask Application and AWS API.

### Postman

The documentation can be found 
```buildoutcfg
https://documenter.getpostman.com/view/24234549/2sA2xpTpBw
```

### NBP AWS API

### AWS invoke url
```buildoutcfg
https://r2qw1eeeve.execute-api.eu-west-1.amazonaws.com/dev
```

### Endpoints

- [Average](#Average)
- [MinMax](#MinMax)
- [Major](#Major)

### Average

User provides a date (formatted YYYY-MM-DD) and a currency code.
Returns the average exchange rate.

**`GET /av_exchange_rate/{user_date}/{curr_code}`**

**Headers**

| Name           | value            | 
|----------------|------------------|
| `Content-Type` | application/json |

**Path Parameters**

| Name        | Type    | In   | Required | Description            |
|-------------|---------|------|----------|------------------------|
| `user_date` | string  | path | Yes      | Date                   |
| `curr_code` | string  | path | Yes      | Currency Code          |

**Status codes**

| Status code        | Description                                                        |
|--------------------|--------------------------------------------------------------------|
| 200 OK             | Indicates a successful response.                                   |
| 406 Not Acceptable | Indicates wrong header "Content-Type"                              |
| 422 Unprocessable Content| Request with wrong URL, or without required path parameters. |

Example Response:
````
{
  "statusCode": 200, 
  "success": true, 
  "body": "\"You chose a currency code:EUR and a date (formatted YYYY-MM-DD): 2024-01-12. Average exchange rate is 4.3574.\""
}
````
#### Examples
```buildoutcfg
https://r2qw1eeeve.execute-api.eu-west-1.amazonaws.com/dev/av_exchange_rate/{user_date}/{curr_code}
```
User gives 2 path parameters: 
{user_date} - a date (formatted YYYY-MM-DD) (example 2024-01-12)
{curr_code}  - a currency code (example EUR)

example:
```buildoutcfg
https://r2qw1eeeve.execute-api.eu-west-1.amazonaws.com/dev/av_exchange_rate/2024-01-12/EUR
```

### MinMax

User provides a currency code and the number of last quotations N (N <= 255).
Returns the max and min average value (every day has a different average).

**`GET /min_max_av/{curr_code}/{last_quo}`**


**Headers**

| Name           | value            | 
|----------------|------------------|
| `Content-Type` | application/json |

**Path Parameters**

| Name        | Type    | In   | Required | Description                                    |
|-------------|---------|------|----------|------------------------------------------------|
| `last_quo ` | string  | path | Yes      | The number of last quotations                  |
| `curr_code` | string  | path | Yes      | Currency Code                                  |

**Status codes**

| Status code              | Description                                                        |
|--------------------------|--------------------------------------------------------------------|
| 200 OK                   | Indicates a successful response.                                   |
| 406 Not Acceptable       | Indicates wrong header "Content-Type"                              |
| 422 Unprocessable Content| Request with wrong URL, or without required path parameters. |

Example Response:
````
{
  "statusCode": 200, 
  "success": true, 
  "body": "\"You chose a currency code:GBP and the number of last quotations: 15. The max average value is 5.0812 and min average value is 4.966.\""
}
````

#### Examples:
```buildoutcfg
https://r2qw1eeeve.execute-api.eu-west-1.amazonaws.com/dev/ min_max_av/{curr_code}/{last_quo}
```
User gives 2 path parameters: 
{curr_code}  - a currency code (example EUR)
{last_quo} - the number of last quotations N (N <= 255) (example 15)

example:
```buildoutcfg
https://r2qw1eeeve.execute-api.eu-west-1.amazonaws.com/dev/min_max_av/GBP/15
```

### Major

User provides a currency code and the number of last quotations N (N <= 255).
Returns the major difference between the buy and ask rate (every day has different rates).

**`GET /major_diff/{curr_code}/{last_quo}`**


**Headers**

| Name           | value            | 
|----------------|------------------|
| `Content-Type` | application/json |

**Path Parameters**

| Name        | Type    | In   | Required | Description                                    |
|-------------|---------|------|----------|------------------------------------------------|
| `last_quo ` | string  | path | Yes      | The number of last quotations                  |
| `curr_code` | string  | path | Yes      | Currency Code                                  |

**Status codes**

| Status code              | Description                                                        |
|--------------------------|--------------------------------------------------------------------|
| 200 OK                   | Indicates a successful response.                                   |
| 406 Not Acceptable       | Indicates wrong header "Content-Type"                              |
| 422 Unprocessable Content| Request with wrong URL, or without required path parameters. |

Example Response:
````
{
  "statusCode": 200, 
  "success": true, 
  "body": "\"You chose a currency code:USD and the number of last quotations: 10. The major difference between the buy and ask rate is 0.0820\""
  }
````

#### Examples:
```buildoutcfg
https://r2qw1eeeve.execute-api.eu-west-1.amazonaws.com/dev/major_diff/{curr_code}/{last_quo}
```
User gives 2 path parameters: 
{curr_code}  - a currency code (example USD)
{last_quo} - the number of last quotations N (N <= 255) (example 10)

example
```buildoutcfg
https://r2qw1eeeve.execute-api.eu-west-1.amazonaws.com/dev/major_diff/USD/10
```
## Technologies Used

* Python 3.11
* Flask 3.0.2
* Alembic 1.13.1
* SQLAlchemy 2.0.28
* Pytest 8.1.1
* PostgreSQL
* AWS (API Gateway + Lambda Funcitons)
* Postman

## Features

List the ready features here:

1. Given a date (formatted YYYY-MM-DD) and a currency code (list: [https://nbp.pl/en/statistic-and-financial-reporting/rates/table-a/](https://nbp.pl/en/statistic-and-financial-reporting/rates/table-a/)), provide its average exchange rate.
2. Given a currency code and the number of last quotations N (N <= 255), provide the max and min average value (every day has a different average).
3. Given a currency code and the number of last quotations N (N <= 255), provide the major difference between the buy and ask rate (every day has different rates).

## Previews

### AWS Rest Api
### Average exchange rate

![Average exchange rate Preview](Documentation/screenshots/av_exchange_rate.jpeg)

### The max and min average value

![The max and min average value Preview ](Documentation/screenshots/min_max_av.jpeg)

### The major difference between the buy and ask rate

![The major difference between the buy and ask rate Preview ](Documentation/screenshots/major_diff.jpeg)


### Postman

### Average exchange rate

![Average exchange rate Preview](Documentation/screenshots/first_request.jpeg)

### The max and min average value

![The max and min average value Preview ](Documentation/screenshots/second_request.jpeg)

### The major difference between the buy and ask rate

![The major difference between the buy and ask rate Preview ](Documentation/screenshots/third_request.jpeg)

## Setup

- Clone repository NBP_API

```buildoutcfg

git clone https://github.com/RockPiryt/NBP_API.git

```

- Enter Project Directory cd NBP_API

```buildoutcfg

cd NBP_API

```

- Create  database
- Rename .env.example to .env and set your calues

```buildoutcfg

# SQLALCHEMY_DATABASE_URI template

SQLALCHEMY_DATABASE_URI = f"postgresql://{username_postdb}:{password_postdb}@{host_postdb}/{database_postdb}"

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

flask run

```

## Project Status

Project is: _in progress_

## Room for Improvement

Room for improvement:

* Unit/integration tests for Flask application.
* Docker image of the whole application.
* Swagger UI 


## Contact

- Created by [@RockPiryt Github](https://github.com/RockPiryt)
- My Resume [@RockPiryt Resume](https://paulinakimak.com)

Feel free to contact me!

## License

This project is open source and available under the [aa]
