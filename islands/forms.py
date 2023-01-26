from django import forms
from islands import models

class IslandForm(forms.ModelForm):
    photos = forms.FileField(
        widget=forms.ClearableFileInput(attrs={"multiple": True}),
    )
    class Meta:
        model = models.Island
        fields = ["name","photos"]
