import os
from re import U
import subprocess
from contextlib import redirect_stdout
import io
import sys
from dataclasses import dataclass
import difflib as dl


class Util:

    @staticmethod
    def get_argument():
        return sys.argv

    @staticmethod
    def get_directory(folder, argument):
        return os.listdir("./" + "TestCases/" + folder + argument + "/")

    @staticmethod
    def make(test):
        os.chdir("../alan/src")
        print("--- make " + test + " " + ("-" * 63))
        os.system("make clean")
        os.system("make " + test)
        print("-" * 80)
        os.chdir("../../TestSuiteALAN")

    def export_jasmin():
        os.environ["JASMIN_JAR"] = "../../TestSuiteALAN/jasmin.jar"

class Difference:
    results_folder = ''

    def __init__(self, folder):
        self.results_folder = folder

    def display_differences(self, l):
        for file in l:
            s1 = file[1].splitlines()
            print("\033[1;30;41m%s%s\033[0m" % ("DIFFERENCES IN FILE: ", file[0]))
            with open('./Results/' + self.results_folder + '/' + file[0] + '.txt') as f:
                s2 = f.read().splitlines()
            for diff in dl.context_diff(s1, s2):
                print(diff)


class Test:
    fails = list()

    @dataclass
    class Stats:
        tests: int
        passes: int
        failures: int

    CurrentResult = Stats(0, 0, 0)

    def __init__(self, directory):
        self.list = directory

    def test_codegen(self, arg):
        os.chdir('../alan/bin')
        Util.export_jasmin()
        self.list.sort()
        for i in self.list: 
            i = i.replace(".alan", "")
            subprocess.run(
                ['./alanc', '../../TestSuiteALAN/TestCases/codegen/' + arg + '/' + i + '.alan'],
                capture_output=False)

            java = "java " + str(i)
            self.out = subprocess.check_output(java, shell=True)
            self.out = str(self.out, "UTF-8")
            with open('../../TestSuiteALAN/Results/codegen/' + i + '.txt') as f:
                result = f.read()
            self.display_result_codegen(i + '.alan', result == self.out)
        os.chdir("../../TestSuiteALAN")


    def test(self, bin_file, type, arg):
        self.list.sort()
        for i in self.list:
            i = i.replace(".alan", "")
            self.out = subprocess.run(
                ['../alan/bin/' + bin_file, './TestCases/' + type + '/' + arg + '/' + i + '.alan'],
                capture_output=True)
            with open('./Results/' + type + '/' + i + '.txt') as f:
                result = f.read()
            self.display_result(i + '.alan', result == (self.out.stdout.decode() + self.out.stderr.decode()))

    def display_result(self, file, res):
        self.CurrentResult.tests += 1
        if res:
            print("\033[1;30;42m%-30s %9s\033[0m" % (file, "PASS"))
            self.CurrentResult.passes += 1
        else:
            print("\033[1;30;41m%-30s %9s\033[0m" % (file, "FAIL"))
            self.fails.insert(self.CurrentResult.failures - 1,
                              [file.replace(".alan", ""), self.out.stdout.decode() + self.out.stderr.decode()])
            self.CurrentResult.failures += 1

    def display_result_codegen(self, file, res):
        self.CurrentResult.tests += 1
        if res:
            print("\033[1;30;42m%-30s %9s\033[0m" % (file, "PASS"))
            self.CurrentResult.passes += 1
        else:
            print("\033[1;30;41m%-30s %9s\033[0m" % (file, "FAIL"))
            self.fails.insert(self.CurrentResult.failures - 1,
                              [file.replace(".alan", ""), self.out])
            self.CurrentResult.failures += 1
    

    def display_stats(self):
        print("%i TESTS: %i PASSES and %i FAILS" % (
            self.CurrentResult.tests, self.CurrentResult.passes, self.CurrentResult.failures))
        print(str(round(self.CurrentResult.passes / self.CurrentResult.tests, 4) * 100) + '%')

    @staticmethod
    def hash(bin_file, file):
        with open(file) as f:
            country = f.readline()
            out = subprocess.run(['../alan/bin/' + bin_file, 'co', 'to'])



if __name__ == '__main__':

    argument = Util.get_argument()
    # Get arguments
    if len(argument) == 3:
        arg = argument[1] + " " + argument[2]

    # Set directory and testxxx
    test = ''
    directory = list()
    loc = ''
    diff = ''
    bin_file = ''

    if argument[1] == 'scanner':
        directory = Util.get_directory('scanner/', argument[2])
        test = 'testscanner'
        diff = 'scanner'
        bin_file = 'testscanner'

    elif argument[1] == 'parser':
        test = 'testparser'
        diff = 'parser'
        bin_file = 'alanc'

        if argument[2] == 'most':
            directory = Util.get_directory('parser/', '')
            directory.remove("tenthousand")
            directory.remove("official")

        else:
            directory = Util.get_directory('parser/', argument[2])

    elif argument[1] == 'typechecking':
        directory = Util.get_directory('typechecking/', argument[2])
        test = 'testtypechecking'
        bin_file = 'alanc'
        diff = 'typechecking'

    elif argument[1] == 'hash': 
        Util.make('testhashtable')
        os.system('cc -o hash hash.c ../alan/src/error.o ../alan/src/hashtable.o   ')
        os.system('./hash')

    elif argument[1] == 'codegen': 
        directory = Util.get_directory('codegen/', argument[2])
        test = 'alanc'
        bin_file = 'alanc'
        diff = 'codegen'



        Util.make(test)
        test = Test(directory)

        if argument[2] != 'codegen':
                test.test_codegen(argument[2])
        else: 
            test.test(bin_file, argument[1], argument[2])
            test.display_stats()
            
        

        print("-" * 80)
        print("Enter 0 to exit, or 1 to display differences in failed cases: ")

        for line in sys.stdin:
            if line.rstrip() == "1":
                diffy = Difference(diff)
                diffy.display_differences(test.fails)
                break
            if line.rstrip() == "0":
                break

