"""Lazy check: falha se a logica de soma quebrar. Rode com `python test_app.py`."""
from app import soma

assert soma(2, 3) == 6, "soma(2,3) deveria ser 6"  # BUG intencional para simular falha no CI
assert soma(-1, 1) == 0, "soma(-1,1) deveria ser 0"
assert soma(0, 0) == 0, "soma(0,0) deveria ser 0"
print("testes ok")
