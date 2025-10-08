def send_message(route):

    first_segment : bool = True
    time : float = 0.0

    for segment in route:

        time += segment / 300000

        if first_segment:
            first_segment = False
            continue

        time += 0.5
        
    time = float((f"{time:.4f}").strip("0"))

    return time

print(send_message([300000, 300000]))

