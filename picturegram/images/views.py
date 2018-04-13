# from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from . import models, serializers

# Create your views here.
class ListAllImages(APIView):
	# format none이면 json
	def get(self, request, format=None):
		all_images = models.Image.objects.all()
		# 모델 안에 있는 모든 오브젝트 종류의 이미지를 가져와
		serializer = serializers.ImageSerializer(all_images, many=True)

		return Response(data=serializer.data)

class ListAllComments(APIView):
	def get(self, request, format=None):
		all_comments = models.Comment.objects.all()
		serializer = serializers.CommentSerializer(all_comments, many=True)

		return Response(data=serializer.data)

class ListAllLikes(APIView):
	def get(self, request, format=None):
		all_likes = models.Like.objects.all()
		serializer = serializers.LikeSerializer(all_likes, many=True)

		return Response(data=serializer.data)