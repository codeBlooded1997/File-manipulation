# For accessing and writing data in the file
import static_data
# For generating random date
import datetime
# For picking random data form static_data file
import random
# For creating random characters in file names
import string
# For controlling the operating system(moving and deleting files and ...)
import os

def generate_reports(num):

    for current_num in range(num):
        """
        This function reads existing data from the static_data files
        and uses the data to generate random file.
        """
        # Generate the right filename of the correct length
        file_name = str(current_num + 1).zfill(3) + '_report.txt'   # zfill() populates with zero

        # Create the file, in the write mode
        f = open(file_name, 'w')

        # Generate all of the text content of our dummy report files
        date = str(datetime.date(2019,1,1) + datetime.timedelta(random.randint(1,365)))

        # Chosing 10 random eomployee names from static_data files
        employee = random.choice(static_data.names)

        # Choosing 10 random ongoing task form the static_data file
        ongoing_tasks = '\t' + random.choice(static_data.ongoing_tasks) + '\n' \
                        '\t' + random.choice(static_data.ongoing_tasks) + '\n'

        completed_tasks = '\t' + random.choice(static_data.completed_tasks) + '\n' \
                          '\t' + random.choice(static_data.completed_tasks) + '\n'

        problems = '\t' + random.choice(static_data.problems) + '\n' \
                   '\t' + random.choice(static_data.problems) + '\n'

        approved_by = random.choice(static_data.names)

        # Fully construnct contetn of dummy report file
        report_content = 'MARIO OFFICE REPORT\n\n' + \
                         'Date: '               + date + '\n\n' + \
                         'Employee: '           + employee + '\n\n' + \
                         'Ongoing Tasks:\n'     + ongoing_tasks + '\n' + \
                         'Completed Tasks:\n'   + completed_tasks + '\n' + \
                         'Problems:\n'          + problems + '\n' + \
                         'Approved By: '        + approved_by

        # Write the content to the file
        f.write(report_content)

def generate_bloat(num):
    """
    This function generates bloat files so it seems more
    realistic when we want to manipulate the files later.
    """

    for current_num in range(num):

        file_name = str(random.randint(1,num)).zfill(3) + \
                    '_bloatfile_' + \
                    ''.join(random.choices(string.ascii_lowercase, k=5)) + \
                    '.txt'

        f = open(file_name, 'w')
        f.write('Trollollolol ;)')

def delete_files():
    """
    This function delets the files with .txt extention.
    """
    for file_name in os.listdir(os.getcwd()):   # getcwd : get Current Working Directory
        if file_name.endswith('.txt'):      # endswith() looks at the files endings
            os.remove(file_name)
#generate_reports(10)
#generate_bloat(5)
delete_files()
