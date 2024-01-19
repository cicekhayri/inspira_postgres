from inspira.decorators.http_methods import get, post
from inspira.decorators.path import path
from inspira.responses import TemplateResponse, HttpResponseRedirect
from inspira.requests import Request

from src.service.user_service import UserService


@path("/users")
class UserController:

    def __init__(self, user_service: UserService):
        self._user_service = user_service

    @get()
    async def get_users(self, request: Request):
        users = self._user_service.get_all_user()
        context = {
            "users": users
        }

        return TemplateResponse("users.html", context)

    @get("/create")
    async def render_form(self, request: Request):
        return TemplateResponse("create_user_form.html")

    @post("/create")
    async def create_user(self, request: Request):
        body = await request.form()
        name = body['name']
        email = body['email']

        success = self._user_service.create_user(name, email)

        if success:
            return HttpResponseRedirect("/users")
        else:
            return HttpResponseRedirect("/users", status_code=400)
