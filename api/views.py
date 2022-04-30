from django.shortcuts import render
from.serializers import homeserializer,createserializer,create_comment,commentserializer
from rest_framework import status
from rest_framework.views import Response
from rest_framework.decorators import api_view,authentication_classes,permission_classes
from.models import post,comment
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication


# Create your views here.
@api_view(['GET'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def home(request):
    try:
        blog_post=post.objects.all()
    except post.DoesNotExist:
        return Response(status=status.HTTP_204_NO_CONTENT)
    if request.method == 'GET':
        serializer=homeserializer(blog_post,many=True)
        return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def detail(request,id):
    try:
        blog_post = post.objects.get(id=id)
    except post.DoesNotExist:
        return Response(status=status.HTTP_204_NO_CONTENT)
    if request.method == 'GET':
        serializer = homeserializer(blog_post)
        return Response(serializer.data)
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def delete(request,id):
    try:
        blog_post = post.objects.get(id=id)
    except post.DoesNotExist:
        return Response(status=status.HTTP_204_NO_CONTENT)

    if request.method == 'DELETE':
        data = {}
        if blog_post.author == request.user:
            blog_post.delete()
            data['response']='Deleted successfully'
            return Response(data=data)
        else:
             data['error']="You don't have permission to delete this"
             return Response(data=data)
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def update(request,id):
    try:
        blog_post=post.objects.get(id=id)
    except post.DoesNotExist:
        return Response(status=status.HTTP_204_NO_CONTENT)
    if request.method == 'PUT':
        data = {}
        if blog_post.author == request.user:
            serializer=homeserializer(blog_post,data=request.data)
            if serializer.is_valid():
                serializer.save()
                data['response']='Updated successfully'
                data['data']=serializer.data
                return Response(data=data)
            else:
                data['error']='There is an error in updating this'
                return Response(data=data)
        else:
            data['error']="You don't permission to update this"
            return Response(data=data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def create(request):
    if request.method == 'POST':
        user = request.user
        blog_post=post(author=user)
        serializer=createserializer(blog_post,data=request.data,partial=True)
        data={}
        if serializer.is_valid():
            serializer.save()
            data['response']='Created'
            data['data']=serializer.data
            return Response(data=data)
        else:
            data['error'] = "Wasn't able to create this"
            return Response(data=data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def reply(request,id):
    if request.method == 'POST':
        # user=request.user
        # posts=post.objects.get(id=id)
        try:
            posts=post.objects.get(id=id)
        except post.DoesNotExist:
            return Response(status=status.HTTP_204_NO_CONTENT)
        if request.method == 'POST':
            user=request.user
            blog_post=comment(author=user,posts=posts)
            serializer = create_comment(blog_post, data=request.data, partial=True)
            data = {}
            if serializer.is_valid():
                serializer.save()
                data['response'] = 'Created'
                data['data'] = serializer.data
                return Response(data=data)
            else:
                data['error'] = "Wasn't able to create this"
                return Response(data=data)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def update_comment(request,id):
    try:
        blog_post=comment.objects.get(id=id)
    except comment.DoesNotExist:
        return Response(status=status.HTTP_204_NO_CONTENT)
    if request.method == 'PUT':
        data = {}
        if blog_post.author == request.user:
            serializer=createserializer(blog_post,data=request.data,partial=True)
            if serializer.is_valid():
                serializer.save()
                data['response']='Updated successfully'
                data['data']=serializer.data
                return Response(data=data)
            else:
                data['error']='There is an error in updating this'
                return Response(data=data)
        else:
            data['error']="You don't permission to update this"
            return Response(data=data)
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def delete_comment(request,id):
    try:
        blog_post = comment.objects.get(id=id)
    except comment.DoesNotExist:
        return Response(status=status.HTTP_204_NO_CONTENT)

    if request.method == 'DELETE':
        data = {}
        if blog_post.author == request.user:
            blog_post.delete()
            data['response']='Deleted successfully'
            return Response(data=data)
        else:
             data['error']="You don't have permission to delete this"
             return Response(data=data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def detail_comment(request,id):
    try:
        blog_post = comment.objects.get(id=id)
    except comment.DoesNotExist:
        return Response(status=status.HTTP_204_NO_CONTENT)
    if request.method == 'GET':
        serializer = createserializer(blog_post)
        return Response(serializer.data)