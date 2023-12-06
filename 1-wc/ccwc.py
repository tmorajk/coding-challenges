import argparse
import sys


class Utility:
    @staticmethod
    def count_bytes(input_content: bytes) -> int:
        return len(input_content)

    @staticmethod
    def count_lines(input_content: bytes) -> int:
        return len(input_content.splitlines())

    @staticmethod
    def count_words(input_content: bytes) -> int:
        return len(input_content.split())

    @staticmethod
    def count_chars(input_content: bytes) -> int:
        return len(input_content.decode('utf8'))


parser = argparse.ArgumentParser(
    prog='ccwc.py',
    description='word, line, character, and byte count',
    epilog='Example: ccwc [options] [filename]')

output_str = ''
if len(sys.argv) == 2:
    with open(sys.argv[1], 'rb') as input_file:
        content = input_file.read()
        output_str += ' '.join([str(Utility.count_bytes(content)),
                                str(Utility.count_lines(content)),
                                str(Utility.count_words(content)),
                                sys.argv[1]])
else:
    with open(sys.argv[2], 'rb') as input_file:
        content = input_file.read()
        if sys.argv[1] == '-c':
            output_str += str(Utility.count_bytes(content))
        elif sys.argv[1] == '-l':
            output_str += str(Utility.count_lines(content))
        elif sys.argv[1] == '-w':
            output_str += str(Utility.count_words(content))
        elif sys.argv[1] == '-m':
            output_str += str(Utility.count_chars(content))
        output_str += ' ' + sys.argv[2]
print(output_str)
