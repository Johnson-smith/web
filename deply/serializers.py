from rest_framework import serializers
from deply.models import Fabu, LANGUAGE_CHOICES, STYLE_CHOICES





class DeplySerializer(serializers.ModelSerializer):
    class Meta:
        model = Fabu
        fields = ('id', 'version', 'servername', 'product', 'linenos', 'language', 'style')