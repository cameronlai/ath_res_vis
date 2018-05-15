from django.db import models
import time



class AthResults(models.Model):
    id = models.IntegerField(primary_key=True, blank=True)  # AutoField?
    name = models.TextField(db_column='Name', blank=True)  # Field name made lowercase.
    school = models.TextField(db_column='School', blank=True)  # Field name made lowercase.
    event = models.TextField(db_column='Event', blank=True)  # Field name made lowercase.
    sex = models.TextField(db_column='Sex', blank=True)  # Field name made lowercase.
    result = models.FloatField(db_column='Result', blank=True, null=True)  # Field name made lowercase.
    date = models.TextField(db_column='Date', blank=True)  # Field name made lowercase. This field type is a guess.
    track = models.IntegerField(db_column='Track', blank=True, null=True)  # Field name made lowercase.

    def display_result(self):
        if self.track:
            m, s = divmod(self.result, 60)
            h, m = divmod(m, 60)
            if h > 0:
                ret = r'%d:%d:%.2f' % (h, m, s)
            elif m > 0:
                ret = r'%d:%.2f' % (m, s)
            else:
                ret = r'%.2f' % (s)
            return ret + 's'
        else:
            return str(self.result) + 'm'

    class Meta:
        managed = False
        db_table = 'ath_results'


        

        
