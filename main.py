file = open("U1rez.txt","w")
file.write("print the results of the calculated distance")
print(file.write)
file.close()

data = """
The number of students who participated in the campaign:
{10, 7, 76, 4353, 8738, 4946, 6484, 8946, 6336, 6284,
11, 74, 4352, 4578, 7239, 3157, 7856, 4648, 5850,
6, 70, 5731, 9017, 7641, 6785, 8865, 3184, 6800}

Student data: class ID; step length in centimeters;
the number of steps taken each day of the campaign week:
{5, 68, 9147, 9702, 8671, 0, 5398, 9555, 7141,
8, 71, 7550, 0, 9089, 8446, 4390, 0, 7901,
7, 68, 4227, 7160, 9565, 3297, 4401, 5740, 6908,
7, 73, 6362, 6705, 0, 9017, 5971, 3154, 3585,
6, 73, 7053, 8752, 7606, 4079, 5204, 3819, 3310}

A value of 0 indicates that the student did not enter data for that day:
{5, 73, 4263, 5836, 3336, 5401, 4719, 0, 0,
8, 71, 8588, 5617, 6903, 9565, 6445, 6786, 4522}
"""

# Open the file, write data, then read and print it
with open("U1.txt", "w+") as file:
    file.write(data)  # Write the provided data to the file
    file.seek(0)  # Move the cursor back to the beginning
    print(file.read())  # Read and print the file contents


def calculate_total_distance_and_count():
    # Student data for class categories (class ID, step length, steps per day)
    student_data = [
        (5, 68, [9147, 9702, 8671, 0, 5398, 9555, 7141]),
        (8, 71, [7550, 0, 9089, 8446, 4390, 0, 7901]),
        (7, 68, [4227, 7160, 9565, 3297, 4401, 5740, 6908]),
        (7, 73, [6362, 6705, 0, 9017, 5971, 3154, 3585]),
        (6, 73, [7053, 8752, 7606, 4079, 5204, 3819, 3310]),
        (5, 73, [4263, 5836, 3336, 5401, 4719, 0, 0]),
        (8, 71, [8588, 5617, 6903, 9565, 6445, 6786, 4522])
    ]

    # Dictionary to store total distance and count per class ID
    class_results = {}

    # Process each student's data
    for class_id, step_length, steps_per_day in student_data:
        if 0 not in steps_per_day:  # Only include students with data for all days
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
            f"Class ID: {class_id}, Students: {result['students']}, Total Distance: {round(result['distance'], 2)} km")


# Call the function
calculate_total_distance_and_count()