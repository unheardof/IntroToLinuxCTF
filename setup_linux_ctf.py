import base64
import os
import binascii
import subprocess
import random

# Pull in the common constants and helper functions
import common

ORDERED_FLAGS = [ "14a15eff3d54b4cc17d7467f3d60bfa8",
                  "e60cdc332b773c8cbdb3125d923862eb",
                  "968e96d318ad1d755268ff566b514fac",
                  "1b300af8e00fed12d5b9bbb189bc4766",
                  "e1d7462a4a091de52137279602d8b9c1",
                  "22e0443c1fbc54f646f08ef6f37c2014",
                  "620b59a6c9a8751a5437ced2acb97d83",
                  "4fa0df5ebbf1d416d9e82ad6715255c3",
                  "6d44080c36d4be4e52b31cd52346aaef",
                  "9ef853ca5fc74b817351adaa1dd5cc39",
                  "f8368bbc48d1c24b2321b26067e91927",
                  "335ce221120c49006df97c546ddaff42",
                  "b4d616f075d9e957426dbd2e2217587d",
                  "ffe5086f8ad902d3954993186bac4cb1",
                  "77bfededbf91888e5d67467547ead72d",
                  "21617ae04c2ad40a4faefe2df688b755",
                  "71b101e6ade6daba356b6bc63c20d44c",
                  "8fcce0e7e4abecadaf646c89ac043381",
                  "b34ce27577e3bd1b8a23b62476892e1b",
                  "18b190bdf56fb20c1c620851a33ecef3",
                  "a4748e789ca194eaee41390ba1b78b5d",
                  "cf4a3de914aef344a9f95d3ab66fe0ee",
                  "b2eec79abe630d42302d5208459f5acf",
                  "790bd0f329cdd4f6f957b6bffb24ea5c",
                  "0b1bd73344376dc00bd736bb946b340b",
                  ]

# TODO: Create an interface for getting to all of the flag hints (?)
#       Otherwise, provide a starting point that gives the first hint and have each subsequent flag also provide the next hint

# TODO: Make sure all hints are exposed to the user (probably through the web server client)
FLAG_HINTS = [
    "Find this one fast; it is only here temporarily",
    "They're making a list of /usr/var, and checking it twice, but without the right approach, the flag will be missed",
    "There's no place like home for finding flags",
    "Finding this flag is a symbolic victory",
    "Things (and files) are not always what they seem; let your sight be an *extension* of your senses, and do not let yourself be *misdirected*",
    "Venture up along your (relative) path, young adventurer, in order find your next flag (hint: you must take a step up from your home)",
    "Knowing how to search through a file will save you a lot of *manual* effort",
    "It's hard to see the forest through the trees, or the flag",
    "This one is sure to vex you, or is it hex you?",
    "Jim is in the_ocean and just wants to go home.",
    "In order to get to this flag, you must first remove the boulder",
    "For this one, you'll need to get rid of that box",
    "thing_1 is identical to thing_2, except for the name; once thing_2 appears, this flag will be revealed",
    "The script for this flag is very argumentative, but once you agree on how to use it, you will find what you seek",
    "tar is sticky, and also hard to search through; if only there were a way to get rid of it",
    "This file really wants to be run as a script; in return, it has promised to give you a flag",
    "The input.txt file is what you need in order to get to this flag, but first you must fix the typo in it",
    "*find* the file named flag_18.txt; I swear it is around here somewhere",
    "This flag is in the same place as the system scripts; a good place to start is finding out *which* 'ls' command you're using.",
    "You will need to use your super(user) powers to get to this flag",
    "If a log file is written to when no one is around to hear it, does it still contain a flag?",
    "Strings of binary data can be difficult to sort through, unless you use the right tool",
    "I need to know where you are in order to give you this flag (hint: I need your address)",
    "Hi. I'm your host! I can't remember my name; can you tell me what it is?",
    "Kill Bill; hint: he's running around in the background"
]
    
###
### Helper Functions
###

def get_flag(flag_number):
    return ORDERED_FLAGS[flag_number - 1]

def get_formatted_flag_line(flag_number):
    return "flag #%d: %s\n" % (flag_number, get_flag(flag_number))

def get_hint_for_flag(flag_number):
    return FLAG_HINTS[flag_number - 1]

def obfuscate_shell_script(script_contents):
    obfuscated_contents = base64.b64encode(script_contents)
    return """#!/bin/sh
    echo "%s" | base64 -d | bash
    """ % (obfuscated_contents)

def generate_flag_10_script_contents():
    return """
    [ ! -f %s ] && [ -f %s ] && echo "%s" && exit
    echo "%s"
    """ % (common.FLAG_FILE_10_ORIGINAL_PATH, common.FLAG_FILE_10_DESIRED_PATH, get_formatted_flag_line(10).strip(), get_hint_for_flag(10))

