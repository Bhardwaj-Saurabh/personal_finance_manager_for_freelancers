# transaction_strategy.py


class TransactionProcessingStrategy:
    """Interface for transaction processing strategies."""

    def apply(self, amount):
        """Process the transaction amount and return the adjusted amount."""
        raise NotImplementedError("Subclasses must implement apply method.")


class NoProcessingStrategy(TransactionProcessingStrategy):
    """Default strategy that applies no modification."""

    def apply(self, amount):
        return amount


class TaxStrategy(TransactionProcessingStrategy):
    """Applies a tax rate to the transaction amount."""

    def __init__(self, rate):
        self.rate = rate

    def apply(self, amount):
        return amount + (amount * self.rate)


class DiscountStrategy(TransactionProcessingStrategy):
    """Applies a discount rate to the transaction amount."""

    def __init__(self, rate):
        self.rate = rate

    def apply(self, amount):
        return amount - (amount * self.rate)
