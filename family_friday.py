import random

def randomize(array):
    """Takes in an array as an input and returns a randomized array of arrays."""
    array_len = len(array)
    if array_len <= 3:
        return array
    random.shuffle(array)
    sublists = [array[i:i+4] for i in range(0, array_len, 4)]
    # if we have a single person left out, add them to the last group of 4
    if len(sublists[-1]) == 1:
        sublists[-2].append(sublists[-1][0])
        sublists.pop()
    # if we have two people left out, add a person from the last group of 4
    # to the group of 2
    elif len(sublists[-1]) == 2:
        sublists[-1].append(sublists[-2][-1])
        sublists[-2].pop()
    return sublists

def store(array, fname):
    """Stores the array in a plaintext file."""
    storage = open(fname, 'w')
    for employee in array:
        storage.write(str(employee)+'\n')
    storage.close()

def load(fname):
    """Parses the text file into an array."""
    with open(fname) as f:
        array, string = [], []
        for char in f.read():
            if char == '\n':
                array.append("".join(string))
                string = []
            else:
                string.append(char)
        return array

def insert(employee, array, fname):
    """Inserts a new employee into the existing list of employees.
    Returns a string of the current number of employees. We will assume that no
    there will be no repeat names."""
    array.append(employee)
    store(array, fname)
    return str(len(array))

def delete(employee, array, fname):
    """Deletes an existing employee if they exist. Returns a string of the
    current number of employees. Otherwise, returns False. We will assume that
    there will be no repeat names."""
    try:
        array.remove(employee)
        store(array, fname)
        return str(len(array))
    except:
        return False

def cli():
    """A front-end facing CLI to insert new employees into the array, delete
    employees, or randomly sort the employees into groups of 3-5."""
    while True:
        action = input('Would you like to insert, sort, or delete? ').lower()
        if action == 'sort':
            array = load('storage.txt')
            print(randomize(array))
            break
        elif action == 'insert':
            employee = input('Who would you like to add? ')
            employ_num = insert(employee, load('storage.txt'), 'storage.txt')
            print('Employee #' + employ_num + ', ' + employee + ' successfully added!')
            break
        elif action == 'delete':
            employee = input('Who would you like to delete? ')
            employ_num = delete(employee, load('storage.txt'), 'storage.txt')
            if employ_num:
                print('There are ' + employ_num + ' employees left.')
            else:
                print(employee + ' is not an employee at Apartment List.')
            break

if __name__ == '__main__':
    cli()
