from django.shortcuts import render
from django.http import HttpResponse
from .models import Student
from django.views.generic.edit import FormView
from .forms import RegistrationForm, SigninForm

def user_auth(request,lang):
    return render(request,'user_auth/' + lang + '/user_auth.html')


def register(request,lang):
    #return HttpResponse('<h1>It Worked Mister!</h1>')
    return render(request,'user_auth/' + lang + '/register_form.html',{})

def register_response(request,lang):
    user = Student()
    return HttpResponse('<h1>It Worked Mr.' + str(user) + '!</h1>')



class RegistrationView(FormView):
    template_name = 'user_auth/en/register_form.html'
    form_class = RegistrationForm
    #success_url = '/thanks/'

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        #form.send_email()
        return super().form_valid(form)


    def get(self, request, *args, **kwargs):
        self.template_name = 'user_auth/' + self.kwargs['lang']+'/register_form.html'
        return super().get(self, request)


class SigninView(FormView):
    template_name = 'user_auth/en/signin_form.html'
    form_class = SigninForm
    #success_url = '/thanks/'

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        #form.send_email()
        return super().form_valid(form)

    def get(self, request, *args, **kwargs):
        self.template_name = 'user_auth/' + self.kwargs['lang']+'/signin_form.html'
        return super().get(self, request)
