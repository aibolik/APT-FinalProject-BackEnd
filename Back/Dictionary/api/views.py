from rest_framework import generics
from ..models import Word
from .serializers import *
from .urls import * 
from django.core.urlresolvers import reverse

class GetByLanguage(generics.ListAPIView):
	serializer_class = ShortSerializer
	def get_queryset(self):
		language = self.kwargs.get("language")
		print(1)
		arr = Word.objects.filter(language='{}'.format(language))
		return sorted(arr)

class GetByTitle(generics.ListAPIView):
	serializer_class = ShortSerializer
	def get_queryset(self):
		language = self.kwargs.get("language")
		print(language)
		symbol = self.kwargs.get("symbol")
		print(symbol)
		arr = Word.objects.filter(language=language).filter(title__startswith=symbol)
		return sorted(arr)

class GetById(generics.ListAPIView):
	serializer_class = DetailedSerializer
	def get_queryset(self):
		print "asd"
		language = self.kwargs.get("language")
		print language 
		pk = self.kwargs.get("pk")
		pk = int (pk)
		arr = Word.objects.filter(language=language).filter(pk=pk)
		return sorted(arr)

# class GetTranslate(generics.ListAPIView):
# 	serializer_class = DetailedSerializer
# 	def get_queryset(self):
# 		print "i'm here"
# 		language = self.kwargs.get("language")
# 		pk = self.kwargs.get("pk")
# 		symbol = self.kwargs.get("symbol")



