from django.shortcuts import render
from basicapp.models import Student
from django.urls import reverse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView,SingleObjectMixin
from django.views.generic.edit import CreateView,UpdateView
from .forms import StudentModelForm
# Create your views here.
class StudentCreateView(CreateView):
    form_class = StudentModelForm
    # success_url = 'student-detail'
    template_name = 'students_form.html'

    def get_success_url(self):
        return reverse('student-detail',kwargs={'pk':self.object.id})

class StudentDetailView(DetailView,SingleObjectMixin):
    model = Student
    template_name = 'student_detail.html'


class StudentListView(ListView):
    model = Student
    template_name = 'student_list.html'
