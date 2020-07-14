import json
from strava_api.AuthServer import authenticate

config = json.load(open("config.json"))


def test_authorize():
    # TODO add mock to make this run better
    assert authenticate is not None
