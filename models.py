from django.db import models
import time

class AthResults(models.Model):
    id = models.IntegerField(primary_key=True, blank=True)
    name = models.TextField(db_column='Name', blank=True)
    school = models.TextField(db_column='School', blank=True)
    event = models.TextField(db_column='Event', blank=True)
    sex = models.TextField(db_column='Sex', blank=True)
    result = models.FloatField(db_column='Result', blank=True, null=True)
    date = models.TextField(db_column='Date', blank=True)
    is_track = models.IntegerField(db_column='IsTrack', blank=True, null=True)

    def display_result(self):
        if self.is_track:
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


        

        
