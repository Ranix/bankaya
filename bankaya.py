
def open_file(file_name:str) -> str:
    """Open and read a file.
    Args:
        file_name(str)
    Returns:
        reader(list) : Returns a list object
    """
    with open(file_name, 'r') as reader:
        return reader.readlines()


def strig_to_ascii(file_name: str, open_file) -> str:
    """Converts text read from a file to an ascii string, 
       removing line breaks and whitespace.
    Args:
        file_name(str)
        open_file(Function)
    Returns:
        ascii_drawn(str): string of ascii code
    """
    ascii_drawn = ''
    raw_str = open_file(file_name)
    for line in raw_str:
        for character in line.replace('\n', '').replace(' ', ''):
            ascii_drawn += str(ord(character))
    return ascii_drawn


if __name__ == "__main__":
    bug = strig_to_ascii('bug.txt', open_file)
    landscape = strig_to_ascii('landscape.txt', open_file)
    print(landscape.count(bug))