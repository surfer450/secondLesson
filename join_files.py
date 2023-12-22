from optparse import OptionParser


def file_manipulator(file_name1: str, file_name2: str, file_name3: str):
    """
    this function adds two files text into a third file
    :param file_name1: the path of first file
    :param file_name2: the path of second file
    :param file_name3: the path of file that the text will be in
    :return: None
    """
    try:
        file1, file2, file3 = open(file_name1, 'r'), open(file_name2, 'r'), open(file_name3, 'w')
        file3.write(file1.read() + "\n" + file2.read())
        [file.close() for file in (file1, file2, file3)]
        print("mission completed :)")

    except FileNotFoundError as fnf:
        print("could not find files :(")

    except UnicodeDecodeError as ud:
        print("the path is not a text file :(")


def set_parser() -> OptionParser:
    """
    this function sets default settings of the parser for the commend line
    :return: return the object parser
    """
    parser = OptionParser()

    parser.add_option('--f1', dest='fileName1',
                      type='string',
                      help='specify first file name')
    parser.add_option('--f2', dest='fileName2',
                      type='string',
                      help='specify second file name')
    parser.add_option('--f3', dest='fileName3',
                      type='string',
                      help='specify third file name')

    parser.usage = "enter files path after --f1, --f2, --f3"
    return parser


def main():
    parser = set_parser()
    (options, args) = parser.parse_args()
    if options.fileName1 is None or options.fileName2 is None or options.fileName3 is None:
        parser.print_help()
    else:
        file_manipulator(options.fileName1, options.fileName2, options.fileName3)


if __name__ == "__main__":
    main()
