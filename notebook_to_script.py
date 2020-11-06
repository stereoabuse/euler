import json
import re
import datetime


f = open('euler__master.ipynb').read()

name = 'Chris B.'
date = datetime.date.today().strftime("%B %d, %Y")
LINE_LENGTH = 80
LEFT_JUS = 11

for cell in json.loads(f)['cells']:
    if cell['cell_type'] == 'code' and re.match(r'def prob_\d\d\d', ''.join(cell['source'])):
        f_name = re.match(r'def (prob_\d\d\d)', ''.join(cell['source']))[1]
        f_prob = re.match(r'def prob_(\d\d\d)', ''.join(cell['source']))[1]
        
        with open(f'/problems/{f_name}.py', 'w') as file:
            title = 'Project Euler Problem ' + f_prob
            subtitle = 'https://projecteuler.net/problem=' + f_prob
            
            # Write header info
            file.write('#' * LINE_LENGTH + '\n')
            file.write('#' + title.center(LINE_LENGTH - 2) + "#\n")
            if subtitle:
                file.write('#' + subtitle.center(LINE_LENGTH - 2) + "#\n")
            file.write('#' + ' ' * (LINE_LENGTH - 2) + '#\n')
            file.write('#' + ' Author:'.ljust(LEFT_JUS) + name.ljust(LINE_LENGTH-13) + '#\n')
            file.write('#' + ' Date:'.ljust(LEFT_JUS) + date.ljust(LINE_LENGTH-13) + '#\n')
            file.write('#' * LINE_LENGTH) 
            
            # Write the actual code
            file.write('\n\n')
            file.write(''.join(cell['source']))
            file.write('\n\n')
            file.write(f'{f_name}()')
            
print('done')
