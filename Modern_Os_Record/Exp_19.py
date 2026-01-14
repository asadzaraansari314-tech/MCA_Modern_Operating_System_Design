class File:
    def __init__(self, name, content=""):
        self.name = name
        self.content = content

class Directory:
    def __init__(self, name):
        self.name = name
        self.files = {}
        self.subdirs = {}

class VirtualFileSystem:
    def __init__(self):
        self.root = Directory("root")
        self.current_dir = self.root
        self.path_stack = ["root"]

    def mkdir(self, dirname):
        if dirname in self.current_dir.subdirs:
            print(f"Directory {dirname} already exists.")
        else:
            self.current_dir.subdirs[dirname] = Directory(dirname)
            print(f"Directory {dirname} created.")

    def ls(self):
        print("Directories:", list(self.current_dir.subdirs.keys()))
        print("Files:", list(self.current_dir.files.keys()))

    def cd(self, dirname):
        if dirname == "..":
            if len(self.path_stack) > 1:
                self.path_stack.pop()
                self.current_dir = self.root
                for d in self.path_stack[1:]:
                    self.current_dir = self.current_dir.subdirs[d]
        elif dirname in self.current_dir.subdirs:
            self.current_dir = self.current_dir.subdirs[dirname]
            self.path_stack.append(dirname)
        else:
            print(f"Directory {dirname} does not exist.")

    def create_file(self, filename, content=""):
        if filename in self.current_dir.files:
            print(f"File {filename} already exists.")
        else:
            self.current_dir.files[filename] = File(filename, content)
            print(f"File {filename} created.")

    def write_file(self, filename, content):
        if filename in self.current_dir.files:
            self.current_dir.files[filename].content = content
            print(f"Written to file {filename}.")
        else:
            print(f"File {filename} not found.")

    def read_file(self, filename):
        if filename in self.current_dir.files:
            print(f"Content of {filename}:\n{self.current_dir.files[filename].content}")
        else:
            print(f"File {filename} not found.")

    def pwd(self):
        print("/" + "/".join(self.path_stack))


# Simulation
vfs = VirtualFileSystem()

# Commands
vfs.mkdir("docs")
vfs.mkdir("images")
vfs.ls()

vfs.cd("docs")
vfs.create_file("file1.txt", "Hello, this is file1.")
vfs.create_file("file2.txt", "This is file2.")
vfs.ls()
vfs.read_file("file1.txt")
vfs.write_file("file2.txt", "Updated content for file2.")
vfs.read_file("file2.txt")
vfs.pwd()

vfs.cd("..")
vfs.pwd()
vfs.ls()
