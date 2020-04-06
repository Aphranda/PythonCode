import exifread


class Define(object):
    def __init__(self, name):
        self.name = name

    def process(self):
        with open(self.name, 'rb') as f:
            print(f)
            tags = exifread.process_file(f)
            print(tags)

if __name__ == "__main__":
    name = r"D:\PythonCode\code\hacker\picture\A.bmp"
    item = Define(name)
    item.process()
