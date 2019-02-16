from rest_framework.views import APIView
from rest_framework.response import Response
from . import models, serializers


class ListAllImages(APIView):

    def get(self, request, format=None):

        all_images = models.Image.objects.all()

        serialzer = serializers.ImageSerializer(all_images, many=True)

        return Response(data=serialzer.data)

class ListAllComments(APIView):

    def get(self, request, format=None):

        all_comments = models.Comment.objects.all()

        serialzer = serializers.CommentSerializer(all_comments, many=True)

        return Response(data=serialzer.data)

class ListAllLikes(APIView):

    def get(self, request, format=None):

        all_likes = models.Like.objects.all()

        serialzer = serializers.LikeSerializer(all_likes, many=True)        

        return Response(data = serialzer.data)