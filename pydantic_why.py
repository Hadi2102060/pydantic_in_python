
from pydantic import BaseModel,EmailStr,AnyUrl,Field,field_validator,model_validator
from typing import List, Dict, Optional,Annotated


# from typing import List             
# (for define ideal schema in pydantic class model (= Patient ) inside this patient you declare a list 
# for alargies then you must be declare this List class)
# for simply any field can be optional then import Optional to (from typing import List,Dict, Optional)  and where i field is optional then initialize default value is ( None)

# (email = EmailStr declaration in pydantic class model) and linkedin_url = AnyUrl declaration in pydantic class)
# jokhon ami weight er value 0 theke nise dita parbo nh ba amon kono case jekhane ami specific required set korte parbo tokhon pydantic amake aktu special function dei jeta name =(Feild)...ata diye amra specific condition set kore dita pari jemon weight gt>0(gt means greater than)

# Annotated typing module er part jeta meta data add korar jonno use kora hoi

# Field  ashole 3 ta kaj kore (1. custom data validation , 2. metadata, 3. default value)

# strict = True mane hosse jodi kono integer value string kori tahole sheta error dekhabe sheta oboshoi integer ei hote hobe

class Patient(BaseModel):
    name: Annotated[str, Field(min_length=1, max_length=50, title="Patient Name", description="Give the name of the patient in less than 50 characters",examples=["hadi","nitish"])]
    email: EmailStr
    linkedin_url: AnyUrl
    age: int= Field(gt=0,lt=120)  # gt means greater than 0
    height: float 
    weight: Annotated[float, Field(gt=0, strict=True)]
    bmi: float
    married: Annotated[bool, Field(default=None,description="Is the patient married or not?")]
    allergies: Annotated[Optional[List[str]], Field(default= None, max_length=5)]
    contact_details: dict[str, str]

def insert_patient_data(patient: Patient):
    print(patient.name)
    print(patient.email)
    print(patient.linkedin_url)
    print(patient.age)
    print(patient.height)
    print(patient.weight)
    print(patient.bmi)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact_details)
    print("insert into database")




patient_info = {"name": "nitish", "email":"abc@gmail.com", "linkedin_url":"http://linkedin.com/1234", "age": 30, "height": 5.9, "weight": 70.5,"bmi": 22.5,"allergies":['pollen','dust'], "contact_details": {'phone':'1234567890'}}

patient1 = Patient(**patient_info)

insert_patient_data(patient1)