import os
import subprocess
import re

# Pull in the common constants and helper functions
import common

def remove_flag_1():
    common.rm(common.FLAG_FILE_1)

def remove_flag_2():
    common.rm(common.FLAG_FILE_2)

def remove_flag_3():
    common.rm(common.FLAG_FILE_3)

def remove_flag_4():
    common.rm(common.FLAG_4_LINK_NAME)
    common.rm(common.FLAG_FILE_4)

def remove_flag_5():
    common.rm(common.FLAG_FILE_5)

def remove_flag_6():
    common.rm(common.FLAG_FILE_6)

def remove_flag_7():
    common.rm(common.FLAG_FILE_7)

def remove_flag_8():
    filenames_dict = common.get_flag_8_filenames()
    files_to_remove = filenames_dict['all_files']

    for filepath in files_to_remove:
       common.rm(filepath)
    
    common.rmdir(common.FLAG_8_DIRECTORY)

def remove_flag_9():
    common.rm(common.FLAG_FILE_9)

def remove_flag_10():
    common.rm(common.FLAG_FILE_10_ORIGINAL_PATH)
    common.rm(common.FLAG_FILE_10_DESIRED_PATH)
    common.rm(common.get_script_path(10))
    common.rmdir(common.FLAG_10_DIRECTORY)

def remove_flag_11():
    common.rm(common.get_script_path(11))
    common.rm(common.FLAG_11_BOULDER)

def remove_flag_12():
    common.rm(common.get_script_path(12))
    common.rmdir(common.FLAG_12_DIRECTORY)

def remove_flag_13():
    common.rm(common.get_script_path(13))
    common.rm(common.FLAG_13_THING_1)
    common.rm(common.FLAG_13_THING_2)

def remove_flag_14():
    common.rm(common.get_script_path(14))

def remove_flag_15():
    common.rm(common.FLAG_FILE_15)
    common.rm(common.FLAG_FILE_15_COMPRESSED)

def remove_flag_16():
    common.rm(common.get_script_path(16))

def remove_flag_17():
    common.rm(common.get_script_path(17))
    common.rm(common.FLAG_FILE_17_INPUT_FILE)

def remove_flag_18():
    for box_num in common.FLAG_18_BOX_NUMS:
        subdir = "box_%d" % (box_num)
        subdir_path = os.path.join(common.FLAG_DIRECTORY_18_ROOT, subdir)
        common.rmdir_and_contents(subdir_path)

    common.rmdir_and_contents(common.FLAG_DIRECTORY_18_ROOT)

def remove_flag_19():
    common.rm(common.FLAG_FILE_19)

def remove_flag_20():
    common.rm(common.FLAG_FILE_20)

def remove_flag_21():
    common.rm(common.FLAG_FILE_21)

def remove_flag_22():
    common.rm(common.FLAG_FILE_22)

def remove_flag_23():
    common.rm(common.get_script_path(23))

def remove_flag_24():
    common.rm(common.get_script_path(24))

def remove_flag_25():
    common.rm(common.FLAG_25_PROCESS_SCRIPT)
    common.rm(common.FLAG_25_SCRIPT)

    # Kill any and all processes started by the flag 25 script
    all_processes = subprocess.check_output(['ps', 'aux']).strip().split('\n')
    bill_process_pattern = re.compile("^.*/bin/sh /tmp/bill.sh$")
    bill_process_lines = [ process_info for process_info in all_processes if bill_process_pattern.match(process_info) ]
    bill_pids = [ line.split()[1] for line in bill_process_lines ]
    [ subprocess.check_output(['kill', pid]) for pid in bill_pids ]

###
### Begin script execution
###

common.quit_if_not_root()

cleaning_functions = filter(lambda x: x.startswith("remove_flag_"), locals())

for func_name in cleaning_functions:
    locals()[func_name]()

common.rm(common.HINTS_FILE)
