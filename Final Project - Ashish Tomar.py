#!/usr/bin/env python
# coding: utf-8

# # OPENING AND READING THE TEXT FILE

# In[1]:


text_file=open("E:\\internshala data science course\\COURSE 4-Python for Data Science\\project\\C1-Project-File Handling & String Manipulation-Dataset\\conv.txt","r")


# In[2]:


complete_text=text_file.read()


# In[4]:


text_file.seek(0)


# In[6]:


complete_text_lines=text_file.readlines()


# In[7]:


type(complete_text_lines)


# In[240]:


# NUMBER OF LINES IN THE FILE
no_of_lines=len(complete_text_lines)
no_of_lines


# In[241]:


# PRINTING THE LINES IN TEXT FILE
for line in complete_text_lines:
    print(line)


# In[285]:


# GETTING THE CAHARACTER LIST FROM THE FILE
list_character=[]
for i in range(0,(no_of_lines)):
    character=complete_text_lines[i].split(":")[0]
    list_character.append(character)
    print(character)


# In[286]:


# REMOVING DUPLICATE VALUES FROM LIST OF CHARACTERS
unique_character_set=set(list_character)


# In[287]:


# REMOVING \N BECAUSE OF SPACES BETWEEN INDIVIDUAL LINES
unique_character_set.remove("\n")


# In[288]:


unique_character_set


# In[247]:


# number of unique characters in the conversation
# royce and waymar royce are same character
print("no of unique characters in the conversation is :", format(len(unique_character_set)-1))


# # FUNCTIONS

# In[257]:


# FUNCTION FOR CLEANING UNIQUE WORDS SPOKEN BY CHARACTERS AND PUTTING THEM INTO PROPER FORMAT
def func_cleaning(x):
    for i in range(0,len(x)):
        x[i]=x[i].lower()
        x[i]=x[i].replace("?","")
        x[i]=x[i].replace(",","")
        x[i]=x[i].replace(".","")
        x[i]=x[i].replace(" ","")
        x[i]=x[i].replace("\n","")
        x[i]=x[i].replace("","")
        x[i]=x[i].replace("!","")
        x[i].strip()
        x[i]=x[i].capitalize() 


# # words spoken by unique characters:

# ### ARYA

# In[258]:


ARYA_words=[]
for i in range(0,(no_of_lines)):
               if complete_text_lines[i].split(":")[0].__contains__("ARYA"):
                   ARYA_words.extend(complete_text_lines[i].split(":")[1].split(" ")[1:])


# In[177]:


# no of unique words spoken by ARYA
ARYA_unique_words=set(ARYA_words)
ARYA_unique_words=list(ARYA_unique_words)


# In[259]:


func_cleaning(ARYA_unique_words)


# In[268]:


ARYA_unique_words_set=set(ARYA_unique_words)
print("unique words spoken by ARYA :",sorted(list(ARYA_unique_words_set)))
print("no of unique words spoken by ARYA :", len(ARYA_unique_words_set))


# ### BRAN

# In[261]:


BRAN_words=[]
for i in range(0,(no_of_lines)):
               if complete_text_lines[i].split(":")[0].__contains__("BRAN"):
                   BRAN_words.extend(complete_text_lines[i].split(":")[1].split(" ")[1:])


# In[262]:


# no of unique words spoken by BRAN
BRAN_unique_words=set(BRAN_words)
BRAN_unique_words=list(BRAN_unique_words)


# In[263]:


func_cleaning(BRAN_unique_words)


# In[269]:


BRAN_unique_words_set=set(BRAN_unique_words)
print("unique words spoken by BRAN :",sorted(list(BRAN_unique_words_set)))
print("no of unique words spoken by BRAN :", len(BRAN_unique_words_set))


# ### CASSEL

# In[184]:


CASSEL_words=[]
for i in range(0,(no_of_lines)):
               if complete_text_lines[i].split(":")[0].__contains__("CASSEL"):
                   CASSEL_words.extend(complete_text_lines[i].split(":")[1].split(" ")[1:])


# In[185]:


# no of unique words spoken by CASSEL
CASSEL_unique_words=set(CASSEL_words)
CASSEL_unique_words=list(CASSEL_unique_words)


# In[186]:


func_cleaning(CASSEL_unique_words)


# In[270]:


CASSEL_unique_words_set=set(CASSEL_unique_words)
print("unique words spoken by CASSEL :",sorted(list(CASSEL_unique_words_set)))
print("no of unique words spoken by CASSEL :", len(CASSEL_unique_words_set))


# ### CATELYN

# In[363]:


