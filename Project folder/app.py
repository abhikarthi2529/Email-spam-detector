from flask import Flask, request, render_template
import CleanedData as CD
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

app = Flask(__name__)
data = CD.cleanedData()
vectorizer = TfidfVectorizer(max_features=1000, stop_words="english")
x_label = vectorizer.fit_transform(data["text"])
y_label = data["spam"]
x_train, x_test, y_train, y_test = train_test_split(
    x_label, y_label, test_size=0.2, random_state=42
)
model = LogisticRegression()
model.fit(x_train, y_train)
accuracy = model.score(x_test, y_test)


@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    error = None
    if request.method == "POST":
        try:
            user_email = request.form["email"]
            if not user_email.strip():
                error = "Please enter email content."
            elif vectorizer is None or model is None:
                error = "Model not initialized."
            else:
                email_vector = vectorizer.transform([user_email])
                result = model.predict(email_vector)[0]
                if(result == 1):
                    prediction = "Spam"
                else: 
                    prediction = "Not Spam"
        except Exception as e:
            error = f"Error processing email: {str(e)}"

    return render_template(
        "index.html",
        prediction=prediction,
        accuracy=round(accuracy * 100, 2),
        error=error,
    )


if __name__ == "__main__":
    app.run(debug=True)
