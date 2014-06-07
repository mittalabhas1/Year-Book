from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import render
from django.views import generic
from django.views.generic.base import TemplateView
from django.views.generic import DetailView
from django.core.exceptions import ValidationError, NON_FIELD_ERRORS

from User.models import User, UserDetails

class IndexView(TemplateView):
	"""
	Shows the login form for the user.
	"""
	template_name = "User/index.html"

def login(request):
	"""
	Controls the login mechanism.
	Redirects to home page for success, otherwise renders the login form again with an error message.
	"""
	try:
		user = User.objects.get(username=request.POST['username'], password=request.POST['password'])
	except User.DoesNotExist:
		return render(request, 'User/index.html', {
			'error_message': "Invalid Credentials !",
		})
	else:
		try:
			userDetail = UserDetails.objects.get(uid=user.id)
		except UserDetails.DoesNotExist:
			return render(request, 'User/details.html', {
				'uid': user.id,
			})
		else:
			return HttpResponseRedirect(reverse(
				'user:home', args=(user.id,)
			))

def saveDetails(request):
	"""
	Controls the details post mechanism.
	Redirects to home page for success, otherwise renders the same page again.
	"""
	try:
		user = User.objects.get(pk=request.POST['uid'])
		user = UserDetails.objects.create(uid=user, name=request.POST['name'], dob=request.POST['dob'], email=request.POST['email'], hometown=request.POST['hometown'], course=request.POST['course'])
		user.save()
	except ValidationError as e:
		return render(request, 'User/details.html', {
			'error_message': "Please complete all the fields with correct and neccessary details !",
		})
	else:
		return HttpResponseRedirect(reverse(
			'user:home', args=(user.id,)
		))

class HomeView(generic.DetailView):
	"""
	Renders the home page after logging in
	"""
	model = UserDetails
	template_name = "User/home.html"
	context_object_name = "thisUser"
	
	def get_context_data(self, **kwargs):
		context = super(HomeView, self).get_context_data(**kwargs)
		return context