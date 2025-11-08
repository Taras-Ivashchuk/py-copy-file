def copy_file(command: str) -> None:
    tokens = command.split(" ")
    if len(tokens) != 3:
        print("Usage: copy_file(cp f1.txt f2.txt)")
        return

    command, file1, file2 = tokens

    if command != "cp" or file1 == file2:
        print("Usage: copy_file(cp f1.txt f2.txt)")
        return

    try:
        with open(file1, "r") as file_in, open(file2, "w") as file_out:
            for line in file_in.read():
                file_out.write(line)

    except FileNotFoundError:
        print(f"File {file1} not found")
