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

    def get_list(self, school_choice, sex_choice, event_choice):
        if school_choice: # Valid school name
            school_athlete_list = self.objects.filter(school=school_choice).order_by('name')
        else:
            school_athlete_list = self.objects.none()

        sex_list = school_athlete_list.order_by('-sex').values_list('sex', flat=True).distinct()    
        event_list = school_athlete_list.order_by('event').values_list('event', flat=True).distinct()

        # Get back name list
        if len(sex_list) > 0 and not sex_choice in sex_list:
            sex_choice = sex_list[0]

        if len(event_list) > 0 and not event_choice in event_list:
            event_choice = event_list[0]

        if sex_choice and event_choice:
            athlete_list = self.objects.filter(school=school_choice, event=event_choice, sex=sex_choice).order_by('name')
        else:
            athlete_list = self.objects.none()

        name_list = athlete_list.values_list('name', flat=True).distinct()

        return sex_list, event_list, name_list
        