def generate_flag_11_script_contents():
    return """
    [ ! -f %s ] && echo "%s" && exit
    echo "%s"
    """ % (common.FLAG_11_BOULDER, get_formatted_flag_line(11).strip(), get_hint_for_flag(11))

def generate_flag_12_script_contents():
    return """
    [ ! -d %s ] && echo "%s" && exit
    echo "%s"
    """ % (common.FLAG_12_DIRECTORY, get_formatted_flag_line(12).strip(), get_hint_for_flag(12))

def generate_flag_13_script_contents():
    return """
    [ -f %s ] && [ -f %s ] && [ "$( diff %s %s )" == "" ] && echo "%s" && exit
    echo "%s"
    """ % (common.FLAG_13_THING_1, common.FLAG_13_THING_2, common.FLAG_13_THING_1, common.FLAG_13_THING_2, get_formatted_flag_line(13).strip(), get_hint_for_flag(13))

def generate_flag_14_script_contents():
    return """
    echo ""

    if [[ $1 == "-h" ]] || [[ $1 == "--help" ]]; then
        echo "Usage: must provide the --flag script argument"
    elif [[ $1 == "--flag" ]]; then
        echo "Flag is $( echo '%s' | base64 -d )"
    else
        echo "Do you need --help?"
    fi

    echo ""
    """ % (base64.b64encode(get_formatted_flag_line(14).strip()))

def generate_flag_16_script_contents():
    return """
    echo "%s"
    """ % (get_formatted_flag_line(16).strip())

def generate_flag_17_script_contents():
    return """
    echo ""
    
    if grep -q "typo" %s; then
        echo "There is still a typo in the input file. Please remove it in order to get to the flag."
    else
        echo "%s"
    fi

    echo ""
    """ % (common.FLAG_FILE_17_INPUT_FILE, get_formatted_flag_line(17).strip())

def generate_flag_23_script_contents():
    return """
    IP=$( ifconfig eth0 | grep "inet addr" | awk '{print $2}' | awk -F ':' '{print $2}' )

    if [ "$1" == $IP ]; then
        echo "%s" | base64 -d; echo ''
    else
        echo "Please provide your host IP address as the only parameter to the script"
    fi
    """ % (base64.b64encode(get_formatted_flag_line(23).strip()))

def generate_flag_24_script_contents():
    return """
    if [[ $1 == `hostname` ]]; then
        echo "%s" | base64 -d; echo ''
    else
        echo '%s'
    fi
    """ % (base64.b64encode(get_formatted_flag_line(24).strip()), get_hint_for_flag(24))

def generate_flag_25_start_process_script_contents():
    # Doesn't need to do anything; it just needs to keep running until it is explicitly stopped
    return """#!/bin/sh

    while true
    do
        sleep 500
    done
    """

def generate_flag_25_script_contents():
    return """
    if [[ -z $( ps aux | grep 'bill.sh' | grep -v grep ) ]]; then
        echo "%s"
    else
        echo "%s"
    fi;
    """ % (get_formatted_flag_line(25).strip(), get_hint_for_flag(25))

###
### Flag Staging Functions
###

def stage_flag_1():
    common.write_to_file(common.FLAG_FILE_1, get_formatted_flag_line(1))

def stage_flag_2():
    common.mkdir('/usr/var')
    common.write_to_file(common.FLAG_FILE_2, get_formatted_flag_line(2))

def stage_flag_3():
    common.write_to_file(common.FLAG_FILE_3, get_formatted_flag_line(3))

def stage_flag_4():
    with open(common.FLAG_FILE_4, 'w') as f:
        f.write(get_formatted_flag_line(4))

    os.symlink(common.FLAG_FILE_4, common.FLAG_4_LINK_NAME)

def stage_flag_5():
    common.write_to_file(common.FLAG_FILE_5, get_formatted_flag_line(5))

def stage_flag_6():
    common.write_to_file(common.FLAG_FILE_6, get_formatted_flag_line(6))

def stage_flag_7():
    with open(common.FLAG_7_SOURCE_FILE, 'r') as f:
        file_lines = f.read().splitlines()

    num_lines = len(file_lines)
    flag_injection_location = (num_lines / 3) * 2
    file_lines.insert(flag_injection_location, get_formatted_flag_line(7))
    common.write_to_file(common.FLAG_FILE_7, "\n".join(file_lines))

def stage_flag_8():
    common.mkdir(common.FLAG_8_DIRECTORY)
    filenames_dict = common.get_flag_8_filenames()
    files_to_create = filenames_dict['all_files']
    flag_file = filenames_dict['flag_file']

    for filepath in files_to_create:
        common.write_to_file(filepath, "duck\n")

    # Overwrite the contents of the flag file
    common.write_to_file(flag_file, "goose\n" + get_formatted_flag_line(8))

def stage_flag_9():
    flag_line = binascii.hexlify(get_formatted_flag_line(9).strip() + "\n")
    common.write_to_file(common.FLAG_FILE_9, flag_line)

