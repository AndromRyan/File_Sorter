# Owner: Alex Ryan
# Started: 13 Aug 2020

# Script to organise downloads directory
# Read File name and move to required location
# Filename: object-location_year_month
# Dir Structure: Loc > year >> jan, feb, ..., dec
# Location: Personal, Work, University, Random, Software
#     printJo      P, W, U, R, S


import sys
import time
import json
import getopt
import datetime
from os import path, listdir, makedirs, rename


# Definitions
locat_list = {'Per': 'Personal', 'Wor': 'Work', 'Uni': 'University', 'Ran': 'Random', 'Sof': 'Software'}
month_list = {1: 'Jan', 2: 'Feb', 3: 'Mar', 4: 'Apr', 5: 'May', 6: 'Jun', 7: 'Jul', 8: 'Aug', 9: 'Sep',
              10: 'Oct', 11: 'Nov', 12: 'Dec'}
downloads_dir = '/home/androm/Downloads/'
documents_dir = '/home/androm/Documents/'
# Path checks
# print("Check if downloads path can be found: ", path.exists(downloads_dir))
# print("Check if documents path can be found: ", path.exists(documents_dir))

section = "origin_dir/"
value_to_check = "/home/androm/Downloads/"


def opening_statement():
    # Opening statement when running
    statement_width = 60
    print("\n|" + (statement_width * "-") + "|")
    print(f'''|\tScript to organise downloads directory                   |
    |\tRead File name and move to required location             |
    |\tFilename: object-location                                |
    |\tDir Structure: Loc > year >> jan, feb, ..., dec          |
    |\tLocation: Personal, Work, University, Random, Software   |
    |\tStrips the extensions of the file, helps with the sorter |''')
    print("|" + (statement_width * "-") + "|")


def print_help():
    # Help statement on -h flag
    help_width = 65
    print(f'''\n      |{help_width * "="}|
      |             Help statement: download_sorter.py -...             |
      |\t-h or --help        \t To print help statement                |
      |\t-v or --version     \t To print version                       |
      |\t-i or --info        \t Prints info on individual file         |
      |\t-l or --locat "a,b" \t Add locations to sorter                |
      |\t-o or --ori "/a"    \t Add origin to sorter                |
      |\t-d or --des "/a"    \t Add destination to sorter                |
      |\t-r or --remove "a,b"\t Remove locations from sorter           |
      |\t-R or --REMOVE "/a,/b"\t Remove directory from sorter           |
      |\t-w or --WIPE        \t Wipe all dirs and locats from sorter   |
      |\t-A or --AUTO "/dir" \t Auto location from directory           |
      |\t-t or --time        \t Infinite runetinme on current settings |''')
    print("      |" + (help_width * "=") + "|")


def file_base_name(file_name):
    # Strips file name at '.'
    if '.' in file_name:
        separator_index = file_name.index('.')
        base_name = file_name[:separator_index]
        return base_name
    else:
        return file_name


def path_check_make(route, dirs_generated):
    # Checks if route is there, if not make it and return True
    # Should always return tue as it recursively creates then checks
    # returns ture after making
    if not path.exists(route):
        # location path doesnt exists
        makedirs(route)
        dirs_generated.append(route)
        path_check_make(route, dirs_generated)
    else:
        # location path exists
        return True


def camel_cut(location):
    location = location.title()
    if len(location) > 3:
        locat = location[:3]
    else:
        filler = 3 - len(location)
        locat = location + (filler * "0")
    return location, locat
# print(camel_cut("h"))


def read_config():
    # Read configurations from the config file
    # Allows for preferences to be saved and updated
    definitions = {}
    with open('sorter_config.txt', 'r') as file_read:
        for line in file_read:
            line = line.strip()
            if "=" not in line:
                print("Config Error")
            else:
                # print(line)
                name, value = line.split(" = ")
                if (name == 'locat_list') or (name == 'month_list'):
                    value = json.loads(value)
            definitions[name] = value
    return definitions


