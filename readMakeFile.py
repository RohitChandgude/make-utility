#!/usr/bin/python
import sys;
import subprocess as sp;

keyVal = dict();
def isKey(ls):
	return (ls[0]!='' and ls[0][-1]==':');
def createDictionary(fileName):
	fo = open(fileName,"r");
	lines = fo.read().replace("\t","").split("\n");
	for i in range(0,len(lines)):
		ls =  lines[i].split(" ");
		if(isKey(ls)):
			key = ls[0][:-1];
			keyVal[key]=[];
			j=i+1;
			while(isKey(lines[j].split(" "))!=True and j < len(lines)-1):
				if(lines[j]==key):
					
					j += 1;
					continue;
				if(lines[j]!=''):
					keyVal[key].append(lines[j]);
				j += 1;

	
	return keyVal;

def execute(input):
	ls = keyVal[input];
	for cmd in ls:
		if cmd in keyVal:
			execute(cmd);
		else:
			sp.call(cmd,shell=True);
input = sys.argv[1];

createDictionary("MyMakefile");
execute(input);
