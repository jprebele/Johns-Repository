# John Rebeles
# PSID: 2039426
class Team:
    def __int__(self):
        self.team_name = 'none'
        self.team_wins = 0
        self.team_losses = 0

    def get_win_percentage(self):
        return self.team_wins / (self.team_wins + self.team_losses)


if __name__ == "__main__":

    student_team = Team()
    student_team.team_name = input()
    student_team.team_wins = float(input())
    student_team.team_losses = int(input())

    if student_team.get_win_percentage() >= .5000:
        print(f'Congratulations, Team {student_team.team_name} has a winning average!')
    else:
        print(f'Team {student_team.team_name} has a losing average.')
