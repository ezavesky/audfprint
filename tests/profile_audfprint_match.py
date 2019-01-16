# coding=utf-8
import cProfile
import pstats
import os, sys  # for local testing

if __name__ == "__main__":
    sys.path.insert(0, os.path.abspath('..'))

# noinspection PyUnresolvedReferences
import audfprint

def run_test():
    cProfile.run('audfprint.main(argv)', 'fpmstats')

    p = pstats.Stats('fpmstats')

    p.sort_stats('time')
    p.print_stats(10)

# run test with text file output
argv = ["audfprint", "match", "-d", "fpdbase.pklz", "--density", "200", "--opfile", "match.output.txt", "data/query.mp3"]
run_test()

# run test with JSON file output; also turn down verbosity to not output
argv = ["audfprint", "match", "-d", "fpdbase.pklz", "--density", "200", "--json", "--opfile", "match.output.json", "--verbose", 0, "data/query.mp3"]
run_test()