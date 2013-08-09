# -*- coding: utf-8 -*-
from django.contrib import admin
import opps.goalserve.models

classes = "Country Category Stadium Team Player Match MatchStats MatchLineUp MatchSubstitutions MatchCommentary MatchEvent MatchResult F1Tournament F1Race F1Team Driver F1Results F1Commentary MatchStandings".split()

for model in classes:
    admin.site.register(
        getattr(opps.goalserve.models, model)
    )