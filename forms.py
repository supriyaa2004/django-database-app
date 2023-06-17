# # from django import forms
# # from .models import book

# # class bookForm(forms.ModelForm):
# #     class Meta:
# #         model = book
# #         fields = ['name', 'email' , 'tittle' , 'publisher' , 'year' , 'status' , 'roll']

# from django import forms

# # class ProductForm(forms.Form):
# #     name = forms.CharField(max_length=100)
# #     price = forms.DecimalField(max_digits=8, decimal_places=2)
# #     description = forms.CharField(widget=forms.Textarea)
# class ProductForm(forms.Form):
#     name = forms.CharField(max_length=100)
#     email=forms.EmailField()
#     tittle=forms.CharField(max_length=50)
#     publisher=forms.CharField(max_length=100)
#     year=forms.IntegerField()
#     status=forms.CharField(max_length=20)
#     roll = forms.IntegerField()
from django import forms
from .models import book

class AddRecordForm(forms.ModelForm):
    class Meta:
        model = book
        fields = '__all__'
class DisplayRecordForm(forms.ModelForm):
    class Meta:
        model = book
        fields = '__all__'
        widgets = {
            field_name: forms.TextInput(attrs={'readonly': True})
            for field_name in book._meta.get_fields()
        }

class DeleteRecordForm(forms.Form):
    Author_first_name = forms.CharField(label='Author First Name', max_length=100)
