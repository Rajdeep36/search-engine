import string
import os
#//...FROM THIS FUNC WE GET ALL UNIQUE DATA_list(STRING) FROM A TXT.FILE...\\\
def read_file(filename):
    b=[]
    c=[]
    with open(filename) as f:
        for line in f:
            line=line.strip()
            a=line.split(" ")
            b+=a
        for elem in b:
            elem=elem.strip(string.punctuation)
            elem=elem.lower()
            if elem=="":
                pass 
            else:
                c.append(elem)
        c=set(c)
        c=list(c)
    return c
#//..FROM THIS FUNC. WE GET ALL ENIQUE DATA_list(STRING) FROM ALL TXT.FILE..\\\
def data_set(filenames):
    d=[]
    for elem in filenames:
        a=read_file(elem)
        d+=a
    data_set=set(d)
    data_set=list(data_set)
    return data_set
##////....TESTING...\\\\
def testing(fienames):
    a=data_set(fienames)
    b=[]
    index={}
    for elem in a:
        index[elem]=b
    c=index
    for elem in fienames:
        d=read_file(elem)
        for elem1 in d:
            if elem1 in c:
                c[elem1]=c[elem1]+[elem]
            else:
                pass
    index=c
    return index

#CREATING TILE TITLES AS A DICT.\\\\
def file_title(filenames):
    file_titles={}
    for elem in filenames:
        with open(elem) as f:
            line=f.readline()
            line=line.strip()
            file_titles[elem]=line

    return  file_titles



#IT GIVES ALL TXT FILE IN A DIRECTORY AS ALIST
def textfiles_in_dir(directory):
    filenames = []
    for filename in os.listdir(directory):
        if filename.endswith('.txt'):
            filenames.append(os.path.join(directory, filename))
    return filenames

#THIS FUNC USE TO FIND THE  USER INPUT QUARY IN OUR DATA SET 
def search(query,index):
    if query.lower() in index:
        c=index[query.lower()]
    else:
        c=[]
    return c
#THIS FUNC GENERATE OUR PROGRAM OUT_PUT
def do_search(index,filetitle):
    while True:
        query=input("ENTER THE QUERY(empty quary to stop): ")
        query=query.lower()
        if query=="":
            break
        result=search(query,index)
        print(f"Result for query {query}: ")
        if result:
            for i in range(len(result)):
                title=filetitle[result[i]]
                print(f"{i+1}.Title: {title},File: {result[i]}")
        else:
            print("No results match that query.")

folder=input("Enter the folder or file name that contain the txt. data files in same directory: ")
files=textfiles_in_dir(folder)
index=testing(files)
filetitle=file_title(files)
main_output=do_search(index,filetitle)



                    