# Sanity check that validation script exists and works
import os
import sys

if not os.path.exists("validation/grubbs_test.py"):
    sys.exit("Error: Grubbs test script missing.")

ret = os.system("python validation/grubbs_test.py")
if ret != 0:
    sys.exit("Error: Grubbs test failed.")
else:
    print("Grubbs test passed.")