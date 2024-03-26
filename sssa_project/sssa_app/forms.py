from .models import Alst
from django import forms
from crispy_forms.helper import FormHelper
class AlstForm(forms.ModelForm):
    class Meta:
        model = Alst

        fields = [
            'catalogue_number',
            'catalogue_name',
            'fieldworker',
            'date',
            'informant_artist',
            'native_area_county',
            'comments',
            'place_recorded',
            'type_of_material',
            'summary',
            'disc_matrix_number',
            'tale_reference',
            'title',
            'reference',
            'old_number_rl',
            'data_record_input',
            'data_last_amended',
            ]
        widgets = {
            "catalogue_number": forms.TextInput(
                attrs={
                    "id": "key_id",
                    "required": True,
                    "placeholder": "Catalogue Number",
                    "style": "text-align: center; color:black",
                },
            ),
            "catalogue_name": forms.TextInput(
                attrs={
                    "id": "key_id",
                    "required": True,
                    "placeholder": "Catalogue Name",
                    "style": "text-align: center; color:black",
                },
            ),
            "fieldworker": forms.TextInput(
                attrs={
                    "id": "key_id",
                    "required": True,
                    "placeholder": "Fieldworker",
                    "style": "text-align: center; color:black",
                },
            ),



        }






    def __init__(self, *args, **kwargs):
        super(AlstForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False