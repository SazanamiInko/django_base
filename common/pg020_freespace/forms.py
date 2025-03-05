from django import forms;

#会員登録ページForm
class QuestionnaireForm(forms.Form):
    userbility=forms.IntegerField(label="利便性");
    price=forms.IntegerField(label="値段");
    desighn=forms.IntegerField(label="デザイン");
    opinion=forms.CharField(label="ご意見",required=False);
        
class AnswerForm(forms.Form):
    userbility=forms.CharField(label="利便性",disabled=True);
    price=forms.CharField(label="値段",disabled=True);
    desighn=forms.CharField(label="デザイン",disabled=True);
    opinion=forms.CharField(label="ご意見",required=False,disabled=True);
    