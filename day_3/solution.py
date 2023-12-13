def parse_number(line,idx):
    """
    Parses a number in a string from an initial index
    Args:
    line (str): The path to the file to be parsed.

    Returns:
    the parsed number(int)
    the length of the nuber in string (int)
    """
    j = idx
    while (j<len(line) and line[j].isdigit()):
        j = j+1

    return [int(line[idx:j]),j-idx]

def is_adjacent_character(c):
    return not(c.isdigit() or c=='.' or c=='\n')

def is_adjacent_number(lines,i_row,j_col,length):
    """
    Checks if there are no specific symbols around string in the text (located by a position and length)

    Args:
    lines (str): The lines describing the file.
    i_row(int),j_col(int): starting indexes for the string
    length(int): length of the string to check

    Returns:
    Boolean to indicate if there is around the word a character different from . or digit
    """
    
    n_row = len(lines)
    m_col = len(lines[0])

    # Check above the word:
    if(i_row>0):
        for j in range(max(j_col-1,0),min(j_col+length+1,m_col)):
            if is_adjacent_character (lines[i_row-1][j]):
                return True
            
    #check left of the word
    if (j_col>0):
        if is_adjacent_character(lines[i_row][j_col-1]):
            return True
        
    #check right of the word
    if (j_col+length<m_col-1):
        if is_adjacent_character(lines[i_row][j_col+length]):
            return True

    # Check below the word:
    if(i_row<n_row-1):
        for j in range(max(j_col-1,0),min(j_col+length+1,m_col)):
            if is_adjacent_character(lines[i_row+1][j]):
                return True
    
    return False

def parse_file(file_path):
    """
    Parse the input file, and goes through it line by line to search 
    for numbers and add them to the total sum if they are adjacent to 
    a specific symbole

    Args:
    file_path(str): A string containing the path to the file

    Returns:
    the sum of all the adjacent numbers
    """
    sum = 0
    with open(file_path, 'r') as file:
        lines = file.readlines()
        idx_line=0
        n_row = len(lines)
        n_col = len(lines[0])-1 # to get rid of new line character
        for l in lines:
            i_col = 0
            while i_col<n_col:
                c = l[i_col]
                if c.isdigit():
                    [num,num_len] = parse_number(l,i_col)
                    if(is_adjacent_number(lines,idx_line,i_col,num_len)):
                        sum=sum+num
                    i_col = i_col + num_len
                else:
                    i_col = i_col+1
                
            idx_line = idx_line + 1

    return sum

def test_parse():
    test_case ={ "123": [0,[123,3]],
                 "558*.": [0,[558,3]],
                 "...223**": [3,[223,3]]}
    false_cases = 0
    for k,v in test_case.items():
        test = parse_number(k,v[0]) == v[1]
        if(not test):
            print("input string " +  k + ", initial idx : "+ str(v[0]) +", expected output: " + str(v[1]) + ", parsed input: " + str(parse_number(k,v[0])))
            false_cases = false_cases + 1

    if false_cases == 0:
        print("All tests on parsing numbers passed")
    else:
        print("Failed cases for parsing number: " + str(false_cases))

def test_adjacent():
    test_inputs=[
            [".....\n",
             ".338.\n",
             "....*\n"],
            [".....\n",
             ".338.\n",
             ".....\n"],
            [".....\n",
             ".338.\n",
             "..12*\n"],
            ["12...\n",
             ".338.\n",
             ".....\n"]
    ]
    test_sol ={ "test_1": [0,1,1,3,True],
                 "test_2": [1,1,1,3,False],
                 "test_3": [2,2,2,2,True],
                 "test_4": [3,0,0,2,False]}
    false_cases = 0
    for k,v in test_sol.items():
        test = is_adjacent_number(test_inputs[v[0]],v[1],v[2],v[3]) == v[4]
        if(not test):
            print("test case : " + k)
            print("input string " +  str(test_inputs[v[0]]))
            print("Initial indices and length: "+ str(v[1:4]) +", expected output: " + str(v[4]) + ", parsed input: " + str(is_adjacent_number(test_inputs[v[0]],v[1],v[2],v[3])))
            false_cases = false_cases + 1

    if false_cases == 0:
        print("All tests on adjacent numbers passed")
    else:
        print("Failed cases for adjacent number: " + str(false_cases))
        

if __name__== "__main__":
    test_parse()
    test_adjacent()
    input_file = "day_3/input.txt"
    print(parse_file(input_file))


