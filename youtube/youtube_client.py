import os

from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.oauth2.credentials import Credentials

from django.conf import settings

from youtube import (
    utils,
    settings as youtube_settings,
)

READONLY_SCOPE = ["https://www.googleapis.com/auth/youtube.readonly"]


class YoutubeClient:

    def __init__(self, base_path: str):
        credentials: Credentials = self.__authenticate(base_path=base_path)

        self.youtube = build(
            "youtube", "v3",
            developerKey=settings.GOOGLE_DEVELOPER_KEY,
            credentials=credentials,
            cache_discovery=False
        )

    def __authenticate(self, base_path: str) -> Credentials:  # pragma: no-cov
        credentials_path = os.path.join(
            base_path,
            youtube_settings.PATH_TO_FILES
        )
        client_id_path = os.path.join(
            base_path,
            youtube_settings.PATH_TO_FILES
        )
        if os.path.isfile(f"{credentials_path}{youtube_settings.CREDENTIALS_FILE}"):
            credentials: Credentials = utils.load_credentials_from_file(credentials_path)
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                f"{client_id_path}{youtube_settings.CLIENT_ID_FILE}",
                READONLY_SCOPE
            )
            credentials: Credentials = flow.run_console()
            utils.save_credentials_to_file(
                utils.credentials_to_dict(credentials),
                credentials_path
            )
        return credentials

    def extract_video(self):
        # As example
        video_public = self.youtube.videos().list(
            part="id,snippet,contentDetails,fileDetails,player,processingDetails,recordingDetails,statistics,status,suggestions,topicDetails",
            id="dummy_id"
        ).execute()
        print(video_public)
