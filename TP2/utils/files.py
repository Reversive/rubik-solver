
def read_numbers_from_file(file_path, rows_per_number, columns_per_number):
    inputs = []
    with open(file_path) as f:
        lines = f.readlines()
        i = 0
        while i < len(lines):
            inputs.append([]) # new number

            for row in range(rows_per_number):
                # read all rows of this number
                line_numbers = lines[i].strip().split(" ")
                for column in range(columns_per_number):
                    inputs[-1].append(int(line_numbers[column]))

                i += 1
                if i > len(lines):
                    raise Exception("Invalid file format")
                    break

    f.close()
    return inputs