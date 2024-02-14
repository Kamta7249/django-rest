from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TodoSerializer, TimingTodoSerializer
from .models import Todo, TimingTodo
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

# Create your views here.


@api_view(['GET'])
def get_todo(request):
    todo_objs = Todo.objects.all()
    serializer = TodoSerializer(todo_objs, many=True)

    return Response({
        'status': True,
        'message': 'Todo Fetched',
        'data' : serializer.data
    })    

@api_view(['POST'])
def post_todo(request):
    try:
        data = request.data
        serializer = TodoSerializer(data = data)
        if  serializer.is_valid():
            serializer.save()
            # print(serializer.data)
            return Response({
                'status': True,
                'message': 'Success Data',
                'data' : serializer.data
            })

        return Response({
            'status': False,
            'message': 'Invalid Data !!',
            'data' : serializer.errors
        })

    except Exception as e:
        print(e)
        return Response({
            'status': False,
            'message': 'Something went wrong'
        })

@api_view(['PATCH'])
def patch_todo(request):
    try:
        data = request.data
        if not data.get('uid'):
            return Response({
                'status': False,
                'message': 'uid is required',
                'data': {}
            })
        
        obj = Todo.objects.get(uid = data.get('uid'))
        serializer = TodoSerializer(obj, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            # print(serializer.data)
            return Response({
                'status': True,
                'message': 'Success Data',
                'data' : serializer.data
            })
        
        return Response({
            'status': False,
            'message': 'Invalid Data !!',
            'data' : serializer.errors
        })
    except Exception as e:
        print(e)

    return Response({
        'status': False,
        'message': 'Invalid  UID !!',
        'data' : {}
    })


class TodoView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request):
        print(request.user)
        todo_objs = Todo.objects.filter(user=request.user)
        serializer = TodoSerializer(todo_objs, many=True)

        return Response({
            'status': True,
            'message': 'Todo Fetched',
            'data' : serializer.data
        })    
        # return Response({
        #     'status': 200,
        #     'message': 'Yes! Django rest framework is working !!!',
        #     'method_called': 'You called GET method'
        # })
    
    def post(self, request):
        try:
            data = request.data
            data['user'] = request.user.id
            serializer = TodoSerializer(data = data)
            if  serializer.is_valid():
                serializer.save()
                # print(serializer.data)
                return Response({
                    'status': True,
                    'message': 'Success Data',
                    'data' : serializer.data
                })

            return Response({
                'status': False,
                'message': 'Invalid Data !!',
                'data' : serializer.errors
            })

        except Exception as e:
            print(e)
            return Response({
                'status': False,
                'message': 'Something went wrong'
            })

        # return Response({
        #     'status': 200,
        #     'message': 'Yes! Django rest framework is working !!!',
        #     'method_called': 'You called POST method'
        # })

class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


    @action(detail=False, methods=['GET'])
    def get_timing_todo(self, request):
        objs = TimingTodo.objects.all()
        serializer = TimingTodoSerializer(objs, many=True)
        return Response({
            'status': True,
            'message': 'Timing todo Fetched',
            'data' : serializer.data
        })        

    @action(detail=False, methods=['post'])
    def add_date_to_todo(self, request):
        try:
            data = request.data
            print(data)
            serializer = TimingTodoSerializer(data=data)
            print(serializer)

            if serializer.is_valid():
                serializer.save()
                return Response({
                    'status': True,
                    'message': 'Success Data',
                    'data' : serializer.data
                })
            return Response({
                'status': False,
                'message': 'Invalid Data !!',
                'data' : serializer.errors
            })
            
        except Exception as e:
            print(e)
            return Response({
                'status': False,
                'message': 'Something went Wrong'
            })

