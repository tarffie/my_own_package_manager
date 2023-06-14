import mirror_parser as mp;

if __name__ == "__main__":

    file_path = '/etc/apt/sources.list'
    
    mirrors = mp.parse_mirror(file_path)

    print(mirrors)
    
