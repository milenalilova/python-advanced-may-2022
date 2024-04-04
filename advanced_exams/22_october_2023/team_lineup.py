def team_lineup(*args):
    team_dict = {}
    for arg in args:
        name, country = arg
        if country not in team_dict:
            team_dict[country] = []
        team_dict[country].append(name)

    team_dict = dict(sorted(team_dict.items(), key=lambda x: (-len(x[1]), (x[0]))))

    output = ''
    for country, names in team_dict.items():
        output += f"{country}:\n"
        for name in names:
            output += f"  -{name}\n"

    return output.strip()


print(team_lineup(
    ("Harry Kane", "England"),
    ("Manuel Neuer", "Germany"),
    ("Raheem Sterling", "England"),
    ("Toni Kroos", "Germany"),
    ("Cristiano Ronaldo", "Portugal"),
    ("Thomas Muller", "Germany")))

print()

print(team_lineup(
    ("Lionel Messi", "Argentina"),
    ("Neymar", "Brazil"),
    ("Cristiano Ronaldo", "Portugal"),
    ("Harry Kane", "England"),
    ("Kylian Mbappe", "France"),
    ("Raheem Sterling", "England")))

print()

print(team_lineup(
    ("Harry Kane", "England"),
    ("Manuel Neuer", "Germany"),
    ("Raheem Sterling", "England"),
    ("Toni Kroos", "Germany"),
    ("Cristiano Ronaldo", "Portugal"),
    ("Thomas Muller", "Germany"),
    ("Bruno Fernandes", "Portugal"),
    ("Bernardo Silva", "Portugal"),
    ("Harry Maguire", "England")))
