from rest_framework import serializers

class Only_Youtube:
    def __init__(self, field):
        self.field = field
    def __call__(self, value):
        temp_value = dict(value).get(self.field)
        if "youtube.com" not in temp_value.lower():
            raise serializers.ValidationError("Разрешены только ссылки на youtube.com")
