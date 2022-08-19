import os
import subprocess
import sys
from dataclasses import dataclass
import difflib as dl


class Util:

    @staticmethod
    def get_argument():
        return sys.argv

    @staticmethod
    def get_directory(argument):
        return os.listdir("./" + "TestCases/parser/" + argument + "/")


    @staticmethod
    def make():
        os.chdir("../alan/src")
        print("--- make testparser " + ("-" * 63))
        os.system("make testparser")
        print("-" * 80)
        os.chdir("../../TestSuiteALAN")


class Difference:

    def display_differences(l):
        for file in l:
            s1 = file[1].splitlines()
            print("\033[1;30;41m%s%s\033[0m" % ("DIFFERENCES IN FILE: ", file[0]))
            with open('./Results/parser/' + file[0] + '.txt') as f:
                s2 = f.read().splitlines()
            for diff in dl.context_diff(s1, s2):
                print(diff)


class ScannerTest:
    fails = list()

    @dataclass
    class Stats:
        tests: int
        passes: int
        failures: int

    CurrentResult = Stats(0, 0, 0)

    def __init__(self, directory):
        self.list = directory

    def test_scanner(self, argument):
        self.list.sort()
        for i in self.list:
            i = i.replace(".alan", "")
            self.out = subprocess.run(['../alan/bin/alanc', './TestCases/parser/' + argument + '/' + i + '.alan'], capture_output=True)
            with open('./Results/parser/' + i + '.txt') as f:
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

    def display_stats(self):
        print("%i TESTS: %i PASSES and %i FAILS" % (
            self.CurrentResult.tests, self.CurrentResult.passes, self.CurrentResult.failures))


if __name__ == '__main__':

    argument = Util.get_argument()

    if len(argument) == 1:
        arg = ""
    else :
        arg = argument[1]

    directory = Util.get_directory(arg)

    if arg == "" :
        directory.remove("tenthousand")
        directory.remove("official")

    Util.make()

    scanner = ScannerTest(directory)

    scanner.test_scanner(arg)
    scanner.display_stats()

    print("-" * 80)
    print("Enter 0 to exit, or 1 to display differences in failed cases: ")

    for line in sys.stdin:
        if line.rstrip() == "1":
            Difference.display_differences(scanner.fails)
            break
        if line.rstrip() == "0":
            break
