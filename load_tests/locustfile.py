from locust import task, run_single_user
from locust import FastHttpUser


class average(FastHttpUser):
    host = "https://r2qw1eeeve.execute-api.eu-west-1.amazonaws.com"
    default_headers = {
        "accept-encoding": "gzip, deflate, br, zstd",
        "accept-language": "pl-PL,pl;q=0.9,en-US;q=0.8,en;q=0.7",
        "sec-ch-ua": '"Opera";v="109", "Not:A-Brand";v="8", "Chromium";v="123"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 OPR/109.0.0.0",
    }

    @task
    def t(self):
        with self.rest(
            "GET",
            "/dev/av_exchange_rate/2024-01-12/EUR",
            headers={
                "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
                "cache-control": "max-age=0",
                "sec-fetch-dest": "document",
                "sec-fetch-mode": "navigate",
                "sec-fetch-site": "none",
                "sec-fetch-user": "?1",
                "upgrade-insecure-requests": "1",
            },
        ) as resp:
            pass
        with self.rest(
            "GET",
            "/favicon.ico",
            headers={
                "accept": "image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8",
                "referer": "https://r2qw1eeeve.execute-api.eu-west-1.amazonaws.com/dev/av_exchange_rate/2024-01-12/EUR",
                "sec-fetch-dest": "image",
                "sec-fetch-mode": "no-cors",
                "sec-fetch-site": "same-origin",
            },
        ) as resp:
            pass


if __name__ == "__main__":
    run_single_user(average)
