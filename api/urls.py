from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter
router=DefaultRouter()
router.register('employeesViewset',views.Employee_Viewset,basename='employee')

urlpatterns = [
    #function based student crud 
    path('students/', views.studentView, name="studentviews" ),
    path('students/<int:pk>/',views.studentDetailView),

    #class based crud
    path('employees/',views.EmployeeView.as_view()),
    path('employees/<int:pk>/',views.EmployeeDetailView.as_view()),

    #mixin based crud
    path('employeesMixin/',views.Employeesmixin.as_view()),
    path('employeesMixin/<int:pk>/',views.EmployeeViewmixin.as_view()),

    #generics API based crud
    path('employeesGeneric/',views.Employeesgeneric.as_view()),
    path('employeesGeneric/<int:pk>/',views.EmployeeViewgeneric.as_view()),

    #viewset based CRUD
    path('',include(router.urls)),

    #nested serializer
    path('blogs/',views.BlogsView.as_view() ),
    path('comments/',views.CommentsView.as_view()),

    path('blogs/<int:pk>',views.BlogsDetailView.as_view() ),
    path('comments/<int:pk>',views.CommentsDetailView.as_view() ),
]