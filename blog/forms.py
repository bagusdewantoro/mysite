from django import forms

class EmailKontenForm(forms.Form):
    nama = forms.CharField(max_length=25)
    email_pengirim = forms.EmailField()
    email_penerima = forms.EmailField()
    catatan = forms.CharField(required=False,
                            widget=forms.Textarea)
