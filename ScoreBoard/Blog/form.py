from django import forms

from Blog.models import Player

from Blog.models import Team, Player, Match, Score


class TeamForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(TeamForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field_name== 'name':
                self.fields['name'].required=False
            if field.widget.attrs.get('class'):
                field.widget.attrs['class'] += ' form-control'
            else:
                field.widget.attrs['class'] = 'form-control'
    class Meta:
        model=Team
        fields=('name','logo_url','club_state')

class PlayersForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PlayersForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():

            if field.widget.attrs.get('class'):
                field.widget.attrs['class'] += ' form-control'
            else:
                field.widget.attrs['class'] = 'form-control'
    class Meta:
        model=Player
        fields=('first_name','last_name','player_image','player_jersy_number','country','team')

class MatchFixForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(MatchFixForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():

            if field.widget.attrs.get('class'):
                field.widget.attrs['class'] += ' form-control'
            else:
                field.widget.attrs['class'] = 'form-control'
    class Meta:
        model=Match
        fields="__all__"

class ScoreBoardForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ScoreBoardForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():

            if field.widget.attrs.get('class'):
                field.widget.attrs['class'] += ' form-control'
            else:
                field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Score
        fields = "__all__"