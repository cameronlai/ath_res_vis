from django.db import models

class AthResults(models.Model):
    id = models.IntegerField(primary_key=True, blank=True)  # AutoField?
    name = models.TextField(db_column='Name', blank=True)  # Field name made lowercase.
    school = models.TextField(db_column='School', blank=True)  # Field name made lowercase.
    event = models.TextField(db_column='Event', blank=True)  # Field name made lowercase.
    sex = models.TextField(db_column='Sex', blank=True)  # Field name made lowercase.
    result = models.FloatField(db_column='Result', blank=True, null=True)  # Field name made lowercase.
    date = models.TextField(db_column='Date', blank=True)  # Field name made lowercase. This field type is a guess.
    track = models.IntegerField(db_column='Track', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ath_results'
