from django import forms


class AddressSearch(forms.Form):
    search = forms.CharField(label='Адрес')
    radius = forms.FloatField(label='Введите радиус поиска (в км)')