CATELYN_words=[]
for i in range(0,(no_of_lines)):
               if complete_text_lines[i].split(":")[0].__contains__("CATELYN"):
                   CATELYN_words.extend(complete_text_lines[i].split(":")[1].split(" ")[1:])


# In[364]:


# no of unique words spoken by CATELYN
CATELYN_unique_words=set(CATELYN_words)
CATELYN_unique_words=list(CATELYN_unique_words)


# In[365]:


func_cleaning(CATELYN_unique_words)


# In[366]:


CATELYN_unique_words_set=set(CATELYN_unique_words)
print("unique words spoken by CATELYN :",sorted(list(CATELYN_unique_words_set)))
print("no of unique words spoken by CATELYN :", len(CATELYN_unique_words_set))


# ### CERSEI

# In[375]:


CERSEI_words=[]
for i in range(0,(no_of_lines)):
               if complete_text_lines[i].split(":")[0].__contains__("CERSEI"):
                   CERSEI_words.extend(complete_text_lines[i].split(":")[1].split(" ")[1:])


# In[376]:


# no of unique words spoken by CERSEI
CERSEI_unique_words=set(CERSEI_words)
CERSEI_unique_words=list(CERSEI_unique_words)


# In[377]:


func_cleaning(CERSEI_unique_words)


# In[378]:


CERSEI_unique_words_set=set(CERSEI_unique_words)
print("unique words spoken by CERSEI :",sorted(list(CERSEI_unique_words_set)))
print("no of unique words spoken by CERSEI :", len(CERSEI_unique_words_set))


# ### GARED

# In[379]:


GARED_words=[]
for i in range(0,(no_of_lines)):
               if complete_text_lines[i].split(":")[0].__contains__("GARED"):
                   GARED_words.extend(complete_text_lines[i].split(":")[1].split(" ")[1:])


# In[380]:


# no of unique words spoken by GARED
GARED_unique_words=set(GARED_words)
GARED_unique_words=list(GARED_unique_words)


# In[381]:


func_cleaning(GARED_unique_words)


# In[382]:


GARED_unique_words_set=set(GARED_unique_words)
print("unique words spoken by GARED :",sorted(list(GARED_unique_words_set)))
print("no of unique words spoken by GARED :", len(GARED_unique_words_set))


# ### JAIME

# In[383]:


JAIME_words=[]
for i in range(0,(no_of_lines)):
               if complete_text_lines[i].split(":")[0].__contains__("JAIME"):
                   JAIME_words.extend(complete_text_lines[i].split(":")[1].split(" ")[1:])


# In[384]:


# no of unique words spoken by JAIME
JAIME_unique_words=set(JAIME_words)
JAIME_unique_words=list(JAIME_unique_words)


# In[385]:


func_cleaning(JAIME_unique_words)


# In[386]:


JAIME_unique_words_set=set(JAIME_unique_words)
print("unique words spoken by JAIME :",sorted(list(JAIME_unique_words_set)))
print("no of unique words spoken by JAIME :", len(JAIME_unique_words_set))


# ### JON

# In[387]:


JON_words=[]
for i in range(0,(no_of_lines)):
               if complete_text_lines[i].split(":")[0].__contains__("JON"):
                   JON_words.extend(complete_text_lines[i].split(":")[1].split(" ")[1:])


# In[388]:


# no of unique words spoken by JON
JON_unique_words=set(JON_words)
JON_unique_words=list(JON_unique_words)


# In[389]:


func_cleaning(JON_unique_words)


# In[390]:


JON_unique_words_set=set(JON_unique_words)
print("unique words spoken by JON :",sorted(list(JON_unique_words_set)))
print("no of unique words spoken by JON :", len(JON_unique_words_set))


# ### NED

# In[391]:


NED_words=[]
for i in range(0,(no_of_lines)):
               if complete_text_lines[i].split(":")[0].__contains__("NED"):
                   NED_words.extend(complete_text_lines[i].split(":")[1].split(" ")[1:])


# In[392]:


# no of unique words spoken by NED
NED_unique_words=set(NED_words)
NED_unique_words=list(NED_unique_words)


# In[393]:


func_cleaning(NED_unique_words)


# In[394]:


NED_unique_words_set=set(NED_unique_words)
print("unique words spoken by NED :",sorted(list(NED_unique_words_set)))
print("no of unique words spoken by NED :", len(NED_unique_words_set))


# ### ROBB

# In[395]:


ROBB_words=[]
for i in range(0,(no_of_lines)):
               if complete_text_lines[i].split(":")[0].__contains__("ROBB"):
                   ROBB_words.extend(complete_text_lines[i].split(":")[1].split(" ")[1:])


