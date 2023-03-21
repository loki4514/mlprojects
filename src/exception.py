import sys
# that provides access to some system-specific functionalities and variables. 
# It allows Python code to interact with the underlying operating system and to, 
# perform tasks like reading and writing to the standard input/output/error 
from src.logger import logging

def error_message_details(error,error_details:sys):
    # only last info is enough 
    # info gives all the info about expection in while file on which line
    _,_,exc_tb = error_details.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    line_number = exc_tb.tb_lineno
    error_msg = str(error)
    error_message = f"Error Occured in python script name [{file_name}] line number \
        [{line_number}] error message [{error_msg}]"
        
        
    return error_message

class CustomException(Exception):
    def __init__(self,error_message,error_details:sys):
        # overwriring with parent class 
        super().__init__(error_message)
        self.error_message = error_message_details(error_message,error_details=error_details)
        
    def __str__(self):
        return self.error_message
    
    
    
    
############ or ################################3
# class CustomException(Exception):
#     def __init__(self, error_message, error_details):
#         super().__init__(error_message)
#         _, _, exc_tb = error_details.exc_info()
#         file_name = exc_tb.tb_frame.f_code.co_filename
#         line_number = exc_tb.tb_lineno
#         self.error_message = f"Error occurred in {file_name}, line {line_number}: {error_message}"

#     def __str__(self):
#         return self.error_message


if __name__ == "__main__":
    # try:
    #     a = 1/0
    # except Exception as e:
    #     raise CustomException(e,sys)
    pass 
