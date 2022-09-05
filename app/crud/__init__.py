from app.models.button import Button
from app.models.button_message import ButtonMessage
from app.models.carousel_message import CarouselMessage
from app.models.message import Message
from app.models.text_message import TextMessage
from app.models.way import Way
from app.schemas.button import ButtonCreate, ButtonUpdate
from app.schemas.button_message import ButtonMessageCreate, ButtonMessageUpdate
from app.schemas.carousel_message import CarouselMessageCreate, CarouselMessageUpdate
from app.schemas.message import MessageCreate, MessageUpdate
from app.schemas.text_message import TextMessageCreate, TextMessageUpdate
from app.schemas.way import WayCreate, WayUpdate

from .base import CRUDBase
from .card import card  # noqa: F401
from .card_button import card_button  # noqa: F401
from .message_button import message_button  # noqa: F401

button = CRUDBase[Button, ButtonCreate, ButtonUpdate](Button)
button_message = CRUDBase[ButtonMessage, ButtonMessageCreate, ButtonMessageUpdate](
    ButtonMessage
)
carousel_message = CRUDBase[
    CarouselMessage, CarouselMessageCreate, CarouselMessageUpdate
](CarouselMessage)
message = CRUDBase[Message, MessageCreate, MessageUpdate](Message)
text_message = CRUDBase[TextMessage, TextMessageCreate, TextMessageUpdate](TextMessage)
way = CRUDBase[Way, WayCreate, WayUpdate](Way)
