import html


def format_ad_message(ad):

    def escape_text(text):
        if text is None:
            return ""
        return html.escape(str(text))
    
    parts = []

    if ad.get("title"):
        parts.append(f"<b>{escape_text(ad['title'])}</b>")

    if ad.get("rent"):
        parts.append(f"💰 <b>Цена:</b> {escape_text(ad['rent'])}")

    if ad.get("rent_description"):
        parts.append(f"📝 {escape_text(ad['rent_description'])}")
    
    if ad.get("adress"):
        parts.append(f"📍 <b>Адрес:</b> {escape_text(ad['adress'])}")
    
    if ad.get("url"):
        # Экранируем URL для безопасности
        escaped_url = escape_text(ad['url'])
        parts.append(f"🔗 <a href='{escaped_url}'>Ссылка на объявление</a>")
    
    if ad.get("description"):
        # Обрезаем длинное описание
        description = escape_text(ad['description'])
        if len(description) > 300:
            description = description[:300] + "..."
        parts.append(f"📋 <b>Описание:</b>\n{description}")
    
    if ad.get("data"):
        parts.append(f"📅 <b>Дата размещения:</b> {escape_text(ad['data'])}")
    
    if ad.get("source"):
        parts.append(f"🏷️ <b>Сервис:</b> {escape_text(ad['source'])}")
    
    message = "\n\n".join(parts)
    
    return message