# In[396]:


# no of unique words spoken by ROBB
ROBB_unique_words=set(ROBB_words)
ROBB_unique_words=list(ROBB_unique_words)


# In[397]:


func_cleaning(ROBB_unique_words)


# In[398]:


ROBB_unique_words_set=set(ROBB_unique_words)
print("unique words spoken by ROBB :",sorted(list(ROBB_unique_words_set)))
print("no of unique words spoken by ROBB :", len(ROBB_unique_words_set))


# ### ROBERT

# In[451]:


ROBERT_words=[]
for i in range(0,(no_of_lines)):
               if complete_text_lines[i].split(":")[0].__contains__("ROBERT"):
                   ROBERT_words.extend(complete_text_lines[i].split(":")[1].split(" ")[1:])


# In[452]:


# no of unique words spoken by ROBERT
ROBERT_unique_words=set(ROBERT_words)
ROBERT_unique_words=list(ROBERT_unique_words)


# In[456]:


func_cleaning(ROBB_unique_words)


# In[457]:


ROBERT_unique_words_set=set(ROBERT_unique_words)
print("unique words spoken by ROBERT :",sorted(list(ROBERT_unique_words_set)))
print("no of unique words spoken by ROBERT :", len(ROBERT_unique_words_set))


# ### ROYCE or WAYMAR ROYCE

# In[403]:


ROYCE_words=[]
for i in range(0,(no_of_lines)):
               if complete_text_lines[i].split(":")[0].__contains__("ROYCE") | complete_text_lines[i].split(":")[0].__contains__("WAYMAR ROYCE"):
                   ROYCE_words.extend(complete_text_lines[i].split(":")[1].split(" ")[1:])


# In[404]:


# no of unique words spoken by ROYCE
ROYCE_unique_words=set(ROYCE_words)
ROYCE_unique_words=list(ROYCE_unique_words)


# In[405]:


func_cleaning(ROYCE_unique_words)


# In[406]:


ROYCE_unique_words_set=set(ROYCE_unique_words)
print("unique words spoken by ROYCE :",sorted(list(ROYCE_unique_words_set)))
print("no of unique words spoken by ROYCE :", len(ROYCE_unique_words_set))


# ### SANSA

# In[407]:


SANSA_words=[]
for i in range(0,(no_of_lines)):
               if complete_text_lines[i].split(":")[0].__contains__("SANSA"):
                   SANSA_words.extend(complete_text_lines[i].split(":")[1].split(" ")[1:])


# In[408]:


# no of unique words spoken by SANSA
SANSA_unique_words=set(SANSA_words)
SANSA_unique_words=list(SANSA_unique_words)


# In[409]:


func_cleaning(SANSA_unique_words)


# In[410]:


SANSA_unique_words_set=set(SANSA_unique_words)
print("unique words spoken by SANSA :",sorted(list(SANSA_unique_words_set)))
print("no of unique words spoken by SANSA :", len(SANSA_unique_words_set))


# ### SEPTA MORDANE

# In[411]:


SEPTA_MORDANE_words=[]
for i in range(0,(no_of_lines)):
               if complete_text_lines[i].split(":")[0].__contains__("SEPTA MORDANE"):
                   SEPTA_MORDANE_words.extend(complete_text_lines[i].split(":")[1].split(" ")[1:])


# In[412]:


# no of unique words spoken by SEPTA_MORDANE
SEPTA_MORDANE_unique_words=set(SEPTA_MORDANE_words)
SEPTA_MORDANE_unique_words=list(SEPTA_MORDANE_unique_words)


# In[413]:


func_cleaning(SEPTA_MORDANE_unique_words)


# In[414]:


SEPTA_MORDANE_unique_words_set=set(SEPTA_MORDANE_unique_words)
print("unique words spoken by SEPTA_MORDANE :",sorted(list(SEPTA_MORDANE_unique_words_set)))
print("no of unique words spoken by SEPTA_MORDANE :", len(SEPTA_MORDANE_unique_words_set))


# ### THEON

# In[415]:


THEON_words=[]
for i in range(0,(no_of_lines)):
               if complete_text_lines[i].split(":")[0].__contains__("THEON"):
                   THEON_words.extend(complete_text_lines[i].split(":")[1].split(" ")[1:])


# In[416]:


# no of unique words spoken by THEON
THEON_unique_words=set(THEON_words)
THEON_unique_words=list(THEON_unique_words)


# In[417]:


func_cleaning(THEON_unique_words)


# In[418]:


