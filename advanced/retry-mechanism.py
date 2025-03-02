def retry(func, attempts):
    for _ in range(attempts):
        try:
            return func()
        except Exception as e:
            print(f"Error: {e}")
    raise Exception("Failed after multiple attempts")

def test():
    print("Testing")
    raise Exception("Error")

retry(test, 3)

# Output:
