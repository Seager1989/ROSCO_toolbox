import os
import unittest
from time import time
import importlib

# from weis.test.utils import execute_script, run_all_scripts


def run_all_scripts(folder_string, all_scripts):
    scripts = [m for m in all_scripts if m.find(folder_string) >= 0]
    for k in scripts:
        try:
            execute_script(k)
        except Exception as e:
            print("Failed to run,", k)
            raise

def execute_script(fscript):
    # thisdir = os.path.dirname(os.path.realpath(__file__))
    # root_dir = os.path.dirname(os.path.dirname(thisdir))
    examples_dir = os.path.dirname(os.path.realpath(__file__))

    # Go to location due to relative path use for airfoil files
    print("\n\n")
    print("NOW RUNNING:", fscript)
    print()
    fullpath = os.path.join(examples_dir, fscript + ".py")
    # basepath = os.path.join(examples_dir, fscript.split("/")[0])
    os.chdir(examples_dir)

    # Get script/module name
    froot = fscript.split("/")[-1]

    # Use dynamic import capabilities
    # https://www.blog.pythonlibrary.org/2016/05/27/python-201-an-intro-to-importlib/
    print(froot, os.path.realpath(fullpath))
    spec = importlib.util.spec_from_file_location(froot, os.path.realpath(fullpath))
    mod = importlib.util.module_from_spec(spec)
    s = time()
    spec.loader.exec_module(mod)
    print(time() - s, "seconds to run")

# 02_ref turbines are regression tested in test_gluecode, no need to duplicate runtime
all_scripts = [
    'example_01',
    'example_02',
    'example_03',
    'example_04',
    'example_05',
    'example_06',
    'example_07',
    'example_08',
    'example_09',
    'example_10',
    'example_11',
    
]

class TestExamples(unittest.TestCase):
    
    # I think we would break them up here, currently they are just one big test
    def test_ROSCO_toolbox(self):
        run_all_scripts("example", all_scripts)
                    


def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestExamples))
    return suite


if __name__ == "__main__":
    unittest.TextTestRunner().run(suite())