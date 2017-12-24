from django import forms
from .models import NssUpload

class NssUploadForm(forms.ModelForm):
	class Meta:
		model = NssUpload
		widget ={
		'description' : forms.Textarea(attrs={'rows':10,'cols':15}),
		}
		fields = ['title','description','photo']
