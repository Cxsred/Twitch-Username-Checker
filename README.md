<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Twitch Username Availability Checker</title>
</head>
<body>
    <h1>Twitch Username Availability Checker 🎮🔍</h1>
    <p>Welcome to the <strong>Twitch Username Availability Checker</strong>! 🎉 This bot helps you check if a Twitch username is available or already taken. Using the Twitch API, you can easily verify if your desired username is free to register. 💻</p>

    <h2>✨ Features</h2>
    <ul>
        <li>Check if a Twitch username is available or not. ✅❌</li>
        <li>Supports both <strong>Slash Commands</strong> and <strong>Prefix Commands</strong> on Discord. 🤖</li>
        <li>Built with Python and the <strong>discord.py</strong> library. 📚</li>
    </ul>

    <h2>📦 Installation</h2>
    <ol>
        <li><strong>Clone the repository</strong> to your local machine:
            <pre><code>git clone https://github.com/yourusername/twitch-username-checker.git</code></pre>
        </li>
        <li><strong>Navigate to the project folder</strong>:
            <pre><code>cd twitch-username-checker</code></pre>
        </li>
        <li><strong>Create and activate a virtual environment</strong> (optional but recommended):
            <ul>
                <li>For Windows:
                    <pre><code>python -m venv venv</code></pre>
                    <pre><code>venv\Scripts\activate</code></pre>
                </li>
                <li>For Mac/Linux:
                    <pre><code>python3 -m venv venv</code></pre>
                    <pre><code>source venv/bin/activate</code></pre>
                </li>
            </ul>
        </li>
        <li><strong>Install the required dependencies</strong>:
            <pre><code>pip install -r requirements.txt</code></pre>
        </li>
    </ol>

    <h2>🔑 .env File</h2>
    <p>The <strong>.env</strong> file has already been created in the repository with the following keys:</p>
    <pre><code>
DISCORD_BOT_TOKEN=
TWITCH_CLIENT_ID=
TWITCH_APP_ACCESS_TOKEN=
    </code></pre>
    <p>Simply <strong>fill in the empty fields</strong> with your own secret values.</p>
    <p><strong>DO NOT commit</strong> your actual secrets to the repository. 🔐</p>
    <p>Make sure the <strong>.env</strong> file is kept private to protect your credentials. 🚫</p>

    <h2>⚙️ Setup and Configuration</h2>
    <ol>
        <li><strong>Create a Twitch Developer Account</strong> and get your <strong>Client ID</strong> and <strong>Access Token</strong>:
            <ul>
                <li>You can get your credentials from the <a href="https://dev.twitch.tv/console/apps" target="_blank">Twitch Developer Console</a>.</li>
            </ul>
        </li>
        <li><strong>Fill in the .env file</strong> with the following keys:
            <ul>
                <li><strong>DISCORD_BOT_TOKEN</strong>: Your Discord bot token.</li>
                <li><strong>TWITCH_CLIENT_ID</strong>: Your Twitch client ID.</li>
                <li><strong>TWITCH_APP_ACCESS_TOKEN</strong>: Your Twitch app access token.</li>
            </ul>
        </li>
    </ol>

    <h2>🚀 Usage</h2>
    <p>Once the bot is set up and running, you can use it on Discord with the following commands:</p>
    <h3>Slash Command</h3>
    <pre><code>/tw username</code></pre>
    <p>Check if the username is available on Twitch.</p>

    <h3>Prefix Command</h3>
    <pre><code>!tw username</code></pre>
    <p>Check if the username is available on Twitch.</p>

    <p>Both commands will return the availability of the username: ✅ if it's available, ❌ if it's already taken.</p>

    <h2>🛠️ Dependencies</h2>
    <ul>
        <li><strong>discord.py</strong>: To interact with Discord's API.</li>
        <li><strong>requests</strong>: To make HTTP requests to the Twitch API.</li>
        <li><strong>python-dotenv</strong>: To manage environment variables.</li>
    </ul>
    <p>Install them by running:
        <pre><code>pip install discord.py requests python-dotenv</code></pre>
    </p>

    <h2>🎉 Contributing</h2>
    <p>Feel free to open an issue or submit a pull request if you want to contribute! 🙌</p>
    <p>Please make sure to follow the repository's guidelines when submitting changes. 📜</p>

    <h2>📜 License</h2>
    <p>This project is licensed under the MIT License - see the <a href="LICENSE" target="_blank">LICENSE</a> file for details.</p>

    <h2>💬 Support</h2>
    <p>If you have any questions or need support, feel free to open an issue in this repository. 😄</p>
</body>
</html>
