from django import forms;

#連絡先ページForm
class ContactForm(forms.Form):

    name=forms.CharField(label="法人名"
                         ,widget=forms.TextInput(attrs={'class':"form-control"}));
    address=forms.CharField(label="住所"
                        ,widget=forms.TextInput(attrs={'class':"form-control"}));
    phone=forms.CharField(label="電話番号"
                          ,max_length=11
                          ,widget=forms.TextInput(attrs={'class':"form-control"}));
    url=forms.URLField(label="URL", required=False);
    email=forms.EmailField();


    