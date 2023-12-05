def write_file(file_name, file_content):
    pass
    with open(f'{file_name}.txt', 'w') as f:
        f.write(file_content)
def append_file(file_name, append_content):
    pass
    with open(f'{file_name}.txt', 'a') as f:
        f.write(append_content)
def read_file(file_name):
    pass
    with open(f'{file_name}.txt', 'r') as f:
        file_content_read = f.read()
    return file_content_read
    


write_file(file_name="logfile", file_content="Log 1: 5 bananas added" )
append_file(file_name="logfile", append_content="Log 2: 3 bananas subtracted")

print(read_file(file_name="logfile"))