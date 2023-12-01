from dataclasses import dataclass

@dataclass
class A:
    a: int = 1
    b: str = "aa"

a = A(b='fjkdfj', a=1)
print(a.a)