#coding=utf8

def load_table(table, path):
    needed_column = [(line.split()[0], int(line.split()[1])) for line in open(path)]
    return (table[0], table[1], needed_column)

def load_conf(folder):
    '''
    load conf from config dir
    in folder: folder of configs
    ret configs: list[tuple(table, table size, list(needed culumns))]
    '''
    tables_file = folder + 'tables.txt'
    folder_to_process_file = folder + 'folder_to_process.txt'
    tables = [(table.split()[0], int(table.split()[1])) for table in open(tables_file).readlines()]
    configs = []
    for table in tables:
        cpath = folder + table[0] + '_conf.txt'
        configs.append(load_table(table, cpath))
    
    folder_to_process = [line.strip() for line in open(folder_to_process_file).readlines()]
    return configs, folder_to_process

def read_single(columns, file):
    ret = []
    for line in open(file).readlines():
        raw = line.decode('utf-8').split('\t')
        tmp = []
        for col in columns:
            tmp.append(raw[col[1]])
        ret.append(tmp)
    return ret

def save_to_file(data, dest_path, dest):
    import os
    if not os.path.exists(dest_path):
        os.makedirs(dest_path)
    out = open(dest, 'w')
    for row in data:
        tr = [word.encode('utf-8') for word in row]
        out.write('\t'.join(tr)+'\n')
    out.close()

def read_and_filtering(columns, path, dest_path, dest):
    import os
    files = [f for f in os.listdir(path) if f.endswith('.txt')]
    data = []
    for f in files:
        data.extend(read_single(columns, path + f))
    save_to_file(data, dest_path, dest)
    

def datafilter(table, folder, basepath):
    path = basepath + folder + '/' + table[0] + '/'
    dest_path = basepath + folder + '_filtered/'
    dest_file = basepath + folder + '_filtered/' + table[0] + '.txt'
    x = read_and_filtering(table[2], path, dest_path, dest_file)
    

def main():
    tables, folder_to_process = load_conf('../../config/')
    for folder in folder_to_process:
        for table in tables:
            datafilter(table, folder, '../../../data/2016-11-01/')

if __name__ == '__main__':
    main()
