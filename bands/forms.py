from django import forms
from django.core.exceptions import ObjectDoesNotExist

from bands.models import Band, Album
from bands.utils.data_access import check_object_duplicity
from django.core.validators import MinValueValidator, MaxValueValidator


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
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'year': forms.NumberInput(attrs={'class': 'form-control'})
        }

    def clean_name_old(self):
        """"""
        # print("-------------------")
        # print("clean->name")
        # print(self.cleaned_data)
        # print("-------------------")
        new_name = self.cleaned_data.get('name')

        is_duplicity = False

        try:
            # print("TESTUJI ADRESU v DB")
            sb_band = Band.objects.get(name=new_name)
            if self.instance:
                if sb_band.pk != self.instance.pk:
                    is_duplicity = True
        except ObjectDoesNotExist:
            # print("Duplicita zda se neexistuje...")
            pass
        if is_duplicity:
            # print("Duplicita je na urovni clean_name")
            if isinstance(is_duplicity, Band):
                kapela_existuje = is_duplicity.full_name
            else:
                kapela_existuje = "EXISTUJE JICH VICE !!!"
            raise forms.ValidationError(f"Kapela zadaneho jmena: {new_name} uz existuje: "
                                        f"({kapela_existuje}), zadejte jine dekuji...")
        return new_name

    def clean(self):
        """"""
        # print("-------------------")
        # print("clean->ALL")
        # print(self.cleaned_data)
        # print("-------------------")
        new_name = self.cleaned_data.get('name')

        is_duplicity = False

        try:
            # print("TESTUJI ADRESU v DB")
            db_band = Band.objects.get(name=new_name)
            if self.instance:
                if db_band.pk != self.instance.pk:
                    is_duplicity = True
        except ObjectDoesNotExist:
            # print("Duplicita zda se neexistuje...")
            pass
        if is_duplicity:
            # print("Duplicita je na urovni clean_name")
            raise forms.ValidationError(f"Kapela zadaneho jmena: {new_name} uz existuje, "
                                        f"zadejte jine dekuji...")


class BandInAlbumChoiceFiled(forms.ModelChoiceField):
    """Modifikace zobrazeni Band ...."""
    def label_from_instance(self, obj):
        return obj.roletove_menu_pojmenovani


class AlbumModelForm(forms.ModelForm):
    """"""
    band = BandInAlbumChoiceFiled(queryset=Band.objects.all(), help_text="Vyber kapelu")

    class Meta:
        model = Album
        fields = '__all__'

    def clean(self):
        """"""
        # print("-------------------")
        # print("clean->ALL")
        # print(self.cleaned_data)
        # print("-------------------")
        new_name = self.cleaned_data.get('name')

        is_duplicity = False

        try:
            # print("TESTUJI ADRESU v DB")
            db_album = Album.objects.get(name=new_name)
            if self.instance:
                if db_album.pk != self.instance.pk:
                    is_duplicity = True
        except ObjectDoesNotExist:
            # print("Duplicita zda se neexistuje...")
            pass
        if is_duplicity:
            # print("Duplicita je na urovni clean_name")
            raise forms.ValidationError(f"Album zadaneho jmena: {new_name} uz existuje, "
                                        f"zadejte jine dekuji...")

