from django import forms
from .models import User

class UserForm(forms.ModelForm):
    
    class Meta:
        model = User
        fields = ('Purpose','Name',  'Notes','Link' )
        widgets = {
            'Purpose': forms.Select(attrs={'class': 'form-control'}),  # Assuming Purpose is a ForeignKey field
            'Name': forms.TextInput(attrs={'class': 'form-control'}),
            'Notes': forms.TextInput(attrs={'class': 'form-control'}),
            'Link': forms.TextInput(attrs={'class': 'form-control'}),
            
        }
        labels ={
            'Purpose': 'Purpose',
            'Name': 'Name',
            'Notes': 'Notes',
            'Link': 'Link'
            
             
        }
        
        def __init__(self, *args, **kwargs):
            super(UserForm,self).__init__(*args,**kwargs)
            self.fields['position'].empty_label = "Select"
            self.fields['Link'].required = False
