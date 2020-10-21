# -*- coding: utf-8 -*-
"""
@author: Naziz Ismail 
"""
import pandas as pd 
import os
import csv


class GetData(object):
	
	def __init__(self,path,separator = None):
		self.path = GetData._init_path(path)
		self.dic_df = GetData._init_dic_df(path,separator)
		
	
	def _init_path(path):
		if not(os.path.exists(path)):
			print('------------\nPlease enter a correct path\n------------')
			raise ValueError
		return path
	
	def _init_dic_df(path,separator):
		dic_df = {}
		files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
		if files == [] : 
			print('------------\nEmpty Folder\n------------')
			raise ValueError
		os.chdir(path)
		for file in files :
			if separator == None:
				with open(file, 'r') as r_file:
					text = r_file.read()[:1000]
					sniffer = csv.Sniffer()
					separator = sniffer.sniff(text).delimiter
					
			name = os.path.splitext(file)[0]
			extension = os.path.splitext(file)[1]
			if  extension == '.csv':
				dic_df[name] = pd.read_csv(file, sep=separator, engine="python")
				
				
			if extension == '.xlxs':
				dic_df[name] =pd.read_excel(file,sep=separator)
				

		if len(dic_df.keys()) == 0:
			print('------------\nNo xlxs or csv files found\n------------')
			raise ValueError
		
		return 	dic_df	

	
if __name__ == "__main__":
	data = GetData(r"D:\machine_learning\generated_data",",")
	for elem in data.dic_df.keys():
		print(data.dic_df[elem]) 	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	