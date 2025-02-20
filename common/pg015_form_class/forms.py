from django import forms;

#会員登録ページForm
class MemberForm(forms.Form):
    name=forms.CharField(label="name");
    age=forms.IntegerField(label="age");
    