from .models import Alst
from django import forms
from crispy_forms.helper import FormHelper
from django import forms



class AlstNameFilterForm(forms.Form):
    catalogue_number = forms.CharField()


class AlstForm(forms.ModelForm):
    class Meta:
        model = Alst

        fields = [
            'catalogue_number',
            'collection',
            'collection_ref',
            'parent',
            'first_line',
            'type_of_material',
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
            'instrument',
            'camera_operator',
            'old_number_rl',
            'restricted',
        ]
        widgets = {
            "catalogue_number": forms.TextInput(
                attrs={
                    "id": "key_id",
                    "required": False,
                    "placeholder": "Catalogue Number",
                    "class": "record-input",  # add a reusable class
                },
            ),
            "collection": forms.TextInput(
                attrs={
                    "id": "key_id",
                    "required": False,
                    "placeholder": "Collection",
                    "style": "text-align: center; color:black; font-size: 25px",
                },
            ),
            "collection_ref": forms.TextInput(
                attrs={
                    "id": "key_id",
                    "required": False,
                    "placeholder": "Collection Ref",
                    "style": "text-align: center; color:black; font-size: 25px",
                },
            ),
            "camera_operator": forms.TextInput(
                attrs={
                    "id": "key_id",
                    "required": False,
                    "placeholder": "Camera Operator",
                    "style": "text-align: center; color:black; font-size: 25px",
                },
            ),
            "first_line": forms.TextInput(
                attrs={
                    "id": "key_id",
                    "required": False,
                    "placeholder": "First Line",
                    "style": "text-align: center; color:black; font-size: 25px",
                },
            ),

            "parent": forms.TextInput(
                attrs={
                    "id": "key_id",
                    "required": False,
                    "placeholder": "Parent",
                    "style": "text-align: center; color:black; font-size: 25px",
                },
            ),
            "instrument": forms.TextInput(
                attrs={
                    "id": "key_id",
                    "required": False,
                    "placeholder": "Instrument",
                    "style": "text-align: center; color:black; font-size: 25px",
                },
            ),
            "catalogue_name": forms.TextInput(
                attrs={
                    "id": "key_id",
                    "required": False,
                    "placeholder": "Catalogue Name",
                    "style": "text-align: left; color:black; font-size: 25px",
                },
            ),
            "fieldworker": forms.TextInput(
                attrs={
                    "id": "key_id",
                    "required": False,
                    "placeholder": "Fieldworker",
                    "style": "text-align: center; color:black; font-size: 25px",
                },
            ),
            "date": forms.TextInput(
                attrs={
                    "id": "key_id",
                    "required": False,
                    "placeholder": "Date",
                    "style": "text-align: center; color:black; font-size: 25px",
                },
            ),
            "informant_artist": forms.TextInput(
                attrs={
                    "id": "key_id",
                    "required": False,
                    "placeholder": "Informant Artist",
                    "style": "text-align: left; color:black; font-size: 25px;",
                },
            ),
            "native_area_county": forms.TextInput(
                attrs={
                    "id": "key_id",
                    "required": False,
                    "placeholder": "Native Area County",
                    "style": "text-align: left; color:black; font-size: 25px;",
                },
            ),
            "comments": forms.TextInput(
                attrs={
                    "id": "key_id",
                    "required": False,
                    "placeholder": "Comments",
                    "style": "text-align: left; color:black; font-size: 25px;",
                },
            ),
            "place_recorded": forms.TextInput(
                attrs={
                    "id": "key_id",
                    "required": False,
                    "placeholder": "Place Recorded",
                    "style": "text-align: left; color:black; font-size: 25px;",
                },
            ),
            "type_of_material": forms.TextInput(
                attrs={
                    "id": "key_id",
                    "required": False,
                    "placeholder": "Type of Material",
                    "style": "text-align: left; color:black; font-size: 25px;",
                },
            ),
            "summary": forms.TextInput(
                attrs={
                    "id": "key_id",
                    "required": False,
                    "placeholder": "Summary",
                    "style": "text-align: left; color:black; font-size: 25px;",
                },
            ),
            "disc_matrix_number": forms.TextInput(
                attrs={
                    "id": "key_id",
                    "required": False,
                    "placeholder": "Disc Matrix Number",
                    "style": "text-align: left; color:black; font-size: 25px;",
                },
            ),
            "tale_reference": forms.TextInput(
                attrs={
                    "id": "key_id",
                    "required": False,
                    "placeholder": "Tale Reference",
                    "style": "text-align: left; color:black; font-size: 25px;",
                },
            ),
            'restricted': forms.Select(attrs={
                'class': 'form-control',
                "style": "text-align: left; color:black; font-size: 25px;"
            }),

        }

    def __init__(self, *args, **kwargs):
        super(AlstForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False
