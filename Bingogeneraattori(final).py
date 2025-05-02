import random
import json

def parse_goals(goal_list):
    categories = {}
    for line in goal_list.strip().split("\n"):
        parts = line.rsplit("\t", 2)
        if len(parts) == 3:
            goal, game, category = parts
            if category not in categories:
                categories[category] = []
            categories[category].append({"name": f"{goal} [{game}]"})
    return categories

def generate_bingo_card(categories):
    selected_goals = set()
    category_numbers = sorted(categories.keys(), key=int)  # Sort categories numerically

    # Use only the first 21 categories (Normal mode)
    category_numbers = category_numbers[:21]

    used_categories = []

    # Pick one goal from each selected category
    for category in category_numbers:
        available_goals = [goal for goal in categories[category] if goal["name"] not in selected_goals]
        if available_goals:
            chosen_goal = random.choice(available_goals)
            selected_goals.add(chosen_goal["name"])
            used_categories.append(category)

    # Fill remaining slots up to 25
    extra_needed = 25 - len(selected_goals)
    while extra_needed > 0:
        random_category = random.choice(used_categories)
        available_goals = [goal for goal in categories[random_category] if goal["name"] not in selected_goals]
        if available_goals:
            chosen_goal = random.choice(available_goals)
            selected_goals.add(chosen_goal["name"])
            extra_needed -= 1

    bingo_card = [{"name": goal} for goal in selected_goals]
    random.shuffle(bingo_card)
    return bingo_card

def print_bingo_card(bingo_card):
    bingo_json = json.dumps({"bingo_card": bingo_card}, indent=4)
    print(bingo_json)

