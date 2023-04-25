import os


def main():
    border = """
    ##################################################
    #                                                #
    #        Hello from txt to c++ converter!        #
    #                                                #
    ##################################################
    """
    coder_info = """
    ##################################################
    #                                                #
    #                 Coder_Name:                    #
    #                                                #
    #                 It's Moazzam                   #
    #                                                #
    ##################################################
    """
    print(border)

    current_folder = os.getcwd()

    input_folder = os.path.join(current_folder, 'Input')
    if not os.path.exists(input_folder):
        os.mkdir(input_folder)

    output_folder = os.path.join(current_folder, 'Output')
    if not os.path.exists(output_folder):
        os.mkdir(output_folder)

    print("Paste your .txt files into Input Folder")
    print("______________________________________\n")
    paste = input(
        "Have you pasted your files in \"Input\" folder(y/n)? ").lower()

    if paste == 'y':
        for dir_path, dir_names, file_names in os.walk(input_folder):
            for file in file_names:
                if os.path.splitext(file)[-1] == '.txt':
                    input_path = os.path.join(input_folder, file)
                    output_path = os.path.join(
                        output_folder, os.path.splitext(file)[0] + '.cpp')
                    with open(input_path, 'r') as input_file:
                        input_data = input_file.read()
                    with open(output_path, 'w') as output_file:
                        output_file.write(input_data)
            print("Congrats! Your Files has been converted successfully")
    elif paste == 'n':
        print("Please paste your files into Input Folder and restart the application")
    else:
        print("Invalid Option!!!")
    print(coder_info)
    input("Press Enter to exit...")


if __name__ == '__main__':
    main()
