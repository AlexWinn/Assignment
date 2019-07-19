def main():
    disk_space = open('numbers.txt   ', 'r')

    file_contents = disk_space.read

    disk_space.close()

    print(file_contents)

main()