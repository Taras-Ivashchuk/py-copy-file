def copy_file(command: str) -> None:
    tokens = command.split(" ")
    if len(tokens) < 3:
        print("Usage: copy_file(cp f1.txt f2.txt)")
        return

    com, f1, f2 = tokens

    if com != "cp" or f1 == f2:
        print("Usage: copy_file(cp f1.txt f2.txt)")
        return

    try:
        with open(f1, "r") as file_in, open(f2, "w") as file_out:
            for line in file_in.read():
                file_out.write(line)

    except FileNotFoundError:
        print(f"File {f1} not found")
