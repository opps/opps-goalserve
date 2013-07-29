# -*- coding: utf-8 -*-


class BaseAPI(object):

    def __init__(self):
        pass


class SoccerSchedule(BaseAPI):

    def __init__(self, league=None):
        super(SoccerSchedule, self).__init__()
        self.league = league


class SoccerNew(BaseAPI):

    def __init__(self):
        super(SoccerNew, self).__init__()


class SoccerHighlights(BaseAPI):

    def __init__(self):
        super(SoccerHighlights, self).__init__()


class SoccerStandings(BaseAPI):

    def __init__(self):
        super(SoccerStandings, self).__init__()


class SoccerCommentaries(BaseAPI):

    def __init__(self):
        super(SoccerCommentaries, self).__init__()


class SoccerFixtures(BaseAPI):

    def __init__(self):
        super(SoccerFixtures, self).__init__()


class SoccerHistory(BaseAPI):

    def __init__(self):
        super(SoccerHistory, self).__init__()


class SoccerTopscores(BaseAPI):

    def __init__(self):
        super(SoccerTopscores, self).__init__()


class SoccerStats(BaseAPI):
    '''stats for team or player
    :type: team or player
    :id: team or player id

    '''
    def __init__(self, type='team', id=None):
        super(SoccerStats, self).__init__()
        self.type = type
        self.id = id


class SoccerTeam(object):

    def __init__(self, team_id):
        self.team_id = team_id


class SoccerPlayer(object):

    def __init__(self):
        self.player_id = player_id


class SoccerH2H(BaseAPI):

    def __init__(self, a_team, b_team):
        super(SoccerH2H, self).__init__()
        self.a_team = a_team
        self.b_team = b_team



class F1Results(BaseAPI):

    def __init__(self):
        super(F1Results, self).__init__()


class F1Drivers(BaseAPI):

    def __init__(self):
        super(F1Drivers, self).__init__()


class F1Schedule(BaseAPI):

    def __init__(self):
        super(F1Schedule, self).__init__()


class F1Live(BaseAPI):

    def __init__(self):
        super(F1Live, self).__init__()


class F1Teams(BaseAPI):

    def __init__(self):
        super(F1Teams, self).__init__()


class F1Team(object):

    def __init__(self):
        pass


class F1Driver(object):

    def __init__(self):
        pass

