# NBP AWS API

This API allows us to query data from the Narodowy Bank Polski's public APIs and return relevant information from them.

## Endpoints

- [Average](#Average)
- [MinMax](#MinMax)
- [Major](#Major)

## Average

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

## MinMax

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

## Major

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
