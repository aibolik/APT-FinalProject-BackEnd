from rest_framework import serializers
from ..models import Word


class ShortSerializer(serializers.ModelSerializer):
	class Meta:
		model = Word
		fields = ['id','title','definition', 'language']


class DetailedSerializer(serializers.ModelSerializer):
	class Meta:
		model = Word
		fields = ['id','title','definition','language','translation','synonyms','antonyms']
		depth=1

