def read_col(filename, col_name):
    dataset=[]
    with open(filename) as f:
        lines=f.readlines()
        header=[x.strip() for x in lines[7].split(",")]
        # col_idx=header.index(col_name)
        # for line in lines[8:]:
        #     tokens=line.split(",")
        #     dataset.append(float(tokens[col_idx]))
    print(header)

# def read_col_str(filename, col_name):
#     dataset=[]
#     with open(filename) as f:
#         lines=f.readlines()
#         header=[x.strip() for x in lines[7].split(",")]
#         col_idx=header.index(col_name)
#         for line in lines[8:]:
#             tokens=line.split(",")
#             dataset.append(str(tokens[col_idx]))
#     return dataset

def main():
    filename="./hw14/jeonju_all.csv"
    tmax=read_col(filename, "최고기온(℃)")

if __name__=="__main__":
    main()