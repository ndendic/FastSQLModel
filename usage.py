from fastsqlmodel.db import BaseTable

class Test(BaseTable):
    name: str
    description: str

test = Test(name="Test", description="Test")

print(test)
