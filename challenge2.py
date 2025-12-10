player = 1
nums=[]
ties = 0

player_count = int(input("Enter the number of players: "))
matches_played = int(input("Enter the amount of matches played: "))

while player <= player_count:
    nums.append(int(input(f"Enter a score for Player #{player}: ")))
    player += 1

for i in nums:
    if (i % 42) % 10 == 0:
        ties += (i % 42)/10
answer = ties/2

print(answer)