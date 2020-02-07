# SRP (Single Responsibilty Principle) or SOC (Seperation Of Concerns)


class Journal:
    def __init__(self):
        self.entries = []
        self.count = 0

    def add_entry(self, text):
        self.count += 1
        self.entries.append(f'{self.count}: {text}')

    def remove_entry(self, position):
        del self.entries[position]

    def __str__(self):
        return '\n'.join(self.entries)

# These methods are not recommended. Cause these can be more generic and used
# for other classes
    def save(self, file_name):
        file = open(file_name, 'w')
        file.write(str(self))
        file.close()

    def load(self, file_name):
        pass

    def load_from_web(self, url):
        pass


class PersistenceManager:
    @staticmethod
    def save_to_file(_object, file_name):
        file = open(file_name, 'w')
        file.write(str(_object))
        file.close()


j = Journal()
j.add_entry('I nutted yesterday!')
j.add_entry('I hope I know what I am doing!')

print(f'Journal entries: \n{j}')

file = 'journal.txt'

PersistenceManager.save_to_file(j, file)


with open(file) as fh:
    print(fh.read())
