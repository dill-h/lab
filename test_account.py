from account import *

class Test:
    def setup_method(self):
        self.a1 = Account('Noah')
        self.a2 = Account('Mio')
        
    def teardown_method(self):
        del self.a1
        del self.a2
        
    def test_init(self):
        assert self.a1.get_balance() == 0.0
        assert self.a1.get_name() == 'Noah'
        assert self.a2.get_balance() == 0.0
        assert self.a2.get_name() == 'Mio'
    
    def test_deposit(self):
        assert self.a1.deposit(10) is True
        assert self.a2.deposit(-5) is False
        assert self.a1.get_balance() == 10.0
        assert self.a2.get_balance() == 0.0
        
    def test_withdraw(self):
        assert self.a1.withdraw(1) is False
        assert self.a2.withdraw(-5) is False
        assert self.a1.get_balance() == 0.0
        assert self.a2.get_balance() == 0.0
        
