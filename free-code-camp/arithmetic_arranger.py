def arithmetic_arranger(problems, display_ans=False) :
    '''
    Takes in a list of addition/subtraction problems and returns a 
    formatted version of the problems.

        from this:    123 + 456 = 579

        to this:      123
                    + 456
                    -----
                      579
    '''
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    arranged_problems = ''
    line1 = ''
    line2 = ''
    dash_line = ''
    ans_line = ''
    answer = ''

    if len(problems) > 5 :
        return 'Too many problems!(Max: 5)'
    else :
        for i, problem in enumerate(problems) :
            if '+' not in problem and '-' not in problem :
                return 'Problems must be addition or subtraction!'
            for letter in alphabet :
                if letter in problem or letter.upper() in problem :
                    return 'Numbers must contain only digits!'
            if len(problem.split()[0]) > 4 or len(problem.split()[2]) > 4 :
                return 'Numbers cannot be more than 4 digits!'

            num1 = problem.split()[0]
            num2 = problem.split()[2]
            operator = problem.split()[1]

            if len(num1) < len(num2) :
                line1 += num1.rjust((len(num2) - len(num1) + len(num1) + 2)) + '    '
                line2 += operator + num2.rjust((len(num2) + 1)) + '    '
                dash_line += ''.rjust((len(num2) + 2), '-') + '    '
            else :
                line1 += num1.rjust((len(num1) + 2)) + '    '
                line2 += operator + num2.rjust((len(num1) - len(num2) + len(num2) + 1)) + '    '
                dash_line += ''.rjust((len(num1) + 2), '-') + '    '

            if operator == '+' :
                answer = int(num1) + int(num2)
            else :
                answer = int(num1) - int(num2)
            ans_line += str(answer).rjust((max(len(num1), len(num2)) + 2)) + '    '

        if display_ans == True :
            arranged_problems += line1[:-4] + '\n' + line2[:-4] + '\n' + dash_line[:-4] + '\n' + ans_line[:-4]
        else :
            arranged_problems = line1[:-4] + '\n' + line2[:-4] + '\n' + dash_line[:-4]

    return arranged_problems

problems = ['123 + 4586', '123 - 4356', '123 + 453', '1232 + 634']


print(arithmetic_arranger(problems))