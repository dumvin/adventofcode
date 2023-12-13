
def  extract_score(winning_numbers, personal_numbers):
    count_score = -1

    for n in personal_numbers:
        if n in winning_numbers:
            count_score = count_score + 1
    if count_score < 0:
        return 0
    else:
        return 2**count_score

def parse_line(line):
    inputs = line.split(":")
    game_id = inputs[0]
    data = inputs[1].split("|")

    winning_numbers = [int(a) for a in data[0].split()]
    personal_numbers = [int(a) for a in data[1].split()]

    return [game_id, winning_numbers, personal_numbers]

        


def parse_file(file_path):
    """
    Parses the given file line by line and tell if a game is possible from each line.

    Args:
    file_path (str): The path to the file to be parsed.

    Returns:
    The sum of the id of games in which the results are possible
    """
    results = []
    sum = 0
    game_id = 1
    with open(file_path, 'r') as file:
        for line in file:
            # Extracting digits from the line
            [id, winning_numbers, personal_numbers] = parse_line(line)
            
            sum = sum + extract_score(winning_numbers, personal_numbers)
    return sum

def parse_line_test():
    input_data = ["Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53",
                   "Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19",
                   "Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1",
                   "Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83",
                   "Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36",
                   "Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"]
    out_data = [["Card 1", [41,48,83,86,17], [83,86,6,31,17,9,48,53] ]]
    
    print(parse_line(input_data[0]))
    
def test_score():
    in_data = [[[41,48,83,86,17], [83,86,6,31,17,9,48,53] ]]
    out_data = 8
    print(extract_score(in_data[0][0], in_data[0][1]))


if __name__== "__main__":

    parse_line_test()
    test_score()
    input_file = "day_4/input.txt"
    print(parse_file(input_file))