THEON_unique_words_set=set(THEON_unique_words)
print("unique words spoken by THEON :",sorted(list(THEON_unique_words_set)))
print("no of unique words spoken by THEON :", len(THEON_unique_words_set))


# ### WILL

# In[419]:


WILL_words=[]
for i in range(0,(no_of_lines)):
               if complete_text_lines[i].split(":")[0].__contains__("WILL"):
                   WILL_words.extend(complete_text_lines[i].split(":")[1].split(" ")[1:])


# In[420]:


# no of unique words spoken by WILL
WILL_unique_words=set(WILL_words)
WILL_unique_words=list(WILL_unique_words)


# In[421]:


func_cleaning(WILL_unique_words)


# In[422]:


WILL_unique_words_set=set(WILL_unique_words)
print("unique words spoken by WILL :",sorted(list(WILL_unique_words_set)))
print("no of unique words spoken by WILL :", len(WILL_unique_words_set))


# # writintg the words into txt files

# ### ARYA

# In[345]:


arya_file=open("E:\\internshala data science course\\COURSE 4-Python for Data Science\\project\\C1-Project-File Handling & String Manipulation-Dataset\\arya_spoken_words_file.txt","a+")


# In[346]:


arya_file.seek(0)
# writing into the above file
for line in list(ARYA_unique_words_set):
    arya_file.writelines(line+"\n")


# In[349]:


arya_file.seek(0)
arya_file.readlines()


# In[356]:


arya_file.close()


# ### BRAN

# In[350]:


bran_file=open("E:\\internshala data science course\\COURSE 4-Python for Data Science\\project\\C1-Project-File Handling & String Manipulation-Dataset\\bran_spoken_words_file.txt","a+")


# In[351]:


bran_file.seek(0)
# writing into the above file
for line in list(BRAN_unique_words_set):
    bran_file.writelines(line+"\n")


# In[352]:


bran_file.seek(0)
bran_file.readlines()


# In[357]:


bran_file.close()


# ### CASSEL

# In[353]:


cassel_file=open("E:\\internshala data science course\\COURSE 4-Python for Data Science\\project\\C1-Project-File Handling & String Manipulation-Dataset\\cassel_spoken_words_file.txt","a+")


# In[354]:


cassel_file.seek(0)
# writing into the above file
for line in list(CASSEL_unique_words_set):
    cassel_file.writelines(line+"\n")


# In[355]:


cassel_file.seek(0)
cassel_file.readlines()


# In[358]:


cassel_file.close()


# ### CATELYN

# In[371]:


catelyn_file=open("E:\\internshala data science course\\COURSE 4-Python for Data Science\\project\\C1-Project-File Handling & String Manipulation-Dataset\\catelyn_spoken_words_file.txt","a+")


# In[372]:


catelyn_file.seek(0)
# writing into the above file
for line in list(CATELYN_unique_words_set):
    catelyn_file.writelines(line+"\n")


# In[373]:


catelyn_file.seek(0)
catelyn_file.readlines()


# In[374]:


catelyn_file.close()


# ### CERSEI

# In[423]:


cersei_file=open("E:\\internshala data science course\\COURSE 4-Python for Data Science\\project\\C1-Project-File Handling & String Manipulation-Dataset\\cersei_spoken_words_file.txt","a+")


# In[424]:


cersei_file.seek(0)
# writing into the above file
for line in list(CERSEI_unique_words_set):
    cersei_file.writelines(line+"\n")


# In[425]:


cersei_file.seek(0)
cersei_file.readlines()


# In[438]:


cersei_file.close()


# ### GARED

# In[426]:


gared_file=open("E:\\internshala data science course\\COURSE 4-Python for Data Science\\project\\C1-Project-File Handling & String Manipulation-Dataset\\gared_spoken_words_file.txt","a+")


# In[427]:


gared_file.seek(0)
# writing into the above file
for line in list(GARED_unique_words_set):
    gared_file.writelines(line+"\n")


# In[428]:


gared_file.seek(0)
gared_file.readlines()


# In[439]:


gared_file.close()


# ### JAIME

# In[429]:


jaime_file=open("E:\\internshala data science course\\COURSE 4-Python for Data Science\\project\\C1-Project-File Handling & String Manipulation-Dataset\\jaime_spoken_words_file.txt","a+")


# In[430]:


jaime_file.seek(0)
# writing into the above file
for line in list(JAIME_unique_words_set):
    jaime_file.writelines(line+"\n")


# In[431]:


jaime_file.seek(0)
jaime_file.readlines()


# In[440]:


jaime_file.close()


# ### JON

# In[432]:


