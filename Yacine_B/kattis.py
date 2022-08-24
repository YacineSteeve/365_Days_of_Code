victory_cards = {
    "Province": {"Cost": 8, "VP_worth": 6},
    "Duchy": {"Cost": 5, "VP_worth": 3},
    "Estate": {"Cost": 2, "VP_worth": 1}
}

treasure_cards = {
    "Gold": {"Cost": 6, "BP_worth": 3},
    "Silver": {"Cost": 3, "BP_worth": 2},
    "Copper": {"Cost": 0, "BP_worth": 1}
}

g, s, c = map(int, input().split())

buying_points = (g * treasure_cards["Gold"]["BP_worth"]) + \
                (s * treasure_cards["Silver"]["BP_worth"]) + \
                (c * treasure_cards["Copper"]["BP_worth"])

best = ""

for card in ["Province", "Duchy", "Estate"]:
    num, remainder = divmod(buying_points, victory_cards[card]["Cost"])
    if num > 0:
        best += f"{card} or "
        break
    buying_points = remainder

for card in ["Gold", "Silver"]:
    num, remainder = divmod(buying_points, treasure_cards[card]["Cost"])
    if num > 0:
        best += card
        break
    buying_points = remainder
    if card == "Silver":
        best += "Copper"

print(best)
