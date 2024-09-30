from django import forms
from .models import Booking

FAVORITE_DISH = [("italian", "Italian"), ("greek", "Greek"), ("turkish", "Turkish")]
SHIFTS = (("1", "Morning"), ("2", "Afternoon"), ("3", "Evening"))


class DemoForm(forms.Form):
    name = forms.CharField(widget=forms.Textarea)
    email = forms.EmailField()
    fav_dish = forms.ChoiceField(choices=FAVORITE_DISH)


class InputForm(forms.Form):
    first_name = forms.CharField(max_length=200, required=False)
    last_name = forms.CharField(max_length=200)
    shift = forms.ChoiceField(choices=SHIFTS)
    time_log = forms.TimeField(help_text="Enter the exact time")


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = "__all__"
