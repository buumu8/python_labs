from django import forms

FAVORITE_DISH = [("italian", "Italian"), ("greek", "Greek"), ("turkish", "Turkish")]


class DemoForm(forms.Form):
    name = forms.CharField(widget=forms.Textarea)
    email = forms.EmailField()
    fav_dish = forms.ChoiceField(choices=FAVORITE_DISH)
