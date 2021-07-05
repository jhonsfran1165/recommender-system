def main():
    f=open("../../OriginalFiles/authors.txt","r")
    if f.mode == 'r':
        contents =f.read()
        print(contents)

main()