"""Forms of the project."""
from django import forms
from django.core.validators import MinValueValidator, MaxValueValidator
from things.models import Thing
# Create your forms here.

class PostForm(forms.Form):

    name = forms.CharField(max_length=35)
    description = forms.CharField(max_length=120)
    quantity = forms.IntegerField(
        validators=[MinValueValidator(0),MaxValueValidator(50)]
    )
#
    class Meta:
        fields=(

            "name",
            "description",
            "quantity",
        )

    def save(self, commit=True):


        user1 = Thing.objects.create_user(
        name = self.cleaned_data.get('name'),
        description = self.cleaned_data.get('description'),
        quantity = self.cleaned_data.get('quantity'),
        )

        return user1