from fastapi import Depends, FastAPI
from models2 import product
from database import session, engine
import database_model
from sqlalchemy.orm import Session

app = FastAPI()
database_model.Base.metadata.create_all(bind=engine)

@app.get("/")
def groot():
    return "Hi Nani"

products=[
    product(id=1,name="phone",description="budget phone",price=99.0,quantity=1),
    product(id=2,name="Laptop",description="gaming laptop",price=9990.0,quantity=10),
    product(id=3,name="computer",description="Tech center",price=12000.0,quantity=15)
]

def get_db():
      db=session()
      try:
            yield db
      finally:
            db.close()

def db_init():
     db=session()
     count=db.query(database_model.Product).count
     if count==0:
            for product in products:
                  db.add(database_model.Product(**product.model_dump()))  
            db.commit()
db_init()    

@app.get("/products")
def get_products(db:Session = Depends(get_db)):
      db_product=db.query(database_model.Product).all()
      return db_product

#@app.get("/product/{id}") 
#def get_products_id(id:int):
#     return products[id-1]

@app.get("/product/{id}")
def get_products_id(id:int, db:Session = Depends(get_db)):
      db_product=db.query(database_model.Product).filter(database_model.Product.id==id).first()
      if db_product:
                return db_product
      return "No product Found" 

@app.post("/product")
def add_products(product : product, db:Session = Depends(get_db)):
      db.add(database_model.Product(**product.model_dump()))
      db.commit()
      return product

@app.put("/product")
def update_products(id:int , product:product,db:Session = Depends(get_db)):
      db_product=db.query(database_model.Product).filter(database_model.Product.id==id).first()
      if db_product:
            db_product.name=product.name
            db_product.description=product.description
            db_product.price=product.price
            db_product.quantity=product.quantity
            db.commit()
            return "successfuly update"
      else:
            return "No update found"

@app.delete("/product")
def delete_product(id:int, db:Session = Depends(get_db)):
    db_product=db.query(database_model.Product).filter(database_model.Product.id==id).first()
    if db_product:
      db.delete(db_product)
      db.commit()
    else:    
      return "Not deleted,recheck"
