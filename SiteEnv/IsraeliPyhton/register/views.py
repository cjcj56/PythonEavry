from django.shortcuts import render
from django.http import HttpResponse
from .models import Student
from django.views.generic.edit import FormView
from .forms import RegistrationForm

def register(request):
    #return HttpResponse('<h1>It Worked Mister!</h1>')
    return render(request,'register/register_form.html',{})

def register_response(request):
    user = Student()
    return HttpResponse('<h1>It Worked Mr.' + str(user) + '!</h1>')



class RegistrationView(FormView):
    template_name = 'register/register_form.html'
    form_class = RegistrationForm
    #success_url = '/thanks/'

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        #form.send_email()
        return super(RegistrationView, self).form_valid(form)