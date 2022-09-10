from dataclasses import fields
from django import forms
from books.models import Materials


class MaterialForm(forms.ModelForm):
    class Meta:
        model = Materials
        fields = {'lecturer', 'course_code', 'course_title', 'year', 'material_type', 'level', 'department', 'efile'}
