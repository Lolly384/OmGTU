from web_parser import WebParser
from file_writer import FileWriter

if __name__ == "__main__":
    parser = WebParser('https://www.omgtu.ru/general_information/the-structure/the-department-of-university.php')
    parser.parse()
    cafedry = parser.get_cafedry()

    writer = FileWriter('cafedry.txt', cafedry)
    writer.write()