from django import forms;

#身体測定ページForm
class MesureForm(forms.Form):

    weight=forms.FloatField(label="体重");
    tall=forms.FloatField(label="身長");

    