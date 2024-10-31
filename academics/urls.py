from django.urls import path
from .views import *

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('about/' , AboutUs.as_view() , name='about'),
    path('contact/' , ContactUs.as_view() , name='contact'),
    path('courses/' , CoursesView.as_view() , name='courses'),
    path('admissions/',Admissions.as_view() , name='admissions'),
    path('courses/' , CoursesView.as_view() , name='courses'),
    path('courses/<int:pk>/' , CoursesDetialView.as_view() , name='course-detail'),
]