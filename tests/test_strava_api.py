from strava_api.Client import Client


def test_strava_api():
    assert Client() is not None
