from django import forms;

#会員登録ページForm
class MemberForm(forms.Form):
    name=forms.CharField(label="氏名"
                         ,widget=forms.TextInput(attrs={'class':"form-control"}));
    address=forms.CharField(label="住所"
                        ,widget=forms.TextInput(attrs={'class':"form-control"}));
    phone=forms.CharField(label="電話番号"
                         ,widget=forms.TextInput(attrs={'class':"form-control",
                                                        'pattern':'[0-9]+',
                                                         'title': '半角数字のみ入力してください'}));
    age=forms.IntegerField(label="年齢");
    apply=forms.NullBooleanField(label="プール使いたい?",required=False);


    