from pydantic import BaseModel,EmailStr,AnyUrl, Field, field_validator, model_validator

from typing import List, Dict, Optional, Annotated


class Patient(BaseModel):
    name : Annotated[str, Field(min_length=1, max_length=50, title="patient Name")]
    email: EmailStr
    linkedin_url: AnyUrl
    age: Annotated[int , Field(gt=0, lt=120)]
    height: float
    weight: Annotated[float, Field(gt=0, strict=True)]
    bmi: float
@field_validator('email')
@classmethod
def email_validate(cls, value):
    valid_domains = ['cse.pstu.ac.bd', 'yahoo.com', 'outlook.com']

    domain_name = value.split('@')[-1]

    if domain_name not in valid_domains:
        raise ValueError('Email domain must be one of the following: cse.pstu.ac.bd, yahoo.com, outlook.com')
    
    return value



@field_validator('linkedin_url')
@classmethod
def linkedin_url_validate(cls, value):
    valid_urls =['ccc.linkedin.com', 'ddd.linkedin.com', 'eee.linkedin.com']

    url_parts = value.split('//')[-1]

    if url_parts not in valid_urls: 
        raise ValueError('Linkedin URL must be one of the following: ccc.linkedin.com, ddd.linkedin.com, eee.linkedin.com')
    return value
patient_info = {'name':'Hadi','email':'ug2102060@yahoo.com','linkedin_url':'https://ccc.linkedin.com/in/hadi123','age':25,'height':5.8,'weight':70.5,'bmi':22.5}

patient1 = Patient(**patient_info)
def insert_patient_data(patient: Patient):
    print(patient.name)
    print(patient.email)
    print(patient.linkedin_url)
    print(patient.age)
    print(patient.height)
    print(patient.weight)
    print(patient.bmi)
    print("insert into database")
insert_patient_data(patient1)