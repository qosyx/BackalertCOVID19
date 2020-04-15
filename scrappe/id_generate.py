import uuid 
  

def generateId():
    id = uuid.uuid1() 
    return id.int

# Representations of uuid1() 

def get():
    bit_size = 16
    sized_unique_id = uuid.uuid4().int 
    print(sized_unique_id)
    
if __name__ == "__main__":
    get()