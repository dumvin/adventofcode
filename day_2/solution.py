
color = ["blue","red","green"]

def test_possible_run(run,input_num):
    for i in range(0,len(run)):
        if run[i]>input_num[i]:
            return(False)
    return(True)

def test_possible_game(runs,input_num):
    test = True
    for r in runs:
        if not test_possible_run(r,input_num):
            return(False)
    return True

def parse_line(line):
    inputs = line.split(":")
    runs = inputs[1].split(";")
    # parsed a game in a 2d array:
    # a line is one round
    # first column is the number of blue
    # second column is the number of red 
    # third column is the number of green

    parsed_game = []  
    for g in runs:
        res = []
        for c in color:
            sep = g.split(c)
            if len(sep) == 1:
                res.append(0)
            else:
                res.append(int(sep[0].split()[-1]))
        parsed_game.append(res)
    return parsed_game
        


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
            game = parse_line(line)
            if(test_possible_game(game,[14,12,13])):
                sum = sum + game_id

            results.append([game_id,test_possible_game(game,[14,12,13])])

            game_id = game_id + 1

    return sum

if __name__== "__main__":
    test_case ={ "Game 1: 5 red, 1 green; 6 red, 3 blue; 9 red; 1 blue, 1 green, 4 red; 1 green, 2 blue; 2 blue, 1 red": (True,[[0,5,1],[3,6,0],[0,9,0],[1,4,1],[2,0,1],[2,1,0]])}
    for k,v in test_case.items():
        game = parse_line(k)
        test = test_possible_game(game,[14,12,13]) == v[0]
        if(not test):
            print("input line " +  k + ", expected output: " + str(v) + ", parsed input: " + str(game), ", Results: " + str(not v))
    

    input_file = "input.txt"
    print(parse_file(input_file))


