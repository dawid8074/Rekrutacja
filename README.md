OpenAI HTML Generator
Opis projektu
Aplikacja napisana w Pythonie, która:

1. Łączy się z API OpenAI.
2. Wczytuje plik tekstowy zawierający artykuł.
3. Przetwarza treść artykułu za pomocą API OpenAI, generując odpowiednio sformatowany kod HTML.
4. Zapisuje wygenerowany kod w pliku artykul.html.

Wygenerowany kod HTML zawiera:
*Strukturalne tagi HTML (np. h1, p, img).
*Miejsca na grafiki oznaczone za pomocą tagów <img> z atrybutami src="image_placeholder.jpg" oraz alt zawierającym opis promptu.
*Podpisy pod grafikami, dodane za pomocą odpowiednich znaczników HTML.

------------------------------------------------------------------------
Instalacja
1. Sklonuj repozytorium:
2. Zainstaluj wymagane biblioteki: Użyj pip do zainstalowania wymaganych pakietów.
3. Przygotuj klucz API OpenAI:
	Utwórz plik .env w katalogu głównym projektu.
	Wprowadź swój klucz API w formacie:
      OPENAI_API_KEY=twój-klucz-api

-------------------------------------------------------------------------
Uruchamianie aplikacji
1. Umieść plik tekstowy z artykułem w katalogu głównym projektu pod nazwą TextIn.txt.
2. Uruchom skrypt:
	python Main.py
3. Po zakończeniu działania aplikacji, wynik zostanie zapisany w pliku artykul.html w katalogu głównym.


