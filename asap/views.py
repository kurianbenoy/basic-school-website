from django.shortcuts import render
from django.http import HttpResponse

from .forms import Asap_UploadForm
from .models import Asap_Upload
# Create your views here.

def asap_form(request):
	form = Asap_UploadForm()
	if request.method == 'POST':
		form = Asap_UploadForm(request.POST,request.FILES)
		if form.is_valid():
			form.save()		
	context = {'form':form}
	return render(request,'asap/asap_upload.html',context)

def asap_feed(request):
	details = Asap_Upload.objects.all()
	context ={"data":details}
	return render(request,'asap/asapfeed.html',context)


