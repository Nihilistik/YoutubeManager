from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    name = "youtubemanager.users"
    verbose_name = _("Users")

    def ready(self):
        try:
            import youtubemanager.users.signals  # noqa F401
        except ImportError:
            pass
