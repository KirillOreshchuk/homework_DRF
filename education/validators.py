from rest_framework import serializers


class UrlValidator:

    def __init__(self, video_url):
        self.video_url = video_url

    def __call__(self, value):
        if (dict(value).get(self.video_url) and 'youtube.com' not in dict(value).get(self.video_url).split(
                '/')) and 'www.youtube.com' not in dict(value).get(self.video_url).split('/'):
            raise serializers.ValidationError('Нет ссылки на YouTube')
