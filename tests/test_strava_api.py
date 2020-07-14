import json
from strava_api.Client import Client

config = json.load(open("config.json"))


def test_strava_api():
    assert (
        Client(
            config["CLIENT_ID"],
            config["CLIENT_SECRET"],
            config["AUTH_TOKEN"],
            config["REFRESH_TOKEN"],
        )
        is not None
    )
