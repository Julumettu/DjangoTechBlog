from django.utils import timezone
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import get_object_or_404
import os


def about(request):
    return HttpResponse("Tää on vähän tyhjä vielä")