config = read_config()


def write_config(definitions):
    # Allows for updating the preferences
    with open('sorter_config_2.txt', 'w') as file_write:
        for name, value in definitions.items():
            if (name == 'locat_list') or (name == 'month_list'):
                value = json.dumps(value)
            file_write.write(name + " = " + value + "\n")


def config_checker(conf, sect, val2c):
    # After reading config, check if input is within current config
    print(f"section: {sect}, value_to_check {val2c}, config:  {conf}")
    # if value is within the config section
    # if false ask for new input
    if section in conf:
        if conf[sect] != 0:
            if conf[sect] == val2c:
                # correct value
                return True
            else:
                # incorrect value
                return False
    else:
        # incorrect section
        return False


# checker = config_checker(config, section, value_to_check)
# print(checker)


def config_origin_destin(direc_list):

    return True


def config_remove(_locat_list, _config):
    locat_cam_lst = [camel_cut(direc) for direc in _locat_list]
    print("config_remove camel: ", locat_cam_lst)
    print(type(config))
    for pair in locat_cam_lst:
        print(pair)
        for long, short in pair:
            if short == config[locat_list]:
                print("Found conf")
    print(config["locat_list"])


config_remove(["personal", "work", "university"], config)


def config_hard_remove(_direc_list):
    print("config_hard_remove: ", _direc_list)


# config_hard_remove([documents_dir, downloads_dir])


def config_wipe():
    config_remove("ALL")
    config_hard_remove("ALL")
    print("Wiped my poo")
    return True


# config_wipe()


def system_input():
    # Gets the arguments, and passes runs required version of the sorter
    # Read in command-line arguments
    full_cmd_arguments = sys.argv

    # Keep all but the first
    argument_list = full_cmd_arguments[1:]
    # print(argument_list)

    short_options = "hvild:A:r:R:Wt"
    long_options = ["help", "version", "info", "locat=", "dir=", "AUTO=", "remove=", "REMOVE=", "WIPE", "time"]

    try:
        arguments, values = getopt.getopt(argument_list, short_options, long_options)
        # print("values: ", values)
        # print("Argu: ", arguments)
    except getopt.error as err:
        # Output error, and return with an error code
        print(str(err))
        sys.exit(2)

    # Definitions
    version = "0.2.4"
    info_bool = False
    run_bool = False

    # Evaluate given options
    for current_argument, current_value in arguments:
        if current_argument in ("-h", "--help"):
            print_help()
        elif current_argument in ("-v", "--version"):
            print(f"Running version {version}")
        elif current_argument in ("-i", "--info"):
            print("Enabling information mode")
            info_bool = not info_bool
        elif current_argument in ("-l", "--locat"):
            print("Adding locat: (%s)" % current_value)
        elif current_argument in ("-d", "--dir"):
            print("Adding dir: (%s)" % current_value)
        elif current_argument in ("-A", "--AUTO"):
            print("Enabling Auto directory mode from: (%s)" % current_value)
        elif current_argument in ("-r", "--remove"):
            print("Enabling special output mode (%s)" % current_value)
        elif current_argument in ("-R", "--REMOVE"):
            print("Enabling special output mode (%s)" % current_value)
        elif current_argument in ("-W", "--WIPE"):
            print("Wipe destination directories from sorter")
        elif current_argument in ("-t", "--time"):
            print("Running all the time")
            run_bool = not run_bool

    arg_definitions = {'origin_dir': '/home/androm/Downloads/',
                       'destin_dir': '/home/androm/Documents/',
                       'locat_list': {'Per': 'Personal', 'Wor': 'Work', 'Uni': 'University', 'Ran': 'Random',
                                      'Sof': 'Software'},
                       'month_list': {'1': 'Jan', '2': 'Feb', '3': 'Mar', '4': 'Apr', '5': 'May', '6': 'Jun',
                                      '7': 'Jul', '8': 'Aug', '9': 'Sep', '10': 'Oct', '11': 'Nov', '12': 'Dec'},
                       'info_bool': 'False',
                       'run_bool': 'False'}
    return arg_definitions


