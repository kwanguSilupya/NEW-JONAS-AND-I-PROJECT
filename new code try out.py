# Open U1rez.txt and write initial text
with open("U1rez.txt", "w") as file:
    file.write("Printing the results of the calculated distance\n")

# Write some initial data to U1.txt (for demonstration only)
with open("U1.txt", "w+") as file:
    file.write(
        "10\n"
        "7 76 4353 8738 4946 6484 8946 6336 6284\n"
        "11 74 4352 4578 7239 3157 7856 4648 5850\n"
        "6 70 5731 9017 7641 6785 8865 3184 6800\n"
        "5 68 9147 9702 8671 0 5398 9555 7141\n"
        "8 71 7550 0 9089 8446 4390 0 7901\n"
        "7 68 4227 7160 9565 3297 4401 5740 6908\n"
        "7 73 6362 6705 0 9017 5971 3154 3585\n"
        "6 73 7053 8752 7606 4079 5204 3819 3310\n"
        "5 73 4263 5836 3336 5401 4719 0 0\n"
        "8 71 8588 5617 6903 9565 6445 6786 4522\n"
    )
    file.seek(0)
    print("Contents of U1.txt:\n" + file.read())

# Define the function to calculate total distance and student count
def calculate_total_distance_and_count():
    # Dictionary to store total distance and count per class ID
    class_results = {}

    # Read data from U1.txt
    with open("U1.txt", "r") as file:
        lines = file.readlines()

    # Process each line of data (skip the first line if needed)
    for line in lines[1:]:
        # Parse the line
        data = list(map(int, line.strip().split()))
        class_id, step_length = data[0], data[1]
        steps_per_day = data[2:]

        # Calculate total steps and distance for each student
        total_steps = sum(steps_per_day)
        total_distance = (total_steps * step_length) / 100000  # Convert to kilometers

        # Update class totals
        if class_id not in class_results:
            class_results[class_id] = {"students": 0, "distance": 0.0}
        class_results[class_id]["students"] += 1
        class_results[class_id]["distance"] += total_distance

    # Write results to U1rez.txt
    with open("U1rez.txt", "w") as result_file:
        for class_id, result in class_results.items():
            # Write class ID, number of students, and total distance (rounded to 2 decimal places)
            result_file.write(f"{class_id} {result['students']} {round(result['distance'], 2)}\n")

    # Also print the results to the console
    for class_id, result in class_results.items():
        print(
            f"Class ID: {class_id}, Students: {result['students']}, "
            f"Total Distance: {round(result['distance'], 2)} km"
        )

# Call the function
calculate_total_distance_and_count()