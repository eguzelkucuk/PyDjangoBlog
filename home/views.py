from django.shortcuts import render, HttpResponse

# Create your views here.
def home_view(request):
 context={
  'personal':['Erkan','Ali']
 }
 return render(request, 'Home.html', context)