# arg_defins = system_inputs()


def sorter(origin, destination, locats, months, info=False, run_time=False):
    downloads_sorted = 0
    dirs_generated = []
    print(run_time)
    # Get files from sorting origin
    downloads_files_list = listdir(origin)
    downloads_files = len(downloads_files_list)
    if downloads_files != 0:
        print("\nItems within Downloads dir: ", downloads_files_list)
        for file in downloads_files_list:
            file_stripped = file_base_name(file)
            if info:
                print(f"\n{file} -> {file_stripped}")

            if not any(("--" + locs) in file_stripped for locs in locats):
                if info:
                    print("No sorter supplied")
                continue
            else:
                item, loc = file_stripped.split('--')
                file_loc = locats[loc]
                if info:
                    print(item, file_loc)

                file_ctime = path.getmtime(downloads_dir + '/' + file)
                file_cstr = time.ctime(file_ctime)

                file_datetime = datetime.datetime.fromtimestamp(file_ctime)
                file_year = file_datetime.year
                file_month = file_datetime.month

                if info:
                    print(f"{file} was created {file_cstr}")
                file_month = months[file_month]
                # print(f"{file} year: {file_year}, month: {file_month}")

                # Check if location exists
                # First check if the main location exists
                # then recurrently go into the years and months
                # If exists check deeper
                # If doesnt exist make current remaining requirements
                doc_location = documents_dir + file_loc
                doc_year = doc_location + "/" + str(file_year)
                doc_month = doc_year + "/" + file_month
                file_cleaned = file.replace('--' + loc, '')
                doc_destination = doc_month + "/" + file_cleaned

                doc_dirs = [doc_location, doc_year, doc_month]
                for doc_dir in doc_dirs:
                    path_check_make(doc_dir, dirs_generated)
                    if info:
                        print(f"Check if {doc_dir} path can be found: ", path.exists(doc_dir))

                rename(downloads_dir + "/" + file, doc_destination)
                if info:
                    print(f"File {file_cleaned} to move \n\tFrom {downloads_dir} \n\tTo {doc_destination}")

                if path.exists(destination):
                    downloads_sorted += 1
        downloads_remain = downloads_files - downloads_sorted
        print(f"Files moved: {downloads_sorted}, remaining: {downloads_remain}")
        if len(dirs_generated) == 0:
            print(f"No directories generated")
        else:
            print(f"Directories generated: {dirs_generated}")
    else:
        print(f"\nNo files found in {downloads_dir}")
        print(f"No directories generated")


# # downloads_dir, documents_dir, locat_list, month_list, info_bool, run_bool =
# config_check(arg_defins)
# # sorter(origin=downloads_dir, destination=documents_dir, locats=locat_list,
# #        months=month_list, info=info_bool, run_time=run_bool)























# def config_check(arg_config):
#     # after user inputs flags and updates the sorter,
#     # check current config file and look for differences
#     #
#     curr_config = read_config()
#     print("curr_config: ", curr_config)
#     print("arg_config:  ", arg_config)
#     print(arg_config)
#
#     dictget = lambda d, *k: [d[i] for i in k]
#     ch_origin_dir, ch_destin_dir, ch_locat_list, ch_month_list, ch_info_bool, \
#     ch_run_bool = dictget(arg_config, 'origin_dir', 'destin_dir', 'locat_list', 'month_list', 'info_bool', 'run_bool')
#     if curr_config == arg_config:
#         print("YAY")
#
#     write_config(arg_config)
#
#     return ch_origin_dir, ch_destin_dir, ch_locat_list, ch_month_list, ch_info_bool, ch_run_bool
