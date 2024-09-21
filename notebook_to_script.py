import json
import re
import datetime
from pathlib import Path

LINE_LENGTH = 80
LEFT_JUS = 11

def extract_euler_problems(notebook_path, output_dir, name):
    f = open(notebook_path).read()
    date = datetime.date.today().strftime("%B %d, %Y")

    Path(output_dir).mkdir(exist_ok=True)

    for cell in json.loads(f)['cells']:
        if cell['cell_type'] == 'code' and re.match(r'def prob_\d\d\d', ''.join(cell['source'])):
            f_name = re.match(r'def (prob_\d\d\d)', ''.join(cell['source']))[1]
            f_prob = re.match(r'def prob_(\d\d\d)', ''.join(cell['source']))[1]
            
            with open(f'{output_dir}/{f_name}.py', 'w') as file:
                # Write header
                write_header(file, f_prob, name, date)
                
                # Write the actual code
                file.write('\n\n')
                file.write(''.join(cell['source']))
                file.write('\n\n')
                file.write(f'{f_name}()')
            
    print('done')

def write_header(file, prob_num, name, date):
    title = 'Project Euler Problem ' + prob_num
    subtitle = 'https://projecteuler.net/problem=' + prob_num
    
    file.write('#' * LINE_LENGTH + '\n')
    file.write('#' + title.center(LINE_LENGTH - 2) + "#\n")
    file.write('#' + subtitle.center(LINE_LENGTH - 2) + "#\n")
    file.write('#' + ' ' * (LINE_LENGTH - 2) + '#\n')
    file.write('#' + ' Author:'.ljust(LEFT_JUS) + name.ljust(LINE_LENGTH-13) + '#\n')
    file.write('#' + ' Date:'.ljust(LEFT_JUS) + date.ljust(LINE_LENGTH-13) + '#\n')
    file.write('#' * LINE_LENGTH)

if __name__ == '__main__':
    notebook_path = 'euler__master.ipynb'
    output_dir = 'problems'
    author_name = 'Chris B.'
    
    extract_euler_problems(notebook_path, output_dir, author_name)