def stage_flag_10():
    common.mkdir(common.FLAG_10_DIRECTORY)
    common.write_to_file(common.FLAG_FILE_10_ORIGINAL_PATH, get_hint_for_flag(10))
    common.create_script(common.get_script_path(10), obfuscate_shell_script(generate_flag_10_script_contents()))

def stage_flag_11():
    common.write_to_file(common.FLAG_11_BOULDER, "This is a boulder")
    common.create_script(common.get_script_path(11), obfuscate_shell_script(generate_flag_11_script_contents()))

def stage_flag_12():
    common.mkdir(common.FLAG_12_DIRECTORY)
    common.create_script(common.get_script_path(12), obfuscate_shell_script(generate_flag_12_script_contents()))

def stage_flag_13():
    common.write_to_file(common.FLAG_13_THING_1, "This is a Thing")
    common.create_script(common.get_script_path(13), obfuscate_shell_script(generate_flag_13_script_contents()))

def stage_flag_14():
    # Deliberately only obfuscate part of this script
    common.create_script(common.get_script_path(14), generate_flag_14_script_contents())

def stage_flag_15():
    common.write_to_file(common.FLAG_FILE_15, get_formatted_flag_line(15))
    subprocess.check_output(['tar', '-czvf', common.FLAG_FILE_15_COMPRESSED_NAME, common.FLAG_FILE_15_NAME], cwd=common.USER_HOME_DIR)
    common.rm(common.FLAG_FILE_15)

def stage_flag_16():
    # Note: we are deliberately writting to the file without execute permissions (since getting the script to execute is the goal of the exercise)
    common.write_to_file(common.get_script_path(16), obfuscate_shell_script(generate_flag_16_script_contents()))

def stage_flag_17():
    common.create_script(common.get_script_path(17), obfuscate_shell_script(generate_flag_17_script_contents()))
    common.write_to_file(common.FLAG_FILE_17_INPUT_FILE, "Here is the 'typo'.\nPlease remove it to get to the flag.")

def stage_flag_18():
    common.mkdir(common.FLAG_DIRECTORY_18_ROOT)

    chosen_box_number = random.choice(common.FLAG_18_BOX_NUMS)
    chosen_box_directory = None
    for box_num in common.FLAG_18_BOX_NUMS:
        subdir = "box_%d" % (box_num)
        subdir_path = os.path.join(common.FLAG_DIRECTORY_18_ROOT, subdir)

        if box_num == chosen_box_number:
            chosen_box_directory = subdir_path
            
        common.mkdir(subdir_path)

    path = os.path.join(chosen_box_directory, common.FLAG_FILE_18_NAME)
    common.write_to_file(path, get_formatted_flag_line(18))

def stage_flag_19():
    common.write_to_file(common.FLAG_FILE_19, get_formatted_flag_line(19))

def stage_flag_20():
    common.write_to_file(common.FLAG_FILE_20, get_formatted_flag_line(20))

    # Restrict read access to root user only (specifically, restrict read
    # access to the owning use, but since the script is being executed as root,
    # the owner of this file will be the root user)
    os.chmod(common.FLAG_FILE_20, 0400) 

def stage_flag_21():
    common.write_to_file(common.FLAG_FILE_21, get_formatted_flag_line(21))

def stage_flag_22():
    binary_file_content = os.urandom(1024 * 1024)
    midpoint = len(binary_file_content) / 2
    file_contents = binary_file_content[:midpoint] + get_formatted_flag_line(22) + binary_file_content[midpoint:]
    common.write_to_file(common.FLAG_FILE_22, file_contents)

def stage_flag_23():
    # Deliberately only obfuscate part of this script
    common.create_script(common.get_script_path(23), generate_flag_23_script_contents())

def stage_flag_24():
    # Deliberately only obfuscate part of this script
    common.create_script(common.get_script_path(24), generate_flag_24_script_contents())

def stage_flag_25():
    common.create_script(common.FLAG_25_PROCESS_SCRIPT, obfuscate_shell_script(generate_flag_25_start_process_script_contents()))
    os.chmod(common.FLAG_25_PROCESS_SCRIPT, 0111) # Make the script executable
    subprocess.Popen([common.FLAG_25_PROCESS_SCRIPT], stdin=None, stdout=None, stderr=None, close_fds=True) # Run the script
    common.create_script(common.FLAG_25_SCRIPT, obfuscate_shell_script(generate_flag_25_script_contents()))

def validate_all_flags():
    # TODO: Validate that all flags are properly staged
    pass

###
### Begin script execution
###

common.quit_if_not_root()

numbered_flag_hints = [ "%d.) %s" % (i + 1, FLAG_HINTS[i]) for i in range(len(FLAG_HINTS)) ]
common.write_to_file(common.HINTS_FILE, "\n".join(numbered_flag_hints))

staging_functions = filter(lambda x: x.startswith("stage_flag_"), locals())

for func_name in staging_functions:
    locals()[func_name]()
