from flask import Flask, request, render_template


app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def guess_the_number():
    """
    Main function of the game.
    Think the number (1 - 1000) and computer will guess it in up to 10 tries.

    allowed methods: GET, POST.
    templates: 4_start.html, 4_form.html, 4_end.html.
    """
    if request.method == "POST":  # pobieramy wartości z ukrytych pól o polu 'name=...'
        min_number = int(request.form.get("min"))
        max_number = int(request.form.get("max"))
        user_answer = request.form.get("user_answer")  # wybór użytkownika
        guess = int(request.form.get("guess", 500))

        if user_answer == "too big":  # zawężamy zakres zgadywania
            max_number = guess
        elif user_answer == "too small":
            min_number = guess
        elif user_answer == "won":
            return render_template("4_end.html").format(guess=guess)

        guess = ((max_number - min_number) // 2) + min_number  # obliczenie nowej liczby

        return render_template("4_form.html").format(guess=guess, min=min_number, max=max_number)

    else:  # GET
        return render_template("4_start.html").format(0, 1000)


if __name__ == "__main__":
    app.run(debug=True)
