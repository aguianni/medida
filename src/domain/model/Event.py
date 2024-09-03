class Event:
    def __init__(self, eventId: str, eventDate: str, eventTime: str, homeTeamId: str, homeTeamNickName: str,
                 homeTeamCity: str, homeTeamRank: str, homeTeamRankPoints: str, awayTeamId: str,
                 awayTeamNickName: str, awayTeamCity: str, awayTeamRank: str, awayTeamRankPoints: str):
        self.eventId = eventId
        self.eventDate = eventDate
        self.eventTime = eventTime
        self.homeTeamId = homeTeamId
        self.homeTeamNickName = homeTeamNickName
        self.homeTeamCity = homeTeamCity
        self.homeTeamRank = homeTeamRank
        self.homeTeamRankPoints = homeTeamRankPoints
        self.awayTeamId = awayTeamId
        self.awayTeamNickName = awayTeamNickName
        self.awayTeamCity = awayTeamCity
        self.awayTeamRank = awayTeamRank
        self.awayTeamRankPoints = awayTeamRankPoints
