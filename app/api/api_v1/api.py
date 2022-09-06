from fastapi import APIRouter

from app.api.api_v1.endpoints import (
    button_messages,
    buttons,
    cards,
    carousel_messages,
    messages,
    text_messages,
    ways,
)

api_router = APIRouter()
api_router.include_router(buttons.router, prefix="/buttons", tags=["Buttons"])
api_router.include_router(
    button_messages.router,
    prefix="/messages/button",
    tags=["Messages", "Button messages"],
)
api_router.include_router(cards.router, prefix="/cards", tags=["Cards"])
api_router.include_router(
    carousel_messages.router,
    prefix="/messages/carousel",
    tags=["Messages", "Carousel messages"],
)
api_router.include_router(
    text_messages.router, prefix="/messages/text", tags=["Messages", "Text messages"]
)
api_router.include_router(messages.router, prefix="/messages", tags=["Messages"])
api_router.include_router(ways.router, prefix="/ways", tags=["Ways"])
