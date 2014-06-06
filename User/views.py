from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import render
from django.views import generic
from django.views.generic.base import TemplateView

from User.models import User, UserDetails

class IndexView(TemplateView):
	"""
	Shows the login form for the user.
	"""
	template_name = "User/index.html"

class HomeView(generic.DetailView):
	model = UserDetails
	template_name = "User/home.html"

def login(request):
	"""
	Controls the login mechanism.
	Redirects to home page for successs, otherwise shows the login form again with an error message.
	"""
	try:
		user = User.objects.get(username=request.POST['username'], password=request.POST['password'])
	except User.DoesNotExist:
		return render(request, 'User/index.html', {
			'error_message': "Invalid Credentials !",
		})
	else:
		return HttpResponseRedirect(reverse(
			'user:home', args=(user.id,)
		))