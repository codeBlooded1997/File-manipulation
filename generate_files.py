import static_data

def generate_reports(num):

    for current_num in range(num):
        # Constructing the file name
        file_name = str(current_num + 1).zfill(3) + '_report.txt'   # zfill() populates with zero
        print(file_name)

generate_reports(15)
