"""
One of the things that programming competition organizers have to do is decide which team should be in which room. There are 
 rooms and 
 teams. The rooms are similar in size, so it is best for teams to be divided into rooms as evenly as possible. For example, if there are 
 rooms and 
 teams, then it is best to put 
 teams in one room, 
 teams in another room, and then the last 
 teams in the last room.

Input
The input consists of two lines. On the first line is an integer 
, and on the second line is an integer 
.

Output
The output should contain 
 lines, one for each room. If 
 teams are to be in room number 
, then line 
 should contain 
 copies of the * symbol.

Explanation of sample cases
The first sample is 
 rooms and 
 teams. Since there is only one room, all the teams are in that room.

The second sample is the same as the one taken above.

In the third sample, there are 
 lounges and 
 teams. Here it is best to put 
 teams in two of the rooms, and 
 teams in the other three rooms. Here we also see that order does not matter.

Scoring
Your solution will be tested on different input data, which is divided into groups as shown in the table below. The solution will then receive points depending on which groups are solved.


Notes: Evenly distribute the teams then distribute the rest into any room
"""
def main():
    rooms = int(input())
    teams = int(input())

    teams_room = [0] * rooms
    max_teams = teams // rooms
    used_rooms = 0
    a_teams = 0

    # Evenly distribute
    while used_rooms < rooms:
        teams_room[used_rooms] += max_teams
        a_teams += max_teams
        used_rooms += 1

    # Distribute the rest
    team_left = teams - a_teams
    while team_left > 0:
        teams_room[team_left] += 1
        team_left -= 1

    for team in teams_room:
        print('*' * team)

if __name__ == "__main__":
    main()