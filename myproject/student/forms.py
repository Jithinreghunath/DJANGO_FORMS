from django import forms
from django.core.exceptions import ValidationError
from student.models import Contact

class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = "__all__"
        # fields = ["name", "content"]
        # exclude = ["name"]

    def clean(self):
        """
        Raise `ValidationError` if user didn't provide both name and email.
        """
        cleaned_data = super().clean() 
        name = cleaned_data.get("name")
        email = cleaned_data.get("email")
        Age = cleaned_data.get("Age")



        if not name and not email:
            raise ValidationError("Please provide name or email.")

        if Age < 18:
             raise ValidationError("Must be greater than 18.")

        
        
        return cleaned_data  
        
        

