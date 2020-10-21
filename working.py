from constants import SAVE_WORKING, log_directory


working = []
current_step = []
synchronise_step_count = 0

def clear():
    with open(log_directory, 'w'):
        pass

def log_method(message, *args, priority_level=-1):
    if not SAVE_WORKING:
        return

    global working

    if args:
        content = f'{message}: {", ".join(map(str, args))}'
    else:
        content = f'{message}.'

    if priority_level >= 2:
        # working.append(f'<ul>{content}</ul>')
        working.append(f'[step: {content}]...')
        displayed = f'[Step] {content}'
    elif priority_level == 1:
        # working.append(f'<li class="working-header">{content}</li>')
        working.append(f'[head: {content}]')
        displayed = f'|*| {content}'
    elif priority_level == 0:
        # working.append(f'<li class="working-double">{content}</li>')
        working.append(f'[work: {content}]')
        displayed = f' *  {content}'
    else:
        # working.append(f'<li class="working">{content}</li>')
        working.append(f'{content}')
        displayed = f'| {content}'

    print(displayed)
    with open(log_directory, 'a') as log_file:
        log_file.write(displayed + '\n')


clear()
