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
                    "class": "record-input",  # add a reusable class
                },
            ),
            "collection_ref": forms.TextInput(
                attrs={
                    "id": "key_id",
                    "required": False,
                    "placeholder": "Collection Ref",
                    "class": "record-input",  # add a reusable class
                },
            ),
            "camera_operator": forms.TextInput(
                attrs={
                    "id": "key_id",
                    "required": False,
                    "placeholder": "Camera Operator",
                    "class": "record-input",  # add a reusable class
                },
            ),
            "first_line": forms.TextInput(
                attrs={
                    "id": "key_id",
                    "required": False,
                    "placeholder": "First Line",
                    "class": "record-input",  # add a reusable class
                },
            ),

            "parent": forms.TextInput(
                attrs={
                    "id": "key_id",
                    "required": False,
                    "placeholder": "Parent",
                    "class": "record-input",  # add a reusable class
                },
            ),
            "instrument": forms.TextInput(
                attrs={
                    "id": "key_id",
                    "required": False,
                    "placeholder": "Instrument",
                    "class": "record-input",  # add a reusable class
                },
            ),
            "catalogue_name": forms.TextInput(
                attrs={
                    "id": "key_id",
                    "required": False,
                    "placeholder": "Catalogue Name",
                    "class": "record-input",  # add a reusable class
                },
            ),
            "fieldworker": forms.TextInput(
                attrs={
                    "id": "key_id",
                    "required": False,
                    "placeholder": "Fieldworker",
                    "class": "record-input",  # add a reusable class
                },
            ),
            "date": forms.TextInput(
                attrs={
                    "id": "key_id",
                    "required": False,
                    "placeholder": "Date",
                    "class": "record-input",  # add a reusable class
                },
            ),
            "informant_artist": forms.TextInput(
                attrs={
                    "id": "key_id",
                    "required": False,
                    "placeholder": "Informant Artist",
                    "class": "record-input",  # add a reusable class
                },
            ),
            "native_area_county": forms.TextInput(
                attrs={
                    "id": "key_id",
                    "required": False,
                    "placeholder": "Native Area County",
                    "class": "record-input",  # add a reusable class
                },
            ),
            "comments": forms.TextInput(
                attrs={
                    "id": "key_id",
                    "required": False,
                    "placeholder": "Comments",
                    "class": "record-input",  # add a reusable class
                },
            ),
            "place_recorded": forms.TextInput(
                attrs={
                    "id": "key_id",
                    "required": False,
                    "placeholder": "Place Recorded",
                    "class": "record-input",  # add a reusable class
                },
            ),
            "type_of_material": forms.TextInput(
                attrs={
                    "id": "key_id",
                    "required": False,
                    "placeholder": "Type of Material",
                    "class": "record-input",  # add a reusable class
                },
            ),
            "summary": forms.TextInput(
                attrs={
                    "id": "key_id",
                    "required": False,
                    "placeholder": "Summary",
                    "class": "record-input",  # add a reusable class
                },
            ),
            "disc_matrix_number": forms.TextInput(
                attrs={
                    "id": "key_id",
                    "required": False,
                    "placeholder": "Disc Matrix Number",
                    "class": "record-input",  # add a reusable class
                },
            ),
            "tale_reference": forms.TextInput(
                attrs={
                    "id": "key_id",
                    "required": False,
                    "placeholder": "Tale Reference",
                    "class": "record-input",  # add a reusable class
                },
            ),
            'restricted': forms.Select(attrs={

                "class": "record-input",  # add a reusable class
            }),

        }

    def __init__(self, *args, **kwargs):
        super(AlstForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False
