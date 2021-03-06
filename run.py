jls_extract_var = """
The aim of this program is to:
- Collect sales data from user
- Add slaes sata into sales worksheet
- Calculate surplus numbers
- Add surplus data to surplus worksheet
- Calculate the average sales of the last 5 markets
- Print stock recommendations to the terminal
- Add calculaed stock numbers into the stock worksheet
- Check that the sales data input from the user is valid 
"""
#in order to use Google Sheet API, this needs to be imported
#To install, type "pip3 install gspread google-auth"
import gspread 
from google.oauth2.service_account import Credentials 
#Put constants in all caps 
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open("love_sandwiches")
"""
This is the code used to check the API is working, leave commented out
sales = SHEET.worksheet('sales')
data = sales.get_all_values()
print(data)
"""

def get_sales_data():
    """
    get sales figures input from the user
    """
    print("Please enter sales data from the last market")
    print("Data should be six numbers, separated by commas")
    print("Example: 10,20,30,40,50\n") #add \n for new line

    data_str = input("Enter your data here: ")
    
    #validate data - split method returns broken up values as a list

    sales_data = data_str.split(",") 
    validate_data(sales_data)

def validate_data(values):
    """
    Inside the try, converts all string values into integers.
    Raises ValueError if strings cannot be concerted 
    intointe, or if there arent exactly 6 values
    """
    print(values)
    try:
        [int(value) for value in values]
        if len(values) !=6:
            raise ValueError(
                f"Exactly 6 values required, you provided {len(values)}"
            )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again \n")

get_sales_data()
