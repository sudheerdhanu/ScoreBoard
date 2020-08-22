from datetime import datetime

from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class Team(models.Model):
    identifier=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=50)
    logo_url=models.ImageField(upload_to='images/team')
    club_state=models.CharField(max_length=70)
    points=models.IntegerField(null=True)

    class Meta:
        db_table = "team"
    def __str__(self):
        return self.name


class Player(models.Model):
    identifier = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=50, null=False)
    last_name = models.CharField(max_length=50, null=False)
    player_image = models.ImageField(upload_to='images/players')
    player_jersy_number=models.IntegerField()
    country=models.CharField(max_length=40)
    team = models.ForeignKey('Team', on_delete=models.CASCADE, related_name='team',default = 0)

    class Meta:
        db_table = "player"

    def __str__(self):
        return self.first_name

class Match(models.Model):
    Bat_Bowl =(('Bat', 'Bat'), ('Bat', 'Bowl'))


    date = models.DateTimeField(default=datetime.now, blank= False)
    Team1 = models.ForeignKey('Team', on_delete=models.CASCADE, related_name='team1',default = 0)
    Team2 = models.ForeignKey('Team', on_delete=models.CASCADE, related_name='team2',default = 0)
    Team1logo= models.ImageField(upload_to='images/match', verbose_name = 'Team1 logo',default = 0)
    Team2logo= models.ImageField(upload_to='images/match', verbose_name ='Team2 logo',default =0)
    League = models.CharField(max_length=100, default = 0)
    Toss_won_by =  models.ForeignKey('Team', on_delete=models.CASCADE, related_name='tosswon',default = 0)
    Elected_to = models.CharField(max_length=100,choices=Bat_Bowl)

    class Meta:
        db_table = "match"

    def __str__(self):
        return str(self.Team1) + '  vs  ' + str(self.Team2) + ' Dated on ' + str(self.date.date())


    def toss_won(self):
        return 'Toss Won by ' + str(self.Toss_won_by) + ' and elected to ' +  str(self.Elected_to) + ' first'

class Player_history(models.Model):
    player=models.OneToOneField('Player',on_delete=models.CASCADE)
    matches=models.IntegerField()
    run=models.IntegerField()
    highest_score=models.IntegerField()
    fifties=models.IntegerField()
    hundreds=models.IntegerField()

    class Meta:
        db_table = "player_history"


class Score(models.Model):

    matches_between = models.ForeignKey('Match',on_delete = models.CASCADE, related_name ='fixture_between')
    Team1 = models.ForeignKey('Team', on_delete=models.CASCADE, related_name='teamA',default = 0)
    Team2 = models.ForeignKey('Team', on_delete=models.CASCADE, related_name='teamB',default = 0)
    team1Score = models.IntegerField(default = 0)
    team2Score = models.IntegerField(default = 0)

    class Meta:
        db_table = "score"

    def runs_gap(self):
        if self.team1Score > self.team2Score:
            return str(self.Team1) + ' won by ' +  str(self.team1Score - self.team2Score) + ' runs '
        else:
            return str(self.Team2) + ' won by ' + str(self.team2Score - self.team1Score) + ' runs '



    def __str__(self):
        if self.team1Score > self.team2Score:
           return str(self.Team1)
        else:
            return str(self.Team2)


