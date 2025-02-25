from django import forms;

#会員登録ページForm
class MemberForm(forms.Form):
    name=forms.CharField(label="氏名");
    address=forms.CharField(label="住所");
    phone=forms.CharField(label="電話番号");
    age=forms.IntegerField(label="年齢");
    