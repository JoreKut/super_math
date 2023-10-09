

def recursion(n: int) -> int:
    return n * (recursion(n-1) if n != 1 else 1)

