def get_vertices_from_file(file_name):
    with open(file_name) as f:
        lines = f.readlines()
        parsed_lines = []

        for line in lines:
            parsed_line = [int(item.strip()) for item in line.split()]
            parsed_lines.append(parsed_line)

    return parsed_lines