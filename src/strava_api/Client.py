"""Main module."""
import requests
from .Athlete import Athlete


class Client:
    """Class to manage your Strava API Client"""

    def __init__(
        self, client_id: str, client_secret: str, auth_token: str, refresh_token: str
    ) -> None:
        """initialize client with application attributes"""
        self.client_id = client_id
        self.client_secret = client_secret
        self.auth_token = auth_token
        self.refresh_token = refresh_token

        # create variables
        self.athlete = None

    def set_athlete(self, auth_code: str) -> None:
        try:
            response = requests.post(
                url="https://www.strava.com/oauth/token",
                params={
                    "client_id": self.client_id,
                    "client_secret": self.client_secret,
                    "code": auth_code,
                    "grant_type": "authorization_code",
                },
            )

            self.athlete = Athlete(response.json())

        except requests.exceptions.RequestException:
            print("HTTP Request failed")
