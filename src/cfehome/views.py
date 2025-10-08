from django.http import HttpResponse
from django.shortcuts import render
from visits.models import PageVisit
def home_view(request, *args, **kwargs):
    queryset = PageVisit.objects.all()
    PageVisit.objects.create()
    return render(request, "base.html", {})