# imoport library
import uvicorn
from fastapi import FastAPI , Path ,  File, UploadFile
from Banknotes import Banknote
# create object of fastapi
app = FastAPI()

# index route open automatically on localhost 8000
# swagger api also known as openAPI
@app.get("/")
def home():
    return {"message":"Hi! i am fastapi "}

# route with singlw parameter name 
@app.get("/welcome")
def get_name(name:str):
    return {"return to my page": f'{name}'}





# http://127.0.0.1:8000/docs this help us for giving a swagger api page its also a advantage of it 
# ib http://127.0.0.1:8000/redoc also shows api respanse


# with default values
# ou can access the parameters using the URL, e.g., /items/?skip=5&limit=20
@app.get("/items/")
def read_item(skip: int = 0, limit: int = 10):
    return {"skip": skip, "limit": limit}

# Path Parameters
# you can access the item_id as part of the URL path, e.g., /items/42
@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id}

# Path Parameters with Validation
# the item_id is required (specified by ...) and must be greater than or equal to 1 (ge=1
@app.get("/items/{item_id}")
def read_item(item_id: int = Path(..., title="The ID of the item to get", ge=1)):
    return {"item_id": item_id}

# upload a file

@app.post("/uploadfile/")
async def upload_file(file: UploadFile):
    with open(file.filename, "wb") as f:
        f.write(file.file.read())
    return {"filename": file.filename}

# expose the predication functionality, 
# Make predication from the passed json data  using post from Banknotes.py file (in postmen we pass data in past using json same it is)
# data is temp variable using we fatch thw values from Banknotes
@app.post('/predict')
def predict_bank_notes(data:Banknote):
    data = data.dict()
    print(data)
    variance = data['variance']
    print("Here is your variance using BASEMODEL",variance)
    if variance > 5:
        variance = "Fale"
    else:
        variance = "pass"
    return {
        'predication' : variance
    }

# run the API usig uvicorn
# To implement ASGI we use uvicorn.run insted of app.run bcz of this its very fast 
if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1", port=8000)

# main insted we use our flle name and app is our object of app
# which we created above using FastAPI

# To run above code
# uvicorn fastapi_basic1:app --reload