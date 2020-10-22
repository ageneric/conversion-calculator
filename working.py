from constants import SAVE_WORKING, LOCAL_DEBUG, log_directory

# Modified using global by log_method().
# Used by main while evaluating steps.
working = []
current_step = []
current_step_title = ''

def clear():
    if LOCAL_DEBUG:
        with open(log_directory, 'w'):
            pass

def log_method(message, *args, priority_level=-1):
    if not SAVE_WORKING:
        return

    global current_step
    global current_step_title

    if args:
        content = f'{message}: {", ".join(map(str, args))}'
    else:
        content = f'{message}.'

    if priority_level >= 2:
        current_step_title = f'<h3>{content}</h3>'
        displayed = f'[Step] {content}'
    elif priority_level == 1:
        current_step.append(f'<li class="working-header">{content}</li>')
        displayed = f'|*| {content}'
    elif priority_level == 0:
        current_step.append(f'<li class="working">{content}</li>')
        displayed = f' *  {content}'
    else:
        current_step.append(f'<li class="working-small">{content}</li>')
        displayed = f'| {content}'

    if LOCAL_DEBUG:
        print(displayed)
        with open(log_directory, 'a') as log_file:
            log_file.write(displayed + '\n')


clear()
