def ReadFile(fileName):
    try:
        file_handle = open(fileName)
        print(file_handle.read())
    except IOError:
        print("File not found or path is incorrect")
    finally:
        file_handle.close()
        print("Read file is completed")


def WriteFile(fileName):
    fruits = ["Orange\n", "Banana\n", "Apple\n"]
    new_file = open(fileName, mode="w", encoding="utf-8")
    new_file.writelines(fruits)
    new_file.close()


def ReadAndWriteFile(fileName):
    fruits = ["Orange_1\n", "Banana 1\n", "Apple 2\n"]
    new_file = open(fileName, mode="a+", encoding="utf-8")
    new_file.writelines(fruits)
    for line in new_file:
        print(line)
    new_file.close()
    print("COMPLETED")


def main():
    ReadFile('example.txt')
    WriteFile('data.txt')
    ReadAndWriteFile('data.txt')

if __name__ == "__main__":
    main()