from django import forms;

#会員登録ページForm
class MemberForm(forms.Form):
    kinds={(1,'一般'),(2,'学生')};
    
    name=forms.CharField(label="氏名"
                         ,widget=forms.TextInput(attrs={'class':"form-control"}));
   
    kind=forms.ChoiceField(label="会員種別", choices=kinds, required=False)
    address=forms.CharField(label="住所"
                        ,widget=forms.TextInput(attrs={'class':"form-control"}));
    phone=forms.CharField(label="電話番号"
                         ,widget=forms.TextInput(attrs={'class':"form-control",
                                                        'pattern':'[0-9]+',
                                                         'title': '半角数字のみ入力してください'}));
    age=forms.IntegerField(label="年齢");
    

    