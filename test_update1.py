class Test():
    def __init__(self):
        print("Init")
    
    def sum(self, a, b):
        return a+b
    
    def multiply(self, a, b):
        return a*b
    

if __name__ == "__main__":
    test = Test()
    print(test.sum(1,2))
    print(test.multiply(1,3))
    print("Done")