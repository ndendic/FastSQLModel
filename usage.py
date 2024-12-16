from fastsqlmodel.db import BaseTable

class Test(BaseTable, table=True):
    name: str
    description: str

test = Test(name="Test", description="Test")

print(test)
