import re
import sys


def get_file_paths():
    #remove THIS filename from sys.argv if it's in there
    args = sys.argv
    if __file__.rstrip('.py') in args[0]:
        del args[0]
    try:
        input_file_path = args[0]
    except IndexError:
        print "Usage: sql2csv input_file [output_file]"
        sys.exit(1)
    try:
        output_file_path = args[1]
    except IndexError:
        output_file_path = "%s-sql2csv.csv" % input_file_path
    return input_file_path, output_file_path


def is_separator(line):
    """ Is the line just +-----+----+ ?"""
    return re.match("\+[+-]+\+", line)


def convert_line(line):
    #TODO: this could be better, as at the moment it removes all whitespace
    line = line.strip("|")
    line = line.replace("|", ",")
    line = line.replace(" ", "")
    return line


def convert_file(sql_file, csv_file):
    for line in sql_file.readlines():
        if is_separator(line):
            continue
        line = convert_line(line)
        csv_file.write(line)


def main():
    input_file_path, output_file_path = get_file_paths()
    sql_file = open(input_file_path, "r")
    csv_file = open(output_file_path, "w")
    convert_file(sql_file, csv_file)
    sql_file.close()
    csv_file.close()
    print "Done"
    sys.exit(0)

if __name__ == "__main__":
    main()
