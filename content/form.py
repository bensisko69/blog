from django.forms import ModelForm, Textarea
from .models import Contact

class ContactForm(ModelForm):
	class Meta:
		model = Contact
		fields = ('firstname', 'lastname', 'email', 'text')
		widgets = {'text': Textarea(attrs={'cols': 80, 'rows': 20}),}