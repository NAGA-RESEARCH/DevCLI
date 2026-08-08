from django.contrib import admin
from django.urls import path
from django.shortcuts import render

# Yahan hum HttpResponse ki jagah render ka use kar rahe hain
# Ye command Django ko bolegi ki templates folder ke andar se index.html uthao
def home_view(request):
    return render(request, 'index.html')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view),
]
