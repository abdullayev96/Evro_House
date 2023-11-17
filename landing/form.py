from django import forms



class ContactForm(forms.Form):
    name= forms.CharField(
        min_length=1,
        widget=forms.TextInput({}
        )
    )
    email= forms.EmailField(
        widget=forms.TextInput(
            {}
            
        )
    )
    number= forms.CharField(
        min_length=2,
        widget=forms.NumberInput(
            attrs={}))