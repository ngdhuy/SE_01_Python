def main():
    # open file is not exist
    try:
        with open('example1.txt') as file_handler:
            for line in file_handler:
                print(line)
    except:
        print('An error occurred')
    finally:
        print("Read file is completed")


if __name__ == "__main__":
    main()