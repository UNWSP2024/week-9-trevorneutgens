import program_3
 
def test_sum():    
    output = [] 
    
    program_3.print = lambda s : output.append(s)
 
    program_3.sum_numbers_from_file()
    print(output)
    correct_count_found = False
    for item in output:
        if "5153" in item or "5,153" in item or "5,153.00" in item or "5153.00" in item:
            correct_count_found = True

    assert correct_count_found == True