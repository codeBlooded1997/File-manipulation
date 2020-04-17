import os

def process_all_reports():
    """
    This function renames the files and removes the
    zeros from the begining of the report files
    """
    # Making a new directory to store the flagged files later
    #os.mkdir('Flagged Files')

    for file_name in os.listdir(os.getcwd()):
        if file_name.endswith('_report.txt'):
            os.rename(file_name, file_name.lstrip('0'))     # Left strip
            # Search the report file
            criteria = "I don't want to automate with python"
            criteria_met = search_for_critieria(file_name, criteria)

            # If reportfile meets criteria
            if criteria_met == True:

                # Process that file
                process_report(file_name)

def search_for_critieria(file_name, criteria):
    """
    This will search every report file
    to see if it meets The criteria.
    If it does, it will return True,
    If it doesn't it will return False.
    """
    # Openning the file
    f = open(file_name)
    # Reading the file's text
    text_of_file = f.read()     # read() Reads the file's text and return the text
    # Cheking if the criteria is in the file's text
    if criteria in text_of_file:
        return True
    else:
        return False


def process_report(file_name):
    return


process_all_reports()
