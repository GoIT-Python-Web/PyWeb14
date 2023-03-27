import unittest
from unittest.mock import MagicMock

from sqlalchemy.orm import Session

from src.schemas import PetModel
from src.database.models import Cat, Owner
from src.repository.cats import (
    get_cats,
    get_cat,
    create_cat,
    update_cat,
    update_vaccinated_cat,
    remove_cat
)


class TestNotes(unittest.IsolatedAsyncioTestCase):

    def setUp(self):
        self.session = MagicMock(spec=Session)
        self.owner = Owner(id=1, email="owner_test@test.com")

    async def test_get_cats(self):
        cats = [Cat(), Cat(), Cat()]
        self.session.query().filter().filter().limit().offset().all.return_value = cats
        result = await get_cats(10, 0, self.owner.id, False, self.session)
        self.assertEqual(result, cats)

    async def test_get_cats_without_vaccinated(self):
        cats = [Cat(), Cat(), Cat()]
        self.session.query().filter().limit().offset().all.return_value = cats
        result = await get_cats(10, 0, self.owner.id, None, self.session)
        self.assertEqual(result, cats)

    async def test_get_cats_without_owner(self):
        cats = [Cat(), Cat(), Cat()]
        self.session.query().filter().limit().offset().all.return_value = cats
        result = await get_cats(10, 0, None, True, self.session)
        self.assertEqual(result, cats)

    async def test_get_cats_without_vaccinated_and_owner(self):
        cats = [Cat(), Cat(), Cat()]
        self.session.query().limit().offset().all.return_value = cats
        result = await get_cats(10, 0, None, None, self.session)
        self.assertEqual(result, cats)

    async def test_create_cats(self):
        body = PetModel(
            nickname='Simon',
            age=4,
            vaccinated=False,
            description='Дуже багато мяукає',
            owner_id=self.owner.id
        )

        result = await create_cat(body=body, db=self.session)
        self.assertEqual(result.nickname, body.nickname)
        self.assertEqual(result.description, body.description)
        self.assertEqual(result.vaccinated, body.vaccinated)
        self.assertEqual(result.owner_id, self.owner.id)
        self.assertTrue(hasattr(result, "id"))

    async def test_update_cat_found(self):
        body = PetModel(
            nickname='Simon',
            age=4,
            vaccinated=False,
            description='Дуже багато мяукає',
            owner_id=self.owner.id
        )

        cat = Cat(
            nickname='Barsik',
            age=3,
            vaccinated=False,
            description='Дуже мяукає',
            owner_id=self.owner.id
        )

        self.session.query().filter_by().first.return_value = cat
        self.session.commit.return_value = None
        result = await update_cat(body=body, cat_id=cat.id, db=self.session)

        self.assertEqual(result, cat)
        self.assertEqual(result.nickname, body.nickname)
        self.assertEqual(result.description, body.description)
        self.assertEqual(result.vaccinated, body.vaccinated)
        self.assertEqual(result.owner_id, self.owner.id)
        self.assertTrue(hasattr(result, "id"))


if __name__ == '__main__':
    unittest.main()
