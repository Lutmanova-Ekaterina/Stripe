from rest_framework import serializers


class ForbiddenWordsValidator:
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        title = value.get('header')
        if title:
            for word in ['война', "оружие", "ЛГБТ", "насилие"]:
                if word in title:
                    raise serializers.ValidationError('Запрещенные слова в заголовке.')
