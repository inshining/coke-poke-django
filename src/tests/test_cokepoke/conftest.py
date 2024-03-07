import pytest as pytest
from model_bakery import baker
def utbb():
    def unfilled_transaction_bakery_batch(n):
        utbb = baker.make(
            'cokepoke.Transaction',
            amount_int_cents=1032000,
            _fill_optional=[
                'name',
                'email',
                'currency',
                'message'
            ],
            _quantity=n
        )
        return utbb
    return unfilled_transaction_bakery_batch

@pytest.fixture
def ftbb():
    def filled_transaction_bakery_batch(n):
        utbb = baker.make(
            'cokepoke.Transaction',
            amount_int_cents=1032000,
            _quantity=n
        )
        return utbb
    return filled_transaction_bakery_batch

@pytest.fixture
def ftb():
    def filled_transaction_bakery():
        utbb = baker.make(
            'cokepoke.Transaction',
            amount_int_cents=1032000,
            currency=baker.make('cokepoke.Currency')
        )
        return utbb
    return filled_transaction_bakery