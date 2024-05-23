import os

def find(path, filename):
    """Find all paths of files with given name
    Arguments:
    -path -- path to start the search
    -filename -- name of file to search (with extension name)
    Returns: list of all paths"""
    pts = []
    for file in os.listdir(path):
        os.chdir(path)
        if os.path.isfile(file) and file == filename:
            pts.append(os.path.join(path, filename))
        elif os.path.isdir(file):
            pts += find(os.path.join(path, file), filename)
    return pts


if __name__ == '__main__':
    for path in find(os.getcwd(), 'tak.txt'): #podmiana wpisanej na sztywno ścieżki na os.getcwd()
        print(path.replace(os.getcwd(), ''))  #os.sep.join() w tym przypadku według mnie jest niepotrzebne,
                                              #bo os.path.join() również generuję odpowiednie separatory dla aktualnego systemu