"""Module for testing the Varasto class."""

import unittest
from varasto import Varasto

class TestVarasto(unittest.TestCase):
    """Unit tests for the Varasto class."""

    def setUp(self):
        """Set up a new Varasto instance for testing."""
        self.varasto = Varasto(10)

    def test_constructor_initializes_correctly(self):
        """Test that the constructor initializes correctly."""
        self.assertEqual(self.varasto.tilavuus, 10)

    def test_adding_negative_amount_does_nothing(self):
        """Test that adding a negative amount does nothing."""
        self.varasto.lisaa_varastoon(-5)
        self.assertEqual(self.varasto.saldo, 0)

    def test_adding_to_varasto_increases_saldo(self):
        """Test that adding a positive amount increases the saldo."""
        self.varasto.lisaa_varastoon(5)
        self.assertEqual(self.varasto.saldo, 5)

    def test_adding_more_than_capacity_locks_to_capacity(self):
        """Test that adding more than capacity locks saldo to maximum."""
        self.varasto.lisaa_varastoon(15)
        self.assertEqual(self.varasto.saldo, 10)

    def test_removing_negative_amount_does_nothing(self):
        """Test that removing a negative amount does nothing."""
        self.varasto.ota_varastosta(-5)
        self.assertEqual(self.varasto.saldo, 0)

    def test_removing_more_than_available_takes_all(self):
        """Test that removing more than available takes all available."""
        self.varasto.lisaa_varastoon(5)
        result = self.varasto.ota_varastosta(10)
        self.assertEqual(result, 5)
        self.assertEqual(self.varasto.saldo, 0)

    def test_string_representation_is_correct(self):
        """Test that the string representation of Varasto is correct."""
        self.varasto.lisaa_varastoon(7)
        self.assertEqual(str(self.varasto), "saldo = 7, vielä tilaa 3")