goals_text = """40 lines	Elektronika 60	1
3000 points	Elektronika 60	1
3000 points	ASoft	2
40 lines	ASoft	2
40 lines (Hide Next)	ASoft	2
Win a Game - Level 5	Igo: Kyuu Roban Taikyoku	3
Win a Game - Level 1	Igo: Kyuu Roban Taikyoku	3
Win a Game - Level 2	Igo: Kyuu Roban Taikyoku	3
Win a Game - Level 3	Igo: Kyuu Roban Taikyoku	3
Win a Game - Level 4	Igo: Kyuu Roban Taikyoku	3
Win a Game - Level 6	Igo: Kyuu Roban Taikyoku	3
40 lines (Phantom)	ASoft v 3.12	4
40 lines (Normal)	ASoft v 3.12	4
3000 points (Phantom)	ASoft v 3.12	4
3000 points (Normal)	ASoft v 3.12	4
40 lines (Hide NEXT)	ASoft v 3.12	4
40 lines (Height 10)	ASoft v 3.12	4
3000 points (Hide NEXT)	ASoft v 3.12	4
3000 points (Height 10)	ASoft v 3.12	4
40 lines (Level 9)	ASoft v 3.12	4
3000 points (Level 9)	ASoft v 3.12	4
3 T-Spins	ASoft v 3.12	4
40 lines	Spectrum HoloByte	5
3000 points	Spectrum HoloByte	5
40 lines (Height 10)	Spectrum HoloByte	5
3000 points (Height 10)	Spectrum HoloByte	5
40 lines (Hide NEXT)	Spectrum HoloByte	5
3000 points (Hide NEXT)	Spectrum HoloByte	5
3 T-Spins	Spectrum HoloByte	5
40 lines	Apple II	6
3000 points	Apple II	6
40 lines (Height 10)	Apple II	6
3000 points (Height 10)	Apple II	6
3 T-Spins	Apple II	6
40-lines	Famicom	7
Stage 0	Famicom	7
Stage 0, Round 3	Famicom	7
Stage 1	Famicom	7
Stage 2	Famicom	7
Stage 3	Famicom	7
Stage 0, Round 5	Famicom	7
3000 points (Level 1)	Welltris	8
3000 points (Level 2)	Welltris	8
3000 points (Level 3)	Welltris	8
Shop 0, Stage 0	Hatris (Famicom)	9
Shop 0, Stage 1	Hatris (Famicom)	9
Shop 0, Stage 2	Hatris (Famicom)	9
Shop 0, Stage 3	Hatris (Famicom)	9
Shop 0, Stage 4	Hatris (Famicom)	9
Shop 0, Stage 5	Hatris (Famicom)	9
Shop 0, Stage 6	Hatris (Famicom)	9
Shop 0, Stage 7	Hatris (Famicom)	9
Shop 0, Stage 8	Hatris (Famicom)	9
Shop 0, Stage 9	Hatris (Famicom)	9
Shop 1, Stage 0	Hatris (Famicom)	9
Shop 1, Stage 1	Hatris (Famicom)	9
Shop 1, Stage 2	Hatris (Famicom)	9
Shop 1, Stage 3	Hatris (Famicom)	9
Shop 1, Stage 4	Hatris (Famicom)	9
Shop 1, Stage 5	Hatris (Famicom)	9
Shop 1, Stage 6	Hatris (Famicom)	9
Shop 1, Stage 7	Hatris (Famicom)	9
Shop 1, Stage 8	Hatris (Famicom)	9
Shop 1, Stage 9	Hatris (Famicom)	9
Shop 2, Stage 0	Hatris (Famicom)	9
Shop 2, Stage 1	Hatris (Famicom)	9
Shop 2, Stage 2	Hatris (Famicom)	9
Shop 2, Stage 3	Hatris (Famicom)	9
Shop 2, Stage 4	Hatris (Famicom)	9
Shop 2, Stage 5	Hatris (Famicom)	9
Shop 2, Stage 6	Hatris (Famicom)	9
Shop 2, Stage 7	Hatris (Famicom)	9
Shop 2, Stage 8	Hatris (Famicom)	9
Shop 2, Stage 9	Hatris (Famicom)	9
Shop 3, Stage 0	Hatris (Famicom)	9
Shop 3, Stage 1	Hatris (Famicom)	9
Shop 3, Stage 2	Hatris (Famicom)	9
Shop 3, Stage 3	Hatris (Famicom)	9
Shop 3, Stage 4	Hatris (Famicom)	9
Shop 3, Stage 5	Hatris (Famicom)	9
Shop 3, Stage 6	Hatris (Famicom)	9
Shop 3, Stage 7	Hatris (Famicom)	9
Shop 3, Stage 8	Hatris (Famicom)	9
Shop 3, Stage 9	Hatris (Famicom)	9
Shop  4, Stage 0	Hatris (Famicom)	9
Shop  4, Stage 1	Hatris (Famicom)	9
Shop  4, Stage 2	Hatris (Famicom)	9
Shop  4, Stage 3	Hatris (Famicom)	9
Shop  4, Stage 4	Hatris (Famicom)	9
Shop  4, Stage 5	Hatris (Famicom)	9
Shop  4, Stage 6	Hatris (Famicom)	9
Shop  4, Stage 7	Hatris (Famicom)	9
Shop  4, Stage 8	Hatris (Famicom)	9
Shop  4, Stage 9	Hatris (Famicom)	9
Shop 5, Stage 0	Hatris (Famicom)	9
Shop 5, Stage 1	Hatris (Famicom)	9
Shop 5, Stage 2	Hatris (Famicom)	9
Shop 5, Stage 3	Hatris (Famicom)	9
Shop 5, Stage 4	Hatris (Famicom)	9
Shop 5, Stage 5	Hatris (Famicom)	9
Shop 5, Stage 6	Hatris (Famicom)	9
Shop 5, Stage 7	Hatris (Famicom)	9
Shop 5, Stage 8	Hatris (Famicom)	9
Shop 5, Stage 9	Hatris (Famicom)	9
Difficulty level 2	Super Tetris	10
Difficulty level 3	Super Tetris	10
Difficulty level 4	Super Tetris	10
Difficulty level 5	Super Tetris	10
Difficulty level 6	Super Tetris	10
Difficulty level 7	Super Tetris	10
Shop 0, Stage 0	Hatris (GB)	11
Shop 0, Stage 1	Hatris (GB)	11
Shop 0, Stage 2	Hatris (GB)	11
Shop 0, Stage 3	Hatris (GB)	11
Shop 0, Stage 4	Hatris (GB)	11
Shop 0, Stage 5	Hatris (GB)	11
Shop 0, Stage 6	Hatris (GB)	11
Shop 0, Stage 7	Hatris (GB)	11
Shop 0, Stage 8	Hatris (GB)	11
Shop 0, Stage 9	Hatris (GB)	11
Shop 1, Stage 0	Hatris (GB)	11
Shop 1, Stage 1	Hatris (GB)	11
Shop 1, Stage 2	Hatris (GB)	11
Shop 1, Stage 3	Hatris (GB)	11
Shop 1, Stage 4	Hatris (GB)	11
Shop 1, Stage 5	Hatris (GB)	11
Shop 1, Stage 6	Hatris (GB)	11
Shop 1, Stage 7	Hatris (GB)	11
Shop 1, Stage 8	Hatris (GB)	11
Shop 1, Stage 9	Hatris (GB)	11
Shop 2, Stage 0	Hatris (GB)	11
Shop 2, Stage 1	Hatris (GB)	11
Shop 2, Stage 2	Hatris (GB)	11
Shop 2, Stage 3	Hatris (GB)	11
Shop 2, Stage 4	Hatris (GB)	11
Shop 2, Stage 5	Hatris (GB)	11
Shop 2, Stage 6	Hatris (GB)	11
Shop 2, Stage 7	Hatris (GB)	11
Shop 2, Stage 8	Hatris (GB)	11
Shop 2, Stage 9	Hatris (GB)	11
Shop 3, Stage 0	Hatris (GB)	11
Shop 3, Stage 1	Hatris (GB)	11
Shop 3, Stage 2	Hatris (GB)	11
Shop 3, Stage 3	Hatris (GB)	11
Shop 3, Stage 4	Hatris (GB)	11
Shop 3, Stage 5	Hatris (GB)	11
Shop 3, Stage 6	Hatris (GB)	11
Shop 3, Stage 7	Hatris (GB)	11
Shop 3, Stage 8	Hatris (GB)	11
Shop 3, Stage 9	Hatris (GB)	11
Shop  4, Stage 0	Hatris (GB)	11
Shop  4, Stage 1	Hatris (GB)	11
Shop  4, Stage 2	Hatris (GB)	11
Shop  4, Stage 3	Hatris (GB)	11
Shop  4, Stage 4	Hatris (GB)	11
Shop  4, Stage 5	Hatris (GB)	11
Shop  4, Stage 6	Hatris (GB)	11
Shop  4, Stage 7	Hatris (GB)	11
Shop  4, Stage 8	Hatris (GB)	11
Shop  4, Stage 9	Hatris (GB)	11
Shop 5, Stage 0	Hatris (GB)	11
Shop 5, Stage 1	Hatris (GB)	11
Shop 5, Stage 2	Hatris (GB)	11
Shop 5, Stage 3	Hatris (GB)	11
Shop 5, Stage 4	Hatris (GB)	11
Shop 5, Stage 5	Hatris (GB)	11
Shop 5, Stage 6	Hatris (GB)	11
Shop 5, Stage 7	Hatris (GB)	11
Shop 5, Stage 8	Hatris (GB)	11
Shop 5, Stage 9	Hatris (GB)	11
100 lines	Tetris 2 + Bombliss	12
300,000 points	Tetris 2 + Bombliss	12
B-Type Level 13 Height 5	Tetris 2 + Bombliss	12
100 Lines (C-Type)	Tetris 2 + Bombliss	12
40 Lines (C-Type, Level 20)	Tetris 2 + Bombliss	12
Level 0 (Puzzle)	Tetris 2 + Bombliss	12
Contest 1-10	Tetris 2 + Bombliss	12
100 Lines	Tetris 2 + Bombliss	12
Shop 0, Stage 0	Hatris NES	13
Shop 0, Stage 1	Hatris NES	13
Shop 0, Stage 2	Hatris NES	13
Shop 0, Stage 3	Hatris NES	13
Shop 0, Stage 4	Hatris NES	13
Shop 0, Stage 5	Hatris NES	13
Shop 0, Stage 6	Hatris NES	13
Shop 0, Stage 7	Hatris NES	13
Shop 0, Stage 8	Hatris NES	13
Shop 0, Stage 9	Hatris NES	13
Shop 1, Stage 0	Hatris NES	13
Shop 1, Stage 1	Hatris NES	13
Shop 1, Stage 2	Hatris NES	13
Shop 1, Stage 3	Hatris NES	13
Shop 1, Stage 4	Hatris NES	13
Shop 1, Stage 5	Hatris NES	13
Shop 1, Stage 6	Hatris NES	13
Shop 1, Stage 7	Hatris NES	13
Shop 1, Stage 8	Hatris NES	13
Shop 1, Stage 9	Hatris NES	13
Shop 2, Stage 0	Hatris NES	13
Shop 2, Stage 1	Hatris NES	13
Shop 2, Stage 2	Hatris NES	13
Shop 2, Stage 3	Hatris NES	13
Shop 2, Stage 4	Hatris NES	13
Shop 2, Stage 5	Hatris NES	13
Shop 2, Stage 6	Hatris NES	13
Shop 2, Stage 7	Hatris NES	13
Shop 2, Stage 8	Hatris NES	13
Shop 2, Stage 9	Hatris NES	13
Shop 3, Stage 0	Hatris NES	13
Shop 3, Stage 1	Hatris NES	13
Shop 3, Stage 2	Hatris NES	13
Shop 3, Stage 3	Hatris NES	13
Shop 3, Stage 4	Hatris NES	13
Shop 3, Stage 5	Hatris NES	13
Shop 3, Stage 6	Hatris NES	13
Shop 3, Stage 7	Hatris NES	13
Shop 3, Stage 8	Hatris NES	13
Shop 3, Stage 9	Hatris NES	13
Shop  4, Stage 0	Hatris NES	13
Shop  4, Stage 1	Hatris NES	13
Shop  4, Stage 2	Hatris NES	13
Shop  4, Stage 3	Hatris NES	13
Shop  4, Stage 4	Hatris NES	13
Shop  4, Stage 5	Hatris NES	13
Shop  4, Stage 6	Hatris NES	13
Shop  4, Stage 7	Hatris NES	13
Shop  4, Stage 8	Hatris NES	13
Shop  4, Stage 9	Hatris NES	13
Shop 5, Stage 0	Hatris NES	13
Shop 5, Stage 1	Hatris NES	13
Shop 5, Stage 2	Hatris NES	13
Shop 5, Stage 3	Hatris NES	13
Shop 5, Stage 4	Hatris NES	13
Shop 5, Stage 5	Hatris NES	13
Shop 5, Stage 6	Hatris NES	13
Shop 5, Stage 7	Hatris NES	13
Shop 5, Stage 8	Hatris NES	13
Shop 5, Stage 9	Hatris NES	13
300,000 points	Super Tetris 2 + Bombliss	14
B-Type Level 13 Height 5	Super Tetris 2 + Bombliss	14
100 Lines (C-Type)	Super Tetris 2 + Bombliss	14
40 Lines (C-Type, Level 20)	Super Tetris 2 + Bombliss	14
Level 0 (Puzzle)	Super Tetris 2 + Bombliss	14
Contest 1-10	Super Tetris 2 + Bombliss	14
100 Lines	Super Tetris 2 + Bombliss	14
Contest 1-10	Super Tetris 2 + Bombliss Genteiban	14
Win Halloween	Tetris Battle Gaiden	15
Win Mirurun	Tetris Battle Gaiden	15
Win Shaman	Tetris Battle Gaiden	15
Win Aladdin	Tetris Battle Gaiden	15
Win Princess	Tetris Battle Gaiden	15
Win Bit	Tetris Battle Gaiden	15
Win Ninja	Tetris Battle Gaiden	15
Win Wolf-Man	Tetris Battle Gaiden	15
100,000 Points Magicaliss	Super Tetris 3	16
Level 0 Puzzle (Sparkliss)	Super Tetris 3	16
Contest 1-5 (Sparkliss)	Super Tetris 3	16
Contest 6-10 (Sparkliss)	Super Tetris 3	16
300 000 points	Super Tetris 3	16
Round 0-3 (Magicaliss)	Super Tetris 3	16
Round 0-3 (Classic)	Super Tetris 3	16
Contest 1-10	Super Bombliss GB	17
Fight Mode - Boss 1-2	Super Bombliss GB	17
Fight Mode - Boss 3-4	Super Bombliss GB	17
Fight Mode - Boss 5-6	Super Bombliss GB	17
Boss 1	Super Bombliss SF	18
Boss 2	Super Bombliss SF	18
Boss 3	Super Bombliss SF	18
Boss 4	Super Bombliss SF	18
Boss 5	Super Bombliss SF	18
Boss 6	Super Bombliss SF	18
Boss 7	Super Bombliss SF	18
Boss 8	Super Bombliss SF	18
Fight Mode - Boss 1-2	Super Bombliss DX	19
Fight Mode - Boss 3-4	Super Bombliss DX	19
Fight Mode - Boss 5-6	Super Bombliss DX	19
Contest 1-10	Super Bombliss DX	19
Modern Marathon	Tetris Time Warp	20
1989 Marathon	Tetris Time Warp	20
150 lines	Tetris Time Warp	20
999,999 Points	Tetris Time Warp	20
40-Line Attack (Level 30)	Tetris Time Warp	20
20 T-Spins		21
Pizza Time!!!		21
Find Alexei		21
Watch a clip from the documentary		21
Play 10 different games		21
1 minute of Technotris		21
1 minute of Kalinka		21
1 minute of Troika		21"""

categories = parse_goals(goals_text)
bingo_card = generate_bingo_card(categories)
print_bingo_card(bingo_card)