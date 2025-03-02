from django import forms;

#会員登録ページForm
class MemberForm(forms.Form):
    name=forms.CharField(label="氏名"
                         ,widget=forms.TextInput(attrs={'class':"form-control"}));
    address=forms.CharField(label="住所"
                        ,widget=forms.TextInput(attrs={'class':"form-control"}));
    phone=forms.CharField(label="電話番号"
                          ,widget=forms.TextInput(attrs={'class':"form-control"}));
    age=forms.IntegerField(label="年齢"
                           ,widget=forms.TextInput(attrs={'class':"form-control"}));
    