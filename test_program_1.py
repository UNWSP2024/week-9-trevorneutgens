import program_1
 
def test_count():    
    output = [] 
    
    program_1.print = lambda s : output.append(s)
 
    program_1.count_file_lines()
    print(output)
    correct_count_found = False
    for item in output:
        if "31" in item:
            correct_count_found = True

    assert correct_count_found == True