Zootopia with Api and GitHub

## How to Run

1️⃣ Clone the Repository

git clone https://github.com/<your-username>/<your-repo-name>.git
cd <your-repo-name>

2️⃣ Set Up the Environment

Make sure you have Python 3.8+ installed.

Create a virtual environment (optional but recommended):

python -m venv venv
source venv/bin/activate   # on macOS/Linux
venv\Scripts\activate      # on Windows

Install required packages:

pip install requests python-dotenv

3️⃣ Get an API Key

Go to API Ninjas

Create an account (free tier available)

Copy your API key

4️⃣ Set Up Your .env File

Create a file named .env in the project root and add:

API_KEY=your_api_key_here

5️⃣ Run the Script
python app.py


Enter an animal name when prompted, for example:

Enter a name of an animal: fox

The script will generate a file named animals.html in the project directory.

6️⃣ View the Result

Open animals.html in your browser to see the generated webpage:

open animals.html          # macOS
xdg-open animals.html      # Linux
start animals.html         # Windows

