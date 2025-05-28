try:
   user=input("Enter text to write to the file: ")
   file1=open('output.txt','w')
   file1.write(user+"\n")
   print("Data successfully written to output.txt")

   file1.close()
   append_input=input("Enter additional text to append: ")
   file1=open('output.txt','a')
   file1.write(append_input)
   file1.close()
   print("Data successfully appended.")
   file1=open('output.txt','r')
   print("final content of output.txt")
   reading_file=file1.read()
   print(reading_file)

except FileNotFoundError():
    print("The file output.txt was not found.")
