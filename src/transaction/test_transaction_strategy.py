import unittest
from transaction.transaction import Transaction
from transaction.transaction_category import TransactionCategory
from transaction.transaction_strategy import (
    NoProcessingStrategy,
    TaxStrategy,
    DiscountStrategy,
)
from balance.balance import Balance


class TestTransactionStrategy(unittest.TestCase):

    def setUp(self):
        self.balance = Balance.get_instance()
        self.balance.reset()

    def test_no_processing_strategy(self):
        strategy = NoProcessingStrategy()
        self.assertEqual(strategy.apply(100), 100)

    def test_tax_strategy(self):
        strategy = TaxStrategy(rate=0.10)
        self.assertEqual(strategy.apply(100), 110)

    def test_discount_strategy(self):
        strategy = DiscountStrategy(rate=0.20)
        self.assertEqual(strategy.apply(100), 80)

    def test_apply_transaction_with_tax_strategy(self):
        t = Transaction(100, TransactionCategory.INCOME)
        self.balance.apply_transaction(t, strategy=TaxStrategy(rate=0.10))
        self.assertEqual(self.balance.get_balance(), 110)

    def test_apply_transaction_with_discount_strategy(self):
        t = Transaction(200, TransactionCategory.EXPENSE)
        self.balance.apply_transaction(t, strategy=DiscountStrategy(rate=0.25))
        self.assertEqual(self.balance.get_balance(), -150)

    def test_apply_transaction_without_strategy(self):
        t = Transaction(100, TransactionCategory.INCOME)
        self.balance.apply_transaction(t)
        self.assertEqual(self.balance.get_balance(), 100)


if __name__ == "__main__":
    unittest.main()
