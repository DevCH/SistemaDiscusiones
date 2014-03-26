# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.views.generic import TemplateView

class IndexView(TemplateView):
	template_name = 'home/index.html'

class NombreView(TemplateView):
	template_name = 'home/nombre.html'

	def get_context_data(self, **kwargs):
		context = super(NombreView, self).get_context_data(**kwargs)
		context['minombre'] = '<b>Carlos Hidalgo</b> <small>es una fregonería...</small>'
		return context