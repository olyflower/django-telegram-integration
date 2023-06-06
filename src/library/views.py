import asyncio
from django.conf import settings
from django.db.models import Q
from django.template.loader import render_to_string
from django.shortcuts import render, get_object_or_404
from django.views import View
from telegram import Bot
from telegram.constants import ParseMode
from library.models import Book


class IndexView(View):
    template_name = "index.html"

    def get(self, request):
        search = request.GET.get("search_text")
        books = Book.objects.all()

        if search:
            search_fields = ["title", "author"]
            or_filter = Q()
            for field in search_fields:
                or_filter |= Q(**{f"{field}__istartswith": search})
            books = books.filter(or_filter)

        return render(request, self.template_name, {"books": books})


def book_detail(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    asyncio.run(book_info(book))
    return render(request, 'library/book_info.html', {'book': book})


async def book_info(book):
    message = render_to_string('library/book_info.html', {'book': book})
    bot = Bot(token=settings.BOT_TOKEN)
    await bot.send_message(
        chat_id=settings.CHAT_ID,
        text=message,
        parse_mode=ParseMode.HTML
    )
