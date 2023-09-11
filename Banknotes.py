from pydantic import BaseModel

# below all are work as json
class Banknote(BaseModel):
    variance: float
    Skewness : float    
    Curtosis : float