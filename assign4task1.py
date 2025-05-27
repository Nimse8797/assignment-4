try:
    file1 = open('sample.txt', 'r')
    print("Reading file content.")
    line_number=1
    for line in file1:
        print(f"Line {line_number}:",line)
        line_number+=1

    file1.close()
except FileNotFoundError:
    print("The file sample.txt was not found.")


