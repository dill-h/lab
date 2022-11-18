class Account:
    def __init__(self,name):
        '''
        Function to initialize the class.
        :param name: String value of the account's name
        '''
        self.__account_name = name
        self.__account_balance = 0.0
 
    def deposit(self, amount) -> bool:
        '''
        Function to add a given amount to the account balance.
        :param amount: Numeric value to add to balance.
        :return: Bool whether the deposit was successful or not.
        '''
        if float(amount) > 0:
            self.__account_balance += float(amount)
            return True
        else:
            return False
      
    def withdraw(self, amount) -> bool:
        '''
        Function to withdraw a given amount from the account balance.
        :param amount: Numeric value to withdraw from balance.
        :return: Bool whether the withdrawal was successful or not.
        '''
        if (float(amount) > 0) and (float(amount) <= self.__account_balance):
            self.__account_balance -= float(amount)
            return True
        else:
            return False
        
    def get_balance(self) -> float:
        '''
        Getter function for account balance.
        :return: Numeric value of account balance.
        '''
        return self.__account_balance
        
    def get_name(self) -> str:
        '''
        Getter function for account name.
        :return: Numeric value of account name.
        '''
        return self.__account_name
