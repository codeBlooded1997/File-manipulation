import os
import shutil


subdirectory_name = 'Flagged Files'

compression_type = 'zip'

def process_all_reports():
    """
    This function renames the files and removes the
    zeros from the begining of the report files
    """
    # Making a new directory to store the flagged files later

    #if os.path.isdir(subdirectory_name) == False:
    os.mkdir(subdirectory_name)

    for file_name in os.listdir(os.getcwd()):
        if file_name.endswith('_report.txt'):
            # Renaming the file
            os.rename(file_name, file_name.lstrip('0'))     # Left strip
            file_name = file_name.lstrip('0')
            # Search the report file
            criteria = "I don't want to automate with Python"
            # Checkig if it meets the criteria
            criteria_met = search_for_criteria(file_name, criteria)
            # If reportfile meets criteria
            if criteria_met == True:
                # Process that file
                process_report(file_name)

    # Compress subdrectory, because we are done with all report files
    shutil.make_archive(subdirectory_name, compression_type, subdirectory_name)


def search_for_criteria(file_name, criteria):
    """
    This will search every report file
    to see if it meets The criteria.
    If it does, it will return True,
    If it doesn't it will return False.
    """
    # Openning the file
    f = open(file_name)
    # Reading the file's text
    text_of_file = f.read()     # read() Reads the file's text and return the text(Is a really good pair with RegEx)
    # Cheking if the criteria is in the file's text
    if criteria in text_of_file:
        return True
    else:
        return False
    #return

def process_report(file_name):
    f = open(file_name)
    # Reading the file
    lines = f.readlines()   # Including new lines
    # Iterating in lines list
    for line in lines:
        # If line starts with Employee
        if line.startswith('Employee: '):
            # Extracting name from the line
            employee = ' '.join(line.split()[1:])

        if line.startswith('Approved By: '):
            # Extracting name from the line
            approver_employee = ' '.join(line.split()[2:])
    flagged_report_filename = "FLAGGED REPORT - " + employee + ".txt"
    flagged_report = open(flagged_report_filename, 'w')

    flagged_report.write("EMPLOYEES FLAGGED FOR REVIEW. CONSIDER TERMINATION.\n" + \
                         employee.upper() + \
                         "DOESN\'T WANT TO AUTOMATE WITH PYTHON\n" + \
                         approver_employee.upper() + \
                         'APPROVED THIS' + \
                         'COPY OF REPORT: \n\n')

    f = open(file_name)
    flagged_report.write(f.read())

    # Moving the file into the Directory
    os.rename(flagged_report_filename, os.path.join(subdirectory_name, flagged_report_filename))

    return


def delete_files():
    if os.path.isdir(subdirectory_name):
        shutil.rmtree(subdirectory_name)
    if os.path.isfile(subdirectory_name + '.' + compression_type):
        os.remove(subdirectory_name + '.' + compression_type)


delete_files()
#process_all_reports()
