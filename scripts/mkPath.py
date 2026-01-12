# Define pyLine's paths.
def mkPath(path):
    if os.path.isabs(path) == True:
        return os.path.join(rootDir,path.lstrip("/"))
    elif os.path.isabs(path) != True:
        return os.path.join(os.getcwd(),path.lstrip("/"))