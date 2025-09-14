from django import forms


class SearchForm(forms.Form):
    q = forms.CharField(required=False, max_length=100, strip=True)

    def clean_q(self):
        data = self.cleaned_data["q"]
        if "<" in data or ">" in data:
            raise forms.ValidationError("Invalid characters.")
        return data


class ExampleForm(forms.Form):
    """
    Simple example form for Task 2 (security best practices).
    Used in templates/bookshelf/form_example.html.
    """
    title = forms.CharField(max_length=200)
    author = forms.CharField(max_length=200)
