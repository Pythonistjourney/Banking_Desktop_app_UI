# Banking Desktop Application

A modern desktop banking application built with PySide6, featuring a beautiful UI and essential banking functionalities.

## Features

- User authentication (login/signup)
- Account dashboard
- Transaction history
- Money transfer
- User profile management
- Modern and responsive UI
- Smooth animations and transitions

## Requirements

- Python 3.8 or higher
- PySide6
- Pillow
- python-dotenv

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/banking-desktop-app.git
cd banking-desktop-app
```

2. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running the Application

1. Activate your virtual environment if not already activated:
```bash
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Run the application:
```bash
python src/main.py
```

## Project Structure

```
banking-desktop-app/
├── src/
│   ├── ui/
│   │   ├── screens/
│   │   │   ├── login.py
│   │   │   ├── signup.py
│   │   │   ├── dashboard.py
│   │   │   └── splash.py
│   │   └── navigation/
│   │       └── navigation_manager.py
│   ├── context/
│   │   └── user_context.py
│   ├── services/
│   │   └── transaction_service.py
│   ├── utils/
│   │   └── avatar_generator.py
│   └── styles/
│       ├── global.qss
│       ├── login.qss
│       ├── signup.qss
│       ├── dashboard.qss
│       └── splash.qss
├── assets/
│   └── images/
│       ├── recipients/
│       └── users/
├── requirements.txt
└── README.md
```

## Demo Account

For testing purposes, you can use the following demo account:
- Email: user@example.com
- Password: password123

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.
