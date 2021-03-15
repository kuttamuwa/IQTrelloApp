from django.apps import AppConfig

from IQTrelloLatest.settings import DEBUG


class CommentsConfig(AppConfig):
    name = 'comments'

    def ready(self):
        if not DEBUG:
            self.do_before_app()

    def do_before_app(self):
        pass

