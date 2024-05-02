def read_col(filename, col_name):
    dataset=[]
    with open(filename) as f:
        lines=f.readlines()
        header=[x.strip() for x in lines[7].split(",")]
        col_idx=header.index(col_name)
        for line in lines[8:38501]:
            tokens=line.strip().split(",")
            if tokens[col_idx]=="":
                dataset.append("")
            else:
                dataset.append(float(tokens[col_idx]))
    return dataset

def read_col_str(filename, col_name):
    dataset=[]
    with open(filename) as f:
        lines=f.readlines()
        header=[x.strip() for x in lines[7].split(",")]
        col_idx=header.index(col_name)
        for line in lines[8:38501]:
            tokens=line.strip().split(",")
            dataset.append(str(tokens[col_idx]))
    return dataset