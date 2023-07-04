import sys  #used to manipulate the runtime enviornment
import logging 

def error_message_detail(error,error_detail:sys):          #custom exception handling
    _,_,exc_tb=error_detail.exc_info()
    file_name=exc_tb.tb_frame.f_code.co_filename #filename interconnection
    error_message="Error occured in  python script name [{0}] line [{1}]  error message [{2}]".format(file_name,exc_tb.tb_lineno,str(error))
    return error_message
    
class CustomException(Exception):
    def __inti__(self,error_message,error_detail:sys):
        super().__init__()
        self.error_message=error_message_detail(error_message,error_detail=error_detail)

    def __str__(self):
        return self.error_message


if __name__=="__main__":
    try:
        a=1/0
    except:
        logging.info("Divide by zero error")
        raise CustomException

    