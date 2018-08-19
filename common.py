import binascii
import shutil
import subprocess
import os

# Constants
USER_HOME_DIR = os.path.expanduser('~')

HINTS_FILE = os.path.join(USER_HOME_DIR, 'hints.txt')

FLAG_FILE_1 = '/tmp/flag_1.txt'
FLAG_FILE_2 = '/usr/var/.flag_2.txt'
FLAG_FILE_3 = os.path.join(USER_HOME_DIR, 'flag_3.txt')
FLAG_FILE_4 = '/usr/lib/flag_of_liberary.so'
FLAG_4_LINK_NAME = os.path.join(USER_HOME_DIR, 'empty.txt')
FLAG_FILE_5 = os.path.join(USER_HOME_DIR, 'misdirection.jpg')
FLAG_FILE_6 = os.path.join(USER_HOME_DIR, '../flag_6.txt')
FLAG_FILE_7 = os.path.join(USER_HOME_DIR, 'manual.txt')
FLAG_7_SOURCE_FILE = 'resources/emacs_manual.txt'
FLAG_8_DIRECTORY = os.path.join(USER_HOME_DIR, 'forest')
FLAG_8_FILENAME_TEMPLATE = "tree_%d.txt"
FLAG_8_NUMBER_OF_FILES = 500
FLAG_8_FILE_NUMBER = 216

# Using "strict" as the decode error type will raise an exception if the unicode string cannot be decoded (see https://docs.python.org/3.3/howto/unicode.html)
# Use the 'xxd -r -p' command to un-hexify the file name and contents
# Ex: echo '6d44080c36d4be4e52b31cd52346aaef' | xxd -r -p => 'filename'
FLAG_9_FILE_NAME = binascii.hexlify('flag_9.txt'.encode("utf8")).decode("utf8", "strict")
FLAG_FILE_9 = os.path.join(USER_HOME_DIR, FLAG_9_FILE_NAME)

FLAG_10_DIRECTORY = os.path.join(USER_HOME_DIR, 'the_ocean')
FLAG_FILE_10_ORIGINAL_PATH = os.path.join(FLAG_10_DIRECTORY, 'Jim')
FLAG_FILE_10_DESIRED_PATH = os.path.join(USER_HOME_DIR, 'Jim')

FLAG_11_BOULDER = os.path.join(USER_HOME_DIR, 'boulder')

FLAG_12_DIRECTORY = os.path.join(USER_HOME_DIR, 'box')

FLAG_13_THING_1 = os.path.join(USER_HOME_DIR, 'thing_1.txt')
FLAG_13_THING_2 = os.path.join(USER_HOME_DIR, 'thing_2.txt')

FLAG_FILE_15_NAME = 'flag_15.txt'
FLAG_FILE_15_COMPRESSED_NAME = 'flag_15.txt.tar.gz'
FLAG_FILE_15 = os.path.join(USER_HOME_DIR, FLAG_FILE_15_NAME)
FLAG_FILE_15_COMPRESSED = os.path.join(USER_HOME_DIR, FLAG_FILE_15_COMPRESSED_NAME)
FLAG_FILE_17_INPUT_FILE = os.path.join(USER_HOME_DIR, 'input.txt')

FLAG_DIRECTORY_18_ROOT = os.path.join(USER_HOME_DIR, 'here')
FLAG_18_BOX_NUMS = range(1,1000)
FLAG_FILE_18_NAME = 'flag_18.txt'

FLAG_FILE_19_DIRECTORY = os.path.dirname(subprocess.check_output(['which', 'ls']).strip())
FLAG_FILE_19 = os.path.join(FLAG_FILE_19_DIRECTORY, 'flag_19.txt')
FLAG_FILE_20 = os.path.join(USER_HOME_DIR, 'flag_20.txt')
FLAG_FILE_21 = '/var/log/flag_21.log'
FLAG_FILE_22 = os.path.join(USER_HOME_DIR, 'flag_22.txt')
FLAG_FILE_24 = ''
FLAG_25_SCRIPT = os.path.join(USER_HOME_DIR, 'flag_25.sh')
FLAG_25_PROCESS_SCRIPT = '/tmp/bill.sh'
FLAG_FILE_25 = ''


# Utility functions

def quit_if_not_root():
    if os.getuid() != 0:
        print("\nError: script must be run as root (i.e. using sudo)\n")
        quit()

def write_to_file(file_path, contents):
    with open(file_path, 'w') as f:
        f.write(contents)

    # Read/write priveleges for everyone
    os.chmod(file_path, 0666)


def get_script_path(flag_number):
    return os.path.join(USER_HOME_DIR, 'flag_%d.sh' % flag_number)

def create_script(file_path, script_contents):
    write_to_file(file_path, script_contents)

     # Everything for user and group and read plus execute for everyone else
    os.chmod(file_path, 0775)
    
def mkdir(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)
        os.chmod(directory, 0777) # Allows anyone to move the files in the directory

def rm(file):
    if os.path.exists(file):
        os.remove(file)

def rmdir(directory):
    if os.path.exists(directory):
        os.rmdir(directory)

def rmdir_and_contents(directory):
    if os.path.exists(directory):
        shutil.rmtree(directory)

# Returns a dictionary with the following format: {'all_files': [<file paths>], 'flag_file': <flag file path>}
def get_flag_8_filenames():
    filepaths = []
    for i in range(1, FLAG_8_NUMBER_OF_FILES + 1):
        filepath = os.path.join(FLAG_8_DIRECTORY, FLAG_8_FILENAME_TEMPLATE % i)
        filepaths.append(filepath)

    return {'all_files': filepaths, 'flag_file': filepaths[FLAG_8_FILE_NUMBER - 1]}
