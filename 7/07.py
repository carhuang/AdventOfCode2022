"""
Day 7: No Space Left On Device
Thank you galaxyinferno.com for providing essential advice on the solution!
"""

# read the input
with open('./input.txt', 'r') as f:
    lines = f.readlines()
    terminal_output = [entry.strip() for entry in lines]

class DirNode:
    def __init__(self, name, is_dir: bool, size=None):
        self.name = name
        self.is_dir = is_dir
        self.size = size
        self.children = []
        self.parent = None
    def add_child(self, child):
        child.parent = self
        self.children.append(child)
    def get_size(self):
        if self.size:
            return self.size
        else:
            total_size = 0
            for child in self.children:
                total_size += child.get_size()
            self.size = total_size # memoize the size of visited directory
            return total_size
    def find_subdirectories_part1(self):
        subdir_size = 0
        if self.is_dir:
            for child in self.children:
                if child.is_dir and child.get_size() <= 100000:
                    subdir_size += child.get_size() + child.find_subdirectories_part1()
                else:
                    subdir_size += child.find_subdirectories_part1()
        return subdir_size
    def find_subdirectory_part2(self, min_size):
        min_subdir_size = 70000000
        if self.is_dir:
            for child in self.children:
                if child.is_dir and child.get_size() >= min_size:
                    min_subdir_size = min(min_subdir_size, child.get_size(), child.find_subdirectory_part2(min_size))
                else:
                    min_subdir_size = min(min_subdir_size, child.find_subdirectory_part2(min_size))
        return min_subdir_size

class Directory:
    def __init__(self):
        self.root = DirNode(name="/", is_dir=True)
        self.current = self.root
    def reset_to_root(self):
        self.current = self.root
    def go_up_one_level(self):
        self.current = self.current.parent
    def go_to_child(self, name):
        for child in self.current.children:
            if child.name == name:
                self.current = child

directory = Directory()

def build_directory_tree():
    idx = 0 
    while idx < len(terminal_output):
        line = terminal_output[idx]
        if line[0] == '$':
            if line == '$ ls':
                pass
            else:
                _, _, name = line.split()
                if name == '/':
                    directory.reset_to_root()
                elif name == '..':
                    directory.go_up_one_level()
                else:
                    directory.go_to_child(name)
        else:
            size, name = line.split()
            if size == 'dir':
                new_node = DirNode(name=name, is_dir=True)
            else:
                new_node = DirNode(name=name, is_dir=False, size=int(size))
            directory.current.add_child(new_node)
        idx += 1

def part1():
    build_directory_tree()
    total_size = directory.root.find_subdirectories_part1()
    return total_size

def part2():
    total_disk_space = 70000000
    min_space_needed = 30000000
    min_disk_size = min_space_needed - (total_disk_space - directory.root.get_size())
    size = directory.root.find_subdirectory_part2(min_disk_size)
    return size

print(part1())
print(part2())