from django.db import models

#店舗モデル
class Shop (models.Model):
    id=models.IntegerField(primary_key=True);
    name=models.CharField(max_length=255);
    isCity=models.BooleanField();
    class Meta:
        db_table = 'm_shop' 
# Create your models here.