jon_file=open("E:\\internshala data science course\\COURSE 4-Python for Data Science\\project\\C1-Project-File Handling & String Manipulation-Dataset\\jon_spoken_words_file.txt","a+")


# In[433]:


jon_file.seek(0)
# writing into the above file
for line in list(JON_unique_words_set):
    jon_file.writelines(line+"\n")


# In[434]:


jon_file.seek(0)
jon_file.readlines()


# In[441]:


jon_file.close()


# ### NED

# In[435]:


ned_file=open("E:\\internshala data science course\\COURSE 4-Python for Data Science\\project\\C1-Project-File Handling & String Manipulation-Dataset\\ned_spoken_words_file.txt","a+")


# In[436]:


ned_file.seek(0)
# writing into the above file
for line in list(NED_unique_words_set):
    ned_file.writelines(line+"\n")


# In[437]:


ned_file.seek(0)
ned_file.readlines()


# In[442]:


ned_file.close()


# ### ROBB

# In[443]:


robb_file=open("E:\\internshala data science course\\COURSE 4-Python for Data Science\\project\\C1-Project-File Handling & String Manipulation-Dataset\\robb_spoken_words_file.txt","a+")


# In[444]:


robb_file.seek(0)
# writing into the above file
for line in list(ROBB_unique_words_set):
    robb_file.writelines(line+"\n")


# In[445]:


robb_file.seek(0)
robb_file.readlines()


# In[446]:


robb_file.close()


# ### ROBERT

# In[447]:


robert_file=open("E:\\internshala data science course\\COURSE 4-Python for Data Science\\project\\C1-Project-File Handling & String Manipulation-Dataset\\robert_spoken_words_file.txt","a+")


# In[448]:


robert_file.seek(0)
# writing into the above file
for line in list(ROBERT_unique_words_set):
    robert_file.writelines(line+"\n")


# In[449]:


robert_file.seek(0)
robert_file.readlines()


# In[450]:


robert_file.close()


# ### ROYCE

# In[458]:


royce_file=open("E:\\internshala data science course\\COURSE 4-Python for Data Science\\project\\C1-Project-File Handling & String Manipulation-Dataset\\royce_spoken_words_file.txt","a+")


# In[459]:


royce_file.seek(0)
# writing into the above file
for line in list(ROYCE_unique_words_set):
    royce_file.writelines(line+"\n")


# In[460]:


royce_file.seek(0)
royce_file.readlines()


# In[461]:


royce_file.close()


# ### SANSA

# In[462]:


sansa_file=open("E:\\internshala data science course\\COURSE 4-Python for Data Science\\project\\C1-Project-File Handling & String Manipulation-Dataset\\sansa_spoken_words_file.txt","a+")


# In[463]:


sansa_file.seek(0)
# writing into the above file
for line in list(SANSA_unique_words_set):
    sansa_file.writelines(line+"\n")


# In[464]:


sansa_file.seek(0)
sansa_file.readlines()


# In[465]:


sansa_file.close()


# ### SEPTA MORDANE

# In[466]:


septa_mordane_file=open("E:\\internshala data science course\\COURSE 4-Python for Data Science\\project\\C1-Project-File Handling & String Manipulation-Dataset\\septa_mordane_spoken_words_file.txt","a+")


# In[467]:


septa_mordane_file.seek(0)
# writing into the above file
for line in list(SEPTA_MORDANE_unique_words_set):
    septa_mordane_file.writelines(line+"\n")


# In[468]:


septa_mordane_file.seek(0)
septa_mordane_file.readlines()


# In[469]:


septa_mordane_file.close()


# ### THEON

# In[470]:


theon_file=open("E:\\internshala data science course\\COURSE 4-Python for Data Science\\project\\C1-Project-File Handling & String Manipulation-Dataset\\theon_spoken_words_file.txt","a+")


# In[471]:


theon_file.seek(0)
# writing into the above file
for line in list(THEON_unique_words_set):
    theon_file.writelines(line+"\n")


# In[472]:


theon_file.seek(0)
theon_file.readlines()


# In[473]:


theon_file.close()


# ### WILL

# In[474]:


will_file=open("E:\\internshala data science course\\COURSE 4-Python for Data Science\\project\\C1-Project-File Handling & String Manipulation-Dataset\\will_spoken_words_file.txt","a+")


# In[475]:


will_file.seek(0)
# writing into the above file
for line in list(WILL_unique_words_set):
    will_file.writelines(line+"\n")


# In[476]:


will_file.seek(0)
will_file.readlines()


# In[477]:


will_file.close()


# In[ ]:




