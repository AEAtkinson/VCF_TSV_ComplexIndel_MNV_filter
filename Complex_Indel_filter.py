#!/usr/bin/env python3

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  3 08:29:37 2019 through 2/24/2019

@author: aaronatkinson
"""
#import packages
import pandas as pd
import glob, os

#Assign directory to change or us within directory
directory="/Users/aaronatkinson/Desktop/FoundationWorkUp/Foundation_072019/Vcfscopy2/F_clin_Filtered_VCFs/avatarTsv/Non_Av_TRFmultipleTSVs/Uploaded_files/Upload_Final_F1_Clin_Tcc/UncompressedTSVs/Pre_ComplexIndel_Filtering"

#create filelist
for filename in glob.glob('**_clin.tsv'):
    print(filename)
    open(filename)
    df = pd.read_table(filename, header=None)
    print(df)
    
#filter complex Indels by column '2' or '3' string length < 2
    df2 = df[
            df[2].apply(lambda x: len(str(x)) < 2) |
            df[3].apply(lambda x: len(str(x)) < 2)
            ]
    print(df2)

#print df split from filelist and save new tsv to_csv function ('\tab') - per illumina format
    csv_file = os.path.splitext(filename)[0]+".tsv"
    df2.to_csv(csv_file, sep='\t', index=False, header=False)