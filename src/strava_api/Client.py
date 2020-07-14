"""Main module."""


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

