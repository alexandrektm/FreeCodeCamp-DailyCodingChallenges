def number_of_files(file_size, file_unit, drive_size_gb):

    if file_unit == "B":
        drive_size_gb=drive_size_gb*1000000000
        result = drive_size_gb//file_size
    if file_unit == "KB":
        drive_size_gb=drive_size_gb*1000000
        result = drive_size_gb//file_size
    if file_unit == "MB":
        drive_size_gb=drive_size_gb*1000
        result = drive_size_gb//file_size

    return result
