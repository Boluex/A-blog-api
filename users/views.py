from rest_framework.views import Response
from rest_framework import status
from rest_framework.decorators import api_view,authentication_classes,permission_classes
from.serializers import register_serializer

@api_view(['POST'])
@permission_classes([])
@authentication_classes([])
def sign_up(request):
    if request.method == 'POST':
        data={}
        serializer=register_serializer(data=request.data)
        if serializer.is_valid():
            data['success'] = 'Welcome'
            data['data'] = serializer.data
            serializer.save()
            return Response(data=data)
        else:
            data['error']="Can't register this user"
            return Response(data=data)