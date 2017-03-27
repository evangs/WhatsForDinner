from django import forms

PRICE_LEVELS = (
        (0, 'Free'),
        (1, 'Cheap'),
        (2, 'Moderate'),
        (3, 'Expensive'),
        (4, 'Fancy'),
)

RATINGS = (
        (1, 'One Star'),
        (2, 'Two Stars'),
        (3, 'Three Stars'),
        (4, 'Four Stars'),
        (5, 'Five Stars'),
)

class PreferenceForm(forms.Form):
    price_level = forms.ChoiceField(choices=PRICE_LEVELS, initial=2)
    minimum_rating = forms.ChoiceField(choices=RATINGS, initial=4)
    keyword = forms.CharField(required=False)
    latitude = forms.DecimalField(widget=forms.HiddenInput())
    longitude = forms.DecimalField(widget=forms.HiddenInput())