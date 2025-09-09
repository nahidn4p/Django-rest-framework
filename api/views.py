from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from students.models import Student
from employees.models import Employees
from blogs.models import Blog,Comment
from blogs.serializers import BlogSerializers,CommentSerializers
from .serializers import StudentSerializer, EmployeeSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import mixins,generics,viewsets
from .paginations import CustomPagination
from rest_framework.filters import SearchFilter,OrderingFilter
from .filters import EmployeeFilter
# Create your views here.
#normal function based view
@api_view(["GET", "POST"])
def studentView(request):
    if request.method == "GET":
        # get all data from student table
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == "POST":
        # check if request.data is a list (multiple students)
        if isinstance(request.data, list):
            serializer = StudentSerializer(data=request.data, many=True)
        else:
            serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(["GET", "PUT", "DELETE"])
def studentDetailView(request, pk):
    try:
        student = Student.objects.get(pk=pk)
    except Student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = StudentSerializer(student)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == "PUT":
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#class based view
class EmployeeView(APIView):
    def get(self, request):
        employees = Employees.objects.all()
        serializer = EmployeeSerializer(employees, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):

        if isinstance(request.data, list):
            serializer = EmployeeSerializer(data=request.data, many=True)
        else:
            serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
class EmployeeDetailView(APIView):
        def get(self,request,pk):
                try:
                    employee = Employees.objects.get(pk=pk)
                except Employees.DoesNotExist:
                    return Response(status=status.HTTP_404_NOT_FOUND)
                serializer=EmployeeSerializer(employee)
                return Response(serializer.data,status=status.HTTP_200_OK)

        def put(self, request, pk):
                try:
                    employee = Employees.objects.get(pk=pk)
                except Employees.DoesNotExist:
                    return Response(status=status.HTTP_404_NOT_FOUND)

                serializer = EmployeeSerializer(employee, data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_200_OK)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        def delete(self,request, pk):
                try:
                    employee = Employees.objects.get(pk=pk)
                except Employees.DoesNotExist:
                    return Response(status=status.HTTP_404_NOT_FOUND)
                
                employee.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)
        

#mixin based views with generics.GenericAPIView
# get all data  and create data using mixins.ListModelMixin,mixins.CreateModelMixin
class Employeesmixin (mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
     queryset=Employees.objects.all()
     serializer_class=EmployeeSerializer

     def get(self,request):
          return self.list(request)
     def post(self,request):
          return self.create(request)     
# retrieve, update and destroy single data using mixins.RetrieveModelMixin,mixins.UpdateModelMixin ,mixins.DestroyModelMixin
class EmployeeViewmixin (mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView): 
     queryset=Employees.objects.all()
     serializer_class=EmployeeSerializer
     def get(self,request,pk):
          return self.retrieve(request,pk)    
     def put(self,request,pk):
          return self.update(request,pk)     
     def delete(self,request,pk):
          return self.destroy(request,pk)
     

#GENERICS API CRUD
# get and Create data 
# class Employeesgeneric(generics.ListAPIView, generics.CreateAPIView):    for individual ListAPI and CreateAPI
class Employeesgeneric(generics.ListCreateAPIView):
     queryset=Employees.objects.all()
     serializer_class=EmployeeSerializer
class EmployeeViewgeneric(generics.RetrieveUpdateDestroyAPIView): #combination of generics.[retrive, update and destroy] APIVIEW
        queryset=Employees.objects.all()
        serializer_class=EmployeeSerializer
        lookup_field='pk'


#VIEWSET BASED CRUD 
# (viewsets.ViewSet)
"""
class Employee_Viewset(viewsets.ViewSet):
     def list(self,request):
          queryset=Employees.objects.all()
          serializer=EmployeeSerializer(queryset,many=True)
          return Response(serializer.data,status=status.HTTP_200_OK)
     def create(self,request):
          serializer=EmployeeSerializer(data=request.data)
          if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
          return Response(serializer.errors)
     def retrieve(self,request,pk=None):
          employee=get_object_or_404(Employees,pk=pk)
          serializer=EmployeeSerializer(employee)
          return Response(serializer.data,status=status.HTTP_200_OK)
     def update(self,request,pk=None):
            employee=get_object_or_404(Employees,pk=pk)
            serializer=EmployeeSerializer(employee,data=request.data)
            if serializer.is_valid():
                serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
     def delete(self,request,pk=None):
            employee=get_object_or_404(Employees,pk=pk)
            employee.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
"""

#(viewsets.ModelViewSet) based CRUD
class Employee_Viewset(viewsets.ModelViewSet):
     queryset=Employees.objects.all()
     serializer_class= EmployeeSerializer
     pagination_class=CustomPagination
     filterset_class = EmployeeFilter
     
class BlogsView(generics.ListCreateAPIView):
     queryset=  Blog.objects.all()
     serializer_class=BlogSerializers
     filter_backends=[SearchFilter,OrderingFilter]
     search_fields=['blog_title','blog_desc']
     ordering_fields=['id']

class CommentsView(generics.ListCreateAPIView):
     queryset= Comment.objects.all()
     serializer_class=CommentSerializers

class BlogsDetailView(generics.RetrieveUpdateDestroyAPIView):
     queryset=Blog.objects.all()
     serializer_class=BlogSerializers
     lookup_field="pk"
class CommentsDetailView(generics.RetrieveUpdateDestroyAPIView):
     queryset=Comment.objects.all()
     serializer_class=CommentSerializers
     lookup_field="pk"     
     

