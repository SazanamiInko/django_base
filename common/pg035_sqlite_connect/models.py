from django.db import models

#固定長
class FixedCharField(models.CharField):
    def db_type(self, connection):
        return f'char({self.max_length})'

#得点モデル
class Score(models.Model):
    employ_no=FixedCharField(max_length=6,primary_key=True);
    score=models.IntegerField();

    def __str__(self):
        return f"{self.employ_no} - {self.score}"

    class Meta:
        db_table = 'score'  # テーブル名を 'score' に指定
# Create your models here.
