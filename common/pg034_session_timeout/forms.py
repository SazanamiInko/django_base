from django import forms;

#会員登録ページForm
class MemberForm(forms.Form):
    kinds={(1,'一般'),(2,'学生')};
    
    sexes={(1,'男性'),(2,'女性')};
    pg034_name=forms.CharField(label="氏名"
                         ,widget=forms.TextInput(attrs={'class':"form-control"}));
   
    pg034_kind=forms.ChoiceField(label="会員種別", choices=kinds, required=False)
    pg034_address=forms.CharField(label="住所"
                        ,widget=forms.TextInput(attrs={'class':"form-control"}));
    pg034_phone=forms.CharField(label="電話番号"
                         ,widget=forms.TextInput(attrs={'class':"form-control",
                                                        'pattern':'[0-9]+',
                                                         'title': '半角数字のみ入力してください'}));
    pg034_age=forms.IntegerField(label="年齢");
    pg034_sex=forms.ChoiceField(label="性別",choices=sexes,widget=forms.RadioSelect);
    

#セッションタイムアウト設定Form
class SessionTimeOutSettingForm(forms.Form):
    pg034_timeout_setting=forms.CharField(label="タイムアウト時間(秒)"
                         ,widget=forms.TextInput(attrs={'class':"form-control",
                                                        'pattern':'[0-9]+',
                                                         'title': '半角数字のみ入力してください'}));

    