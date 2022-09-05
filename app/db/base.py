# Import all the models, so that Base has them before being imported by alembic
from app.db.base_class import Base  # noqa: F401
from app.models.button import Button  # noqa: F401
from app.models.button_message import ButtonMessage  # noqa: F401
from app.models.card import Card  # noqa: F401
from app.models.card_button import CardButton  # noqa: F401
from app.models.carousel_message import CarouselMessage  # noqa: F401
from app.models.message import Message  # noqa: F401
from app.models.message_button import MessageButton  # noqa: F401
from app.models.text_message import TextMessage  # noqa: F401
from app.models.way import Way  # noqa: F401
