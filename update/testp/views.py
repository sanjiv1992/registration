from django.shortcuts import render
from django.http import HttpResponse
#from testp.forms import userform
from rest_framework import viewsets
from testp.serializers import userserializers
from testp.models import userform
# Create your views here.
'''def end(request):
    if request.method=='POST':
        user=userForm(request.POST, request.FILES)
        if user.is_valid():
            user.save()
            return HttpResponse('submitted file')

    else:
        user=userForm()
        return render(request, 'testp/index.html', {'form':user})
'''

class listview(viewsets.ModelViewSet):
    queryset = userform.objects.all()
    serializer_class = userserializers