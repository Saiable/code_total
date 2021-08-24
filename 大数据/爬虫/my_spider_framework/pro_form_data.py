
def gen_form_data(infile ='FormData.txt',outfile='settings.py'):
    with open(infile,'r',encoding='utf-8') as fr:
        lines = fr.readlines()
        DATA = []
        DATA.append('\nDATA = {\n')
        with open(outfile,'a+',encoding='utf-8') as fw:
            for line in lines:
                res = line.strip().split(':')
                temp = '\t"' + res[0].strip() + '": "' + res[1].strip() + '",\n'
                DATA.append(temp)
            DATA.append('}\n')
            fw.writelines(DATA)

gen_form_data()

