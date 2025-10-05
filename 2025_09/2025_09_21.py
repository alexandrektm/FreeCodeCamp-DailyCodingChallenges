def number_of_videos(video_size, video_unit, drive_size, drive_unit):

    skip = False
    if drive_unit == "GB":
        drive_size = drive_size
    elif drive_unit == "TB":
        drive_size *= 1000
    else:
        result = "Invalid drive unit"
        skip = True

    if skip != True:
        if video_unit == "KB":
            drive_size=drive_size*1000000
            result = drive_size//video_size
        elif video_unit == "MB":
            drive_size=drive_size*1000
            result = drive_size//video_size
        elif video_unit == "GB":
            drive_size=drive_size
            result = drive_size//video_size
        else:
            result = "Invalid video unit"

    return result

print(number_of_videos(2000, "B", 1, "TB"))