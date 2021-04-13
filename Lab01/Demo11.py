# Exception handling
import sys

def main():
    a = 10
    b = "hello"

    try:
        c = a + b
        raise ImportError('Data type is not matching')

    except:
        print("Is my error: ", ImportError.args, ImportError.name)



if __name__ == "__main__":
    main()