from django import forms


class CreateListForm(forms.Form):
    name = forms.CharField(label="Name ", max_length=300)


class DocumentForm(forms.Form):
    docfile = forms.FileField(label='select GeoJSON file containing water rights boundary')
