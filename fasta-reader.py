def fasta(file):
    dot_name = os.path.basename(file)[os.path.basename(file).find('.'):]
    if dot_name == '.fa' or dot_name == '.fasta':
        with open(file, 'r') as f:
            data = f.readlines()
        seq = []
        for line in range(len(data)):
            if data[line].startswith('>'):
                seq.append(data[line + 1])
        return seq
    else:
        print('Invalid format')
        exit()
