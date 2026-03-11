#recursion
import sys
def hello():
    print("Hello")
    hello()
sys.setrecursionlimit(500)
print(sys.getrecursionlimit())
#hello()