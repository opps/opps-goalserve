# coding: utf-8

from django import forms
from .models import TEAM_STATUS, PLAYER_STATUS

class LineupAddForm(forms.Form):

    POSITION = (
        ("Midfielder", "Midfielder"),
        ("Attacker", "Attacker"),
        ("Goalkeeper", "Goalkeeper"),
    )
    
    match_id = forms.CharField(required=True)
    team_id = forms.CharField(required=True)
    team_status = forms.ChoiceField(required=True, choices=TEAM_STATUS)
    player_name = forms.CharField(required=True)
    player_number = forms.CharField(required=True)
    player_position = forms.ChoiceField(required=True, choices=POSITION)
    player_status = forms.ChoiceField(required=True, choices=PLAYER_STATUS)

    #def clean(self):
    #    data = self.cleaned_data
    #    print "cleaning"