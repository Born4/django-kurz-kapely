from django import forms
from bands.models import Band


class BandGenericForm(forms.Form):
    """"""
    name = forms.CharField(max_length=64,
                           label="Nazev",
                           help_text="Zadejte nazev kapely - max 64 znaku",
                           widget=forms.TextInput(),
                           required=True)
    year = forms.IntegerField(label="Rok",
                              help_text="Zadejte rok zalozeni kapely",
                              widget=forms.NumberInput(),
                              required=True)


class BandModelForm(forms.ModelForm):
    """"""
    class Meta:
        model = Band
        fields = ['name', 'year']
        labels = {
            'name': 'Nazev kapely',
            'year': 'Rok vzniku'
        }
        help_texts = {
            'name': 'Zadejte nazev kapely - max 64 znaku',
            'year': 'Zadejte rok zalozeni kapely'
        }
