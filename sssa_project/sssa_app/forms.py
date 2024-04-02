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
                    "style": "text-align: center; color:black; font-size: 25px",
                },
            ),
            "catalogue_name": forms.TextInput(
                attrs={
                    "id": "key_id",
                    "required": True,
                    "placeholder": "Catalogue Name",
                    "style": "text-align: left; color:black; font-size: 25px",
                },
            ),
            "fieldworker": forms.TextInput(
                attrs={
                    "id": "key_id",
                    "required": True,
                    "placeholder": "Fieldworker",
                    "style": "text-align: center; color:black; font-size: 25px",
                },
            ),
            "date": forms.TextInput(
                attrs={
                    "id": "key_id",
                    "required": True,
                    "placeholder": "Date",
                    "style": "text-align: center; color:black; font-size: 25px",
                },
            ),
            "informant_artist": forms.TextInput(
                attrs={
                    "id": "key_id",
                    "required": True,
                    "placeholder": "Informant Artist",
                    "style": "text-align: left; color:black; font-size: 25px;",
                },
            ),
            "native_area_county": forms.TextInput(
                attrs={
                    "id": "key_id",
                    "required": True,
                    "placeholder": "Native Area County",
                    "style": "text-align: left; color:black; font-size: 25px;",
                },
            ),
            "comments": forms.TextInput(
                attrs={
                    "id": "key_id",
                    "required": True,
                    "placeholder": "Comments",
                    "style": "text-align: left; color:black; font-size: 25px;",
                },
            ),
            "place_recorded": forms.TextInput(
                attrs={
                    "id": "key_id",
                    "required": True,
                    "placeholder": "Place Recorded",
                    "style": "text-align: left; color:black; font-size: 25px;",
                },
            ),
            "type_of_material": forms.TextInput(
                attrs={
                    "id": "key_id",
                    "required": True,
                    "placeholder": "Type of Material",
                    "style": "text-align: left; color:black; font-size: 25px;",
                },
            ),
            "summary": forms.TextInput(
                attrs={
                    "id": "key_id",
                    "required": True,
                    "placeholder": "Summary",
                    "style": "text-align: left; color:black; font-size: 25px;",
                },
            ),
            "disc_matrix_number": forms.TextInput(
                attrs={
                    "id": "key_id",
                    "required": True,
                    "placeholder": "Disc Matrix Number",
                    "style": "text-align: left; color:black; font-size: 25px;",
                },
            ),
            "tale_reference": forms.TextInput(
                attrs={
                    "id": "key_id",
                    "required": True,
                    "placeholder": "Tale Reference",
                    "style": "text-align: left; color:black; font-size: 25px;",
                },
            ),



        }






    def __init__(self, *args, **kwargs):
        super(AlstForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False