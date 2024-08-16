# Spotify Stats App

Spotify Stats App is a web application that allows users to log in with their Spotify account and view their top tracks, artists, and albums over different time ranges. The application is built using Flask for the backend and Spotipy to interact with the Spotify API.

## Features

- User authentication with Spotify
- View top tracks for the last 4 weeks, 6 months, and all time
- View top artists for the last 4 weeks, 6 months, and all time
- View top albums for the last 4 weeks, 6 months, and all time
- Responsive design with grid and list views
- Search functionality to filter tracks

## Screenshots

![Home Page](static/images//homepage-screenshot.png)
![Top Tracks](static/images/top-tracks-screenshot.png)
![Top Artists](static/images/top-artists-screenshot.png)
![Top Albums](static/images/top-albums-screenshot.png)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/ehijeleb/spotify-stats-app.git
   cd spotify-stats-app
   ```

2. Create a virtual environment and activate it:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Set up your Spotify API credentials:

   1. Go to [Spotify Developer Dashboard](https://developer.spotify.com/)
   2. Log in with your Spotify account
   3. Go to the dashboard and create a new app
   4. Make sure `http://localhost:5000/callback` is added to the Redirect URIs in the app settings
   5. You now have access to your client ID and client secret
   6. edit the `config.py` file in the root directory and add your Spotify API credentials:

   ```python
   SPOTIPY_CLIENT_ID = 'your-client-id'
   SPOTIPY_CLIENT_SECRET = 'your-client-secret'
   SPOTIPY_REDIRECT_URI = 'http://localhost:5000/callback'
   ```

5. Run the application:

   ```bash
   flask run
   ```

6. Open your browser and navigate to `http://localhost:5000`.

## Usage

- Navigate to the home page and click "Login with Spotify".
- Log in to your Spotify account and authorize the application.
- View your top tracks, artists, and albums by selecting the respective links.

## Technologies Used

- Python
- Flask
- Spotipy (Spotify Web API Wrapper)
- HTML/CSS
- JavaScript

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Contact

For any inquiries or issues, please contact me at [benedict.ibha@gmail.com].
