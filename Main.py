# from openai import OpenAI
#
# def odczytaj_plik(sciezka):
#     """
#     Funkcja do odczytu zawartości pliku tekstowego.
#
#     :param sciezka: Ścieżka do pliku tekstowego.
#     :return: Zawartość pliku jako string.
#     """
#     try:
#         with open(sciezka, "r", encoding="utf-8") as plik:
#             zawartosc = plik.read()
#         return zawartosc
#     except FileNotFoundError:
#         return f"Błąd: Plik o ścieżce '{sciezka}' nie istnieje."
#     except Exception as e:
#         return f"Błąd: {e}"
#
# plik = odczytaj_plik("TextIn.txt")
#
# client = OpenAI()
#
# completion = client.chat.completions.create(
#     model="gpt-4o-mini",
#     messages=[
#         {"role": "system", "content": "You are a helpful assistant."},
#         {
#             "role": "user",
#             "content": "Napisz coś ciekawego"
#         }
#     ]
# )
#
# print(completion.choices[0].message)
#


import openai
from openai import OpenAI


def odczytaj_plik(sciezka):
    """
    Funkcja do odczytu zawartości pliku tekstowego.

    :param sciezka: Ścieżka do pliku tekstowego.
    :return: Zawartość pliku jako string.
    """
    try:
        with open(sciezka, "r", encoding="utf-8") as plik:
            zawartosc = plik.read()
        return zawartosc
    except FileNotFoundError:
        return f"Błąd: Plik o ścieżce '{sciezka}' nie istnieje."
    except Exception as e:
        return f"Błąd: {e}"

def zapisz_do_HTML(sciezka, zawartosc):
    """
    Funkcja do zapisywania zawartości do pliku.

    :param sciezka: Ścieżka do pliku.
    :param zawartosc: Zawartość do zapisania.
    """
    try:
        with open(sciezka, "w", encoding="utf-8") as plik:
            plik.write(zawartosc)
    except Exception as e:
        print(f"Błąd podczas zapisywania pliku: {e}")




client = OpenAI()
# Odczytaj zawartość pliku wejściowego
sciezka_wejsciowa = "TextIn.txt"
tekst = odczytaj_plik(sciezka_wejsciowa)

if "Błąd" in tekst:
    print(tekst)
else:
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {
                    "role": "user",
                    "content": f"Przekonwertuj poniższy tekst na dokument HTML:\n\n{tekst}. Dodatkowe wymagania: \n "
                               f"-Brak kodu CSS oraz JavaScript. Jedyne co masz zwróćić to kod HTML."
                               f"-Zwrócony kod powinien zawierać wyłącznie zawartość do wstawienia między tagami <body></body>."
                               f"-Nie dołączaj znaczników <head> oraz <body>."
                               f"-Do strukturyzaji danych użyj odpowiednich znaczników."
                               f"-Wybierz odpowiednie miejsca do wstawienia grafik. Są trzy rozdziały więc do każdego z nich dołącz grafikę wedlę następujących instrukcji:"
                               f"*Oznacz je takgiem img z atrybutem src='image_placeholder.jpg'."
                               f"*Do każdego zdjęcia dodaj atrybut alt z dokładnym i szczegółowym zapytaniem do AI,którego można użyć do wygenerowania grafiki. "
                               f"*Dodaj podpisy pod grafikami używając odpowiedniego tagu HTML."
                               f"*Grafiki powinny nawiązywać do nastęującego po nim akapitu jednak nie muszą występować od razu po tytule."
                               f"Zwróć jako tekst. Nie cytuj i nie używaj swojego formatowania"
                }
            ]
        )

        # Pobierz treść odpowiedzi (tylko kod HTML)
        html_output = response.choices[0].message.content

        # Zapisz wynik do pliku
        sciezka_wyjsciowa = "artykul.html"
        zapisz_do_HTML(sciezka_wyjsciowa, html_output)

        print(f"Plik HTML został zapisany jako '{sciezka_wyjsciowa}'.")

    except Exception as e:
        print(f"Błąd podczas komunikacji z OpenAI API: {e}")
