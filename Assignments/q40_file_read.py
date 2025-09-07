# Q40. Read content of a file using try, except and finally.

if __name__ == "__main__":
    filename = input("Enter filename to read: ")
    f = None
    try:
        f = open(filename, "r", encoding="utf-8")
        content = f.read()
        print("File content:\n", content, sep="")
    except FileNotFoundError:
        print("File not found.")
    except OSError as e:
        print("OS error:", e)
    finally:
        if f is not None:
            f.close()
            print("File closed.")