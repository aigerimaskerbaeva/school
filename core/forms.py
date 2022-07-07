from django.forms import ModelForm
from core.models import Category,EmpLoyee

class CategoryForms(ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'description']

class EmployeeForms(ModelForm):
    class Meta:
        model = EmpLoyee
        fields = [' first_name','lust_name', 'email_adderess','phone_number']
