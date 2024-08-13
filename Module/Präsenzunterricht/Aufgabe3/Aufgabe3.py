import file_operations
import os

# Change current working directory to the directory of the script
os.chdir(os.path.dirname(os.path.abspath(__file__)))

file_operations.write_file('test.txt', 'Hello World')
print(file_operations.read_file('test.txt'))
file_operations.append_to_file('test.txt', 'Hello World2')
print(file_operations.read_file('test.txt'))