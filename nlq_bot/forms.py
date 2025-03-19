from django import forms

class QueryForm(forms.Form):
    question = forms.CharField(label="Enter your query about the database", max_length=500)
