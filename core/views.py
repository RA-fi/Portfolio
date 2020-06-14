from django.shortcuts import render
from django.views.generic import TemplateView
from .models import *


# Create your views here.
class HomeTemplateView(TemplateView):
	template_name = 'home.html'

	# override get context data method
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)

		context['information'] = Information.objects.all()
		context['about'] = About.objects.first()
		context['services'] = Service.objects.all()
		context['works'] = RecentWork.objects.all()
		return context

