from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import BoardSerializer
from rest_framework import status
from .models import Board

from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication


class BoardView(APIView):
    @api_view(['POST'])
    @permission_classes((IsAuthenticated, ))
    @authentication_classes((JSONWebTokenAuthentication,))
    def post(request):
        board_serializer = BoardSerializer(data=request.data)
        if board_serializer.is_valid():
            board_serializer.save()
            return Response(board_serializer.data, status=201)
        else:
            return Response(board_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @api_view(['GET'])
    @permission_classes((IsAuthenticated, ))
    @authentication_classes((JSONWebTokenAuthentication,))
    def get(request, **kwargs):
        if kwargs.get('id') is None:
            board_queryset = Board.objects.all()
            board_queryset_serializer = BoardSerializer(
                board_queryset, many=True)
            return Response(board_queryset_serializer.data, status=status.HTTP_200_OK)
        else:
            id = kwargs.get('id')
            board_serializer = BoardSerializer(Board.object.get(id=id))
            return Response(board_serializer.data, status=status.HTTP_200_OK)

    @api_view(['PUT'])
    @permission_classes((IsAuthenticated, ))
    @authentication_classes((JSONWebTokenAuthentication,))
    def put(request, **kwargs):
        return Response("ok", status=status.HTTP_200_OK)

    @api_view(['DELETE'])
    @permission_classes((IsAuthenticated, ))
    @authentication_classes((JSONWebTokenAuthentication,))
    def delete(request, **kwargs):
        return Response("ok", status=status.HTTP_200_OK)
