# NOTE THAT THIS WAS BUILT TO WORK ONLY ON _MY MACHINE_
# this is built thinking about x86_64 linux architecture, made for educational purposes only

import mirror_parser as mp;

if __name__ == "__main__":

    file_path = '/etc/apt/sources.list'
    
    mirrors = mp.parse_mirror(file_path)

    print(mirrors)
    
