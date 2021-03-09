# ------------------------------------------------------------------------ #
# Title: Assignment 08
# Description: Working with classes

# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created starter script
# RRoot,1.1.2030,Added pseudo-code to start assignment 8
# Molly Weaver, 03/06/2021, Modified code to complete assignment 8
# ------------------------------------------------------------------------ #

# Start Data -------------------------------------------------------------------- #

# Declaration of variables and constants
strChoice = ""                  # Captures the user's menu option choice
strFileName = 'products.txt'    # file to save data
lstOfProductObjects = []        # list to save dictionaries of objects -> product and price
strProduct = ""                 # string variable to save product
strPrice = ""                   # string variable to save price
strPriceError = ""              # variable for error handling

class Product(object):
    """Creates instances of the product and handles errors in user input

    changelog: (When,Who,What)
        Molly Weaver, 03/06/2021, Created script
    """

    # -- Constructor --
    def __init__(self, product="", price=""):
        # --Attributes --
        self.product = product
        self.price = price

    # -- Properties --
    # product
    @property
    def product(self):  # getter
        return str(self.__product)

    @product.setter
    def product(self, value):  # setter
        self.__product = value

    # price
    @property
    def price(self):  # getter
        return str(self.__price)

    @price.setter
    def price(self, value):  # setter
        self.__price = value

    # -- Methods -- #


# End Data -------------------------------------------------------------------- #

# Start Processing  ------------------------------------------------------------- #
class FileProcessor:
    """Processes data to and from a file and a list of product objects:

    methods:
        save_data_to_file(file_name, list_of_product_objects)

        read_data_from_file(file_name)

    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        Molly Weaver, 03/06/2021, Modified code to complete assignment 8
    """

    @staticmethod
    def read_data_from_file(file_name, list_of_rows):
        """ Reads data from a pickled file

        :param file_name: (string) with name of file
        :param list_of_rows: (list) you want written to file
        :return: list_of_rows
        """
        import pickle

        file_unpickle = open(file_name, "rb")
        list_of_rows = pickle.load(file_unpickle)
        file_unpickle.close()
        return list_of_rows

    @staticmethod
    def save_data_to_file(file_name, list_of_rows):
        """ Saves data from a list of product objects

        :param file_name: (string) with name of file
        :param list_of_rows: (list) you want written to file
        :return: list_of_rows
        """
        import pickle

        file_pickle = open(file_name, "wb")
        pickle.dump(list_of_rows, file_pickle)
        file_pickle.close()
        return list_of_rows


class InputProcessor:
    """Processes user input to and from a list of product objects:

    methods:
        add_data_to_list(product, price, list_of_products)

        is_price_numeric(price)

    changelog: (When,Who,What)
        Molly Weaver, 03/06/2021, Created
    """

    @staticmethod
    def add_data_to_list(product, price, list_of_products):
        """ Adds a new product to the list

        :param product: (string) new product
        :param price: (string) new product's price
        :param list_of_products: (list) of products
        :return: updated list_of_products
        """
        row = {} # create a new dictionary row
        row = {"Product": product, "Price": price}
        list_of_products.append(row)
        return list_of_products

    @staticmethod
    def is_price_numeric(price):
        """ Checks that the entered price is numeric

        :param price: (string) new product's price
        :return: (string) price_error
        """

        price_error = ""

        try:
            if not str(price).isnumeric():
                raise Exception
        except Exception:
            print("The price must be a number")
            price_error = "wrong"
        else:
            price_error = "right"
        finally:
            return price_error


# End Processing  ------------------------------------------------------------- #

# Start Presentation (Input/Output)  -------------------------------------------- #
class IO:
    """Displays data to and collects data from the user:

    methods:
        print_menu_Products()

        input_menu_choice()

        print_current_products_in_list(list_of_rows)

        input_new_product_and_price()

    changelog: (When,Who,What)
        Molly Weaver, 03/06/2021, Created
    """

    @staticmethod
    def print_menu_products():
        """  Display a menu of choices to the user

        :return: nothing
        """
        print('''
        Menu of Options
        1) See the current product list
        2) Add a new product      
        3) Save the product list
        4) Exit the program
        ''')
        print()  # Add an extra line for looks

    @staticmethod
    def input_menu_choice():
        """ Gets the menu choice from a user

        :return: (string) users menu choice
        """
        choice = str(input("Which option would you like to perform? [1 to 4] - ")).strip()
        print()  # Add an extra line for looks
        return choice

    @staticmethod
    def print_current_products_in_list(list_of_rows):
        """ Shows the current Products in the list of dictionaries rows

        :param list_of_rows: (list) of rows you want to display
        :return: nothing
        """
        print()  # Add an extra line for looks
        print("******* The current Products are: *******")
        for row in list_of_rows:
            print(row["Product"], "$", row["Price"])
        print("*****************************************")
        print()  # Add an extra line for looks

    @staticmethod
    def input_new_product_and_price():
        """ Ask user for a new product and price

        :return (string) product and (string) price
        """

        product = input("Enter the name of the new product: ")
        price = input("Enter the new product's price: $")
        return product, price

# End Presentation (Input/Output)  -------------------------------------------- #

# Start Main Body of Script  ---------------------------------------------------- #

# Load data from file into a list of product objects when script starts
lstOfProductObjects = FileProcessor.read_data_from_file(strFileName, lstOfProductObjects)

while(True):
    IO.print_menu_products()  # Show user a menu of options
    strChoice = IO.input_menu_choice() # Get user's menu option choice

    # Process user's menu choice
    if strChoice.strip() == "1":  # Menu option 1 -> Print the current Product list
        IO.print_current_products_in_list(lstOfProductObjects)

    elif strChoice == "2":  # Menu option 2 -> Add a new Product
        strProduct, strPrice = IO.input_new_product_and_price()
        strPriceError = InputProcessor.is_price_numeric(strPrice)
        if strPriceError == "right":
            objP = Product()
            objP.strProduct, objP.strPrice = strProduct, strPrice
            lstOfProductObjects = InputProcessor.add_data_to_list(objP.strProduct, objP.strPrice, lstOfProductObjects)

    elif strChoice == "3":  # Menu option 3 -> Save Data to File
        FileProcessor.save_data_to_file(strFileName, lstOfProductObjects)

    elif strChoice == "4":  # Exit the Program
        print("Goodbye!")
        break

# End Main Body of Script  ---------------------------------------------------- #
