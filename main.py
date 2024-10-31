file = open("U1rez.txt","w")
file.write("print the results of the calculated distance")
print(file.write)
file.close()


# Open the file, write data, then read and print it
with open("U1.txt", "w+") as file:
    file.write(data)  # Write the provided data to the file
    file.seek(0)  # Move the cursor back to the beginning
    print(file.read())  # Read and print the file contents


def calculate_total_distance_and_count():

    # Dictionary to store total distance and count per class ID
    class_results = {}

    # Process each student's data
    for class_id, step_length, steps_per_day in student_data:
        # Calculate total steps for all students, including those who did not participate (some days may have 0 steps)
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