from django import forms
from .models import Asap_Upload

class Asap_UploadForm(forms.ModelForm):
	class Meta:
		model = Asap_Upload
		fields = ['title','description','photo']