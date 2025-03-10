from django import forms;

#身体測定ページForm
class CheckOutForm(forms.Form):

    Date=forms.DateField(label="日付",widget=forms.DateInput(attrs={'class':'form-control','type': 'date'}));
    Time=forms.TimeField(label="時間",widget=forms.DateInput(attrs={'class':'form-control','type': 'time'}));


    