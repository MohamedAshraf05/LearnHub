from django.shortcuts import render
from django.views.generic import TemplateView , ListView , DetailView
from .models import Teachers , Courses
# Create your views here.

class Home(TemplateView):
    template_name = 'pages/index.html'

class AboutUs(ListView):
    queryset = Teachers.objects.all()
    template_name = 'pages/about.html'
    context_object_name = "teachers"

class ContactUs(TemplateView):
    template_name = 'pages/contact.html'

class CoursesView(ListView):
    queryset = Courses.objects.all()
    template_name = "pages/courses.html"
    context_object_name = 'courses'

class Admissions(TemplateView):
    template_name = 'pages/admissions.html'

class CoursesDetialView(DetailView):
    queryset = Courses.objects.all()
    template_name = 'pages/course-single.html'
    context_object_name = 'course'