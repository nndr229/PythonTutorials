class Calculator:
    def __init__(self):
        pass

    def get_input(self):
        a = int(input("enter a: "))
        b = int(input("enter b: "))

        return [a,b]


    def add(self,a,b):
        return a+b

    def subtract(self,a,b):
        return a-b
    
    def multiply(self,a,b):
        return a*b

    def main_loop(self):
        print("Welcome to the Calculator app!")
        print()
        while True:
            print("Choose 0 to exit, 1 for addition, 2 for subtraction and 3 for multiplication")

            choice  = input("Enter your choice : ")

            choice = int(choice)

            if choice == 0:
                break
            elif choice == 1:
                ret_values = self.get_input()
                ret_value = self.add(ret_values[0],ret_values[1])
                print(ret_value)
                print()
            elif choice == 2:
                ret_values = self.get_input()
                ret_value = self.subtract(ret_values[0],ret_values[1])
                print(ret_value)
                print()

            else:
                ret_values = self.get_input()
                ret_value = self.multiply(ret_values[0],ret_values[1])
                print(ret_value)
                print()


if __name__ == "__main__":
    calci = Calculator()
    calci.main_loop()


        