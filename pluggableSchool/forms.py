from django import forms
from .models import Class,Student

class ClassForm(forms.ModelForm):
    class Meta:
        model = Class
        fields = ['class_name', 'block']

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['classroom', 'first_name', 'last_name']

    def __init__(self, *args, **kwargs):
        class_instance = kwargs.pop('class_instance', None)
        super(StudentForm, self).__init__(*args, **kwargs)
        if class_instance:
            self.fields['classroom'].initial = class_instance
