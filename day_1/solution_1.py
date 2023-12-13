def is_digit_string(s):
    digit_strings = {
        "zero": "0", "one": "1", "two": "2", "three": "3", "four": "4",
        "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"
    }
    siz = len(s)
    for t in digit_strings.keys():
        l = len(t)
        if s[0:min(l,siz)]==t:
            return [True, digit_strings[t]]
    return [False,None]

def is_digit_string_from_back(s):
    digit_strings = {
        "zero": "0", "one": "1", "two": "2", "three": "3", "four": "4",
        "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"
    }
    siz = len(s)
    for t in digit_strings.keys():
        l = len(t)
        if s[max(-l,-siz):]==t:
            return [True, digit_strings[t]]
    return [False,None]

def parse_line(line):
    l=len(line)
    i = 0
    continue_critera =True
    first_digit=None
    while(continue_critera):
        if line[i].isdigit():
            first_digit=line[i]
            continue_critera = False
        else:
            out = is_digit_string(line[i:min(i+5,l)])
            if out[0]:
                first_digit=out[1]
                continue_critera = False

        i=i+1

    j =len(line) -1
    continue_critera =True
    second_digit=None
    while( continue_critera):
        if line[j].isdigit():
            second_digit=line[j]
            continue_critera = False
        else:
            out = is_digit_string_from_back(line[max(j-6+1,0):j+1])
            if out[0]:
                second_digit=out[1]
                continue_critera = False

        j=j-1
    
    # digits = line[i] + line[j]
    digits = first_digit + second_digit

    return digits

def parse_file(file_path):
    """
    Parses the given file line by line and extracts the first and last digit from each line.

    Args:
    file_path (str): The path to the file to be parsed.

    Returns:
    list of tuples: A list containing tuples with the first and last digit of each line.
    """
    results = []
    sum = 0
    with open("out_file",'w') as o_file:
        with open(file_path, 'r') as file:
            for line in file:
                # Extracting digits from the line
                print(line)
                digits = parse_line(line)
                results.append(digits)
                print(digits)
                sum = sum + int(digits)
                o_file.write(line[:-3] + " " + digits + '\n')

    return sum

if __name__== "__main__":
    # print(is_digit_string("zero"))
    # print(is_digit_string("three"))
    # print(is_digit_string_from_back("eethree"))
    parse_line("7twor")
    test_case ={ "88twofourf": "84",
                 "558": "58",
                 "7twor": "72",
                 "six": "66",
                 "two1nine" : "29",
                "eightwothree" : "83",
                "abcone2threexyz" : "13",
                "xtwone3four" : "24",
                "4nineeightseven2" : "42",
                "zoneight234" : "14",
                "7pqrstsixteen" : "76"}
    for k,v in test_case.items():
        test = parse_line(k) == v
        if(not test):
            print("input line " +  k + ", expected output: " + v + ", parsed input: " + parse_line(k))
    

    input_file = "input_problem_1.txt"
    #
    print(parse_file(input_file))

