# -*- coding: utf-8 -*-
import pytest
from unittest import TestCase

pytestmark = pytest.mark.django_db


class TestDigioWebhook(TestCase):
    def test_is_valid_signature(self):

        assert 2 + 2 == 4
