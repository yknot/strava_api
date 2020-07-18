from datetime import datetime


class Athlete:
    def __init__(self, raw_response: dict) -> None:
        # access information
        self.access_token = raw_response["access_token"]
        self.refresh_token = raw_response["refresh_token"]
        self.expires_at = datetime.fromtimestamp(raw_response["expires_at"])

        # identifiers
        self.name = raw_response["athlete"]["username"]
        self.id = raw_response["athlete"]["id"]

        # full response
        self.raw = raw_response

