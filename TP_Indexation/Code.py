import os

directory = "C:/Users/adamp/OneDrive/Desktop/Indexation/TP/data"
determinants=['le','cette','mes','quels','tes','quelle','ma','tout','quelles','quel','premier',
   'la','leur','chaque','au','quelle','mon','aux','cinq','ton','ce','vingt','un','sur',
   'ta','sept','cet','ces','des','plusieurs','quel','vos','nos','beaucoup','par','est','à','en','a','pour'
   'leurs','du','une','notre','de','les','votre','quels','troisième','dixième',',',':','?','!','.','(',')']
i=1

for filename in os.listdir(directory):
    if filename.endswith(".txt"):
        with open(os.path.join(directory, filename), "r",encoding='utf-8') as f:
            contents = f.read()
            mots=contents.split()
            mots=[x for x in mots if x.lower() not in determinants and x.isdigit()==False]

        with open('C:/Users/adamp/OneDrive/Desktop/Indexation/TP/reficher{}.txt'.format(i),'w',encoding='utf-8') as f:
            f.write('\n'.join(mots))
    i+=1