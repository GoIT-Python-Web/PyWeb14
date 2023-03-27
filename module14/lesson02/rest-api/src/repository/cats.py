from sqlalchemy.orm import Session

from src.database.models import Cat
from src.schemas import PetModel, PetStatusVaccinated


async def get_cats(limit: int, offset: int, owner_id: int, is_vaccinated: bool, db: Session):
    """
    The get_cats function returns a list of cats.

    :param limit: int: Limit the number of results returned
    :param offset: int: Specify the number of items to skip before starting to collect the result set
    :param owner_id: int: Filter the cats by owner_id
    :param is_vaccinated: bool: Filter the cats by whether they are vaccinated or not
    :param db: Session: Pass the database session to the function
    :return: A list of cats
    :doc-author: Trelent
    """
    cats = db.query(Cat)
    if owner_id:
        cats = cats.filter(Cat.owner_id == owner_id)

    if is_vaccinated is not None:
        cats = cats.filter(Cat.vaccinated == is_vaccinated)
    cats = cats.limit(limit).offset(offset).all()
    return cats


async def get_cat(cat_id: int, db: Session):
    """
    The get_cat function returns a cat object from the database.

    :param cat_id: int: Specify the id of the cat we want to get
    :param db: Session: Pass in the database session
    :return: The cat with the given id
    :doc-author: Trelent
    """
    cat = db.query(Cat).filter_by(id=cat_id).first()
    return cat


async def create_cat(body: PetModel, db: Session):
    """
    The create_cat function creates a new cat in the database.

    :param body: PetModel: Define the type of data that is expected to be passed into the function
    :param db: Session: Access the database
    :return: The cat that was created
    :doc-author: Trelent
    """
    cat = Cat(**body.dict())
    db.add(cat)
    db.commit()
    db.refresh(cat)
    return cat


async def update_cat(body: PetModel, cat_id: int, db: Session):
    """
    The update_cat function updates a cat in the database.
        Args:
            body (PetModel): The PetModel object containing the new data for the cat.
            cat_id (int): The id of the Cat to update.
            db (Session): A Session instance used to query and commit changes to our database.

    :param body: PetModel: Get the data from the request body
    :param cat_id: int: Specify which cat to update
    :param db: Session: Access the database
    :return: The updated cat object
    :doc-author: Trelent
    """
    cat = db.query(Cat).filter_by(id=cat_id).first()
    if cat:
        cat.nickname = body.nickname
        cat.age = body.age
        cat.vaccinated = body.vaccinated
        cat.description = body.description
        cat.owner_id = body.owner_id
        db.commit()
    return cat


async def update_vaccinated_cat(body: PetStatusVaccinated, cat_id: int, db: Session):
    """
    The update_vaccinated_cat function updates the vaccinated status of a cat in the database.


    :param body: PetStatusVaccinated: Pass the pet status vaccinated object to the function
    :param cat_id: int: Identify the cat that is being updated
    :param db: Session: Access the database
    :return: The cat object
    :doc-author: Trelent
    """
    cat = db.query(Cat).filter_by(id=cat_id).first()
    if cat:
        cat.vaccinated = body.vaccinated
        db.commit()
    return cat


async def remove_cat(cat_id: int, db: Session):
    """
    The remove_cat function removes a cat from the database.
        Args:
            cat_id (int): The id of the cat to remove.
            db (Session): A connection to the database.

    :param cat_id: int: Specify the id of the cat to be removed
    :param db: Session: Pass the database session to the function
    :return: A cat object
    :doc-author: Trelent
    """
    cat = db.query(Cat).filter_by(id=cat_id).first()
    if cat:
        db.delete(cat)
        db.commit()
    return cat
