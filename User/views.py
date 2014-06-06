from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import render
from django.views import generic
from django.views.generic.base import TemplateView
from django.views.generic import DetailView

from User.models import User, UserDetails

class IndexView(TemplateView):
	"""
	Shows the login form for the user.
	"""
	template_name = "User/index.html"

class HomeView(generic.DetailView):
	"""
	Renders the home page after logging in
	"""
	model = UserDetails
	template_name = "User/home.html"
	context_object_name = 'user'
	
	def get_context_data(self, **kwargs):
		context = super(HomeView, self).get_context_data(**kwargs)
		return context

def login(request):
	"""
	Controls the login mechanism.
	Redirects to home page for successs, otherwise renders the login form again with an error message.
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