import file_operations



file_operations.write_file('test.txt', 'Hello World')
print(file_operations.read_file('test.txt'))
file_operations.append_to_file('test.txt', 'Hello World2')
print(file_operations.read_file('test.txt'))