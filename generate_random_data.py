# -*- coding: utf-8 -*-
"""
@author: Naziz Ismail 
"""
import numpy as np 
import pandas as pd
import os
import logging
import time 
import datetime as dt

class GeneratorManager(object):
	
	def __init__(self,nb_columns,nb_lines,pp = 0.5):
		self.path = r"D:\machine_learning\generated_data"
		self.counter_file = r"D:\machine_learning\generated_data\num_file.txt"
		self.counter = GeneratorManager._init_counter(self.counter_file)
		self.nb_columns =nb_columns 
		self.nb_lines = nb_lines 
		self.pp = pp


	def generate_data(self,output_type ,mixed_data , ppd = None):
# mixed_data c coutinous, b binary, m = mixed

		df = {}
		for i in range(self.nb_columns):
			name ='col_' + str(i)
			if i == self.nb_columns-1:
				name = 'output'

			if mixed_data == 'm':
				if i%2 == 0:
					df[name] = [np.random.random()for j in range(self.nb_lines)]
				
				else:

					if name == 'output' and output_type == 'c':
						df[name] = [np.random.random()for j in range(self.nb_lines)]
					
					else:
						df[name] = [np.random.randint(2)for j in range(self.nb_lines)]

			elif mixed_data == 'c':
				
				if name == 'output' and output_type == 'b':
					df[name] = [np.random.randint(2)for j in range(self.nb_lines)]
				
				else:
					df[name] = [np.random.random() for j in range(self.nb_lines)]

			elif mixed_data == 'b':
				
				if name == 'output' and output_type == 'c':
					df[name] = [np.random.random()for j in range(self.nb_lines)]
				
				else:
					df[name] = [np.random.randint(2) for j in range(self.nb_lines)]


		df = pd.DataFrame.from_dict(df)
		print(df)
		return df 

	def generate_file(self,output_type = 'c',mixed_data = 'c'):
		df = self.generate_data(output_type,mixed_data)
		if output_type == 'c':
			file_name = self.path +'\data_'+str(self.counter)+'_continuous_output.csv'
		else:
			file_name = self.path +'\data_'+str(self.counter)+'_binary_output.csv'
		df.to_csv(file_name)
		print(f'{dt.datetime.now()} csv file {file_name} created ')
		self._update_counter()
	
	def _update_counter(self):
		self.counter +=1
		with open(self.counter_file,'r+') as file:
			file.truncate(0)
			file.write(str(self.counter))

	@classmethod
	def _init_counter(cls,my_file):
		with open(my_file,'r+') as file:
			content = file.read() 
			if not content :
				file.write('0')
				return 0
			else:
				return int(content)
		

if __name__ == "__main__":
	my_object = GeneratorManager(50,1000)
	my_object.generate_file('b','c')
	my_object.generate_file('c','c')
	my_object.generate_file('m','b')