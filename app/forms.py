from django.forms import ModelForm
from app.models import Rider

# Create the form class.
class RiderForm(ModelForm):
    class Meta:
        model = Rider
        fields = ['nome', 'tema', 'ano']