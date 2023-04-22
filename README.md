
# C Program Evaluator

This project was written to make the task of evaluating C files automatic. It was done as a student practice work.

It was asked to make a python script using the system calls we studied at that moment to analyse some C files and give them a mark for each of these following points :

- The file compiles
- It makes an executable
- The run of the program with some tests values works
- Amount of documentation








## Launch the script

To launch the script you must be in the same directory of the **Correction.py** file. Then you have two ways of running it.

You must provide the path of the archive you want to be analyzed. 

### 1 - Script arguments

We can run the project with two packs of arguments :

- **./Correction.py** [archive path] [folder after the unzip] [csv file name]

- **./Correction.py** [archive path] [folder after the unzip]


### 2 - Python command

```bash
python3 Correction.py ...
```


### 3 - Executable command

To use this python file as an executable file, you should care about this line (at the top of the file):

```python
#! /usr/local/bin/python3.8
```

For your own use, you must check if your path is the same and update this line if it is not the case.

Then you can run this command:

```bash
./Correction.py ...
```




## Example

You can run the project with the given archive. 

**Rendus_eleves.zip** contains a lot of different files written in C language.

In a console :

```bash
./Correction.py Rendus_eleves.zip eleves_bis result.csv
```



## Optimizations

The actual code is awful (old project), I plan to refactor it to be more understandable.

I'd like to make it more generic to be used for more tasks by adding a config file describing the tests and its answers that the C files must check. The script could parse this config file and do the analysis thanks to theses information.


## Feedback

If you have any feedback, please reach out to me at dyl.dejesusmilitar@gmail.com




## Credits

Created by [@Dyl-DJM](https://www.github.com/Dyl-DJM).


