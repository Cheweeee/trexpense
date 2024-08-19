from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Expense

def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())

def expenses(request):
    myexpenses = Expense.objects.all().values()
    template = loader.get_template('all_expenses.html')
    context = {
        'myexpenses': myexpenses,
    }
    return HttpResponse(template.render(context, request))

def details(request, id):
  myexpense = Expense.objects.get(id=id)
  template = loader.get_template('details.html')
  context = {
    'myexpense': myexpense,
  }
  return HttpResponse(template.render(context, request))

def testing(request):
  template = loader.get_template('template.html')
  context = {
    'fruits': ['Apple', 'Banana', 'Cherry'],   
  }
  return HttpResponse(template.render(context, request))