import os
from typing import Any, Optional

from django.core.management.base import BaseCommand, CommandError

from youtube.youtube_client import YoutubeClient


class Command(BaseCommand):
    help = "Extract videos from Owned Youtube Channel"

    def handle(self, *args: Any, **options: Any) -> Optional[str]:
        base_path = os.path.abspath(os.path.dirname("manage.py"))
        youtube = YoutubeClient(base_path=base_path)
        youtube.extract_video()
