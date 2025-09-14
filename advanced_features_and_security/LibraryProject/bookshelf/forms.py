from django import forms

class SearchForm(forms.Form):
    q = forms.CharField(required=False, max_length=100, strip=True)

    def clean_q(self):
        data = self.cleaned_data["q"]
        if "<" in data or ">" in data:
            raise forms.ValidationError("Invalid characters.")
        return data
