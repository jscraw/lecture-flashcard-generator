def fileReader():
    with open('data/sample_lecture.txt') as lecture:
        print(lecture.read())
    
fileReader()