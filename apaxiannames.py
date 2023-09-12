community_name = input()
n = int(input())
names = [input() for _ in range(n)]

princess_count = 0
baron_count = 0
priest_count = 0
commoner_count = 0

for name in names:
    if community_name in name:
        if name.startswith(community_name):
            princess_count += 1
        elif name.endswith(community_name):
            baron_count += 1
        else:
            priest_count += 1
    else:
        commoner_count += 1

print(f"{princess_count} PRINCESS")
print(f"{baron_count} BARON")
print(f"{priest_count} PRIEST")
print(f"{commoner_count} COMMONER")
