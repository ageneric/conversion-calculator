from constants import USE_WORKING, LOG_WORKING, log_directory
from itertools import count

# Modified using global by log_method().
# Used by main while evaluating steps.
working = []
current_step = []

# Increments for unique id.
id_counter = count(0)

def clear():
    if LOG_WORKING:
        with open(log_directory, 'w'):
            pass

def log_method(message, *args, priority_level=-1):
    if not USE_WORKING:
        return

    global current_step

    if args:
        content = f'{message}: {", ".join(map(str, args))}'
    else:
        content = f'{message}.'

    if priority_level >= 2:
        element = {'tag': 'h3', 'class': 'step-header'}
        displayed = f'Step: {content}'
    elif priority_level == 1:
        element = {'tag': 'li', 'class': 'working-header'}
        displayed = f'| {content}'
    elif priority_level == 0:
        element = {'tag': 'li', 'class': 'working-legend'}
        displayed = f'- {content}'
    else:
        element = {'tag': 'li', 'class': 'working'}
        displayed = content

    element['string'] = content
    element['key'] = next(id_counter)
    current_step.append(element)

    if LOG_WORKING:
        print(displayed)
        with open(log_directory, 'a') as log_file:
            log_file.write(displayed + '\n')


clear()
