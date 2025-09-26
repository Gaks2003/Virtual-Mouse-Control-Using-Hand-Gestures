# Virtual Mouse Control Using Hand Gestures

A computer vision-based application that enables hands-free mouse control through hand gesture recognition. Built with OpenCV, MediaPipe, and PyAutoGUI, this project translates real-time hand movements into precise mouse operations.

## Features

- **Real-time Hand Tracking**: Uses MediaPipe for accurate hand landmark detection
- **Mouse Movement**: Index finger controls cursor position
- **Click Gesture**: Pinch index finger and thumb together
- **Drag & Drop**: Hold pinch gesture to drag objects
- **Scroll Control**: Middle finger up/down for scrolling
- **App Switching**: Three fingers together triggers Alt+Tab
- **Visual Feedback**: On-screen gesture indicators

## Project Structure

```
virtual-mouse-control/
├── .github/
│   └── workflows/
│       └── ci-cd.yml       # GitHub Actions pipeline
├── src/
│   └── app.py              # Main application file
├── tests/
│   └── test_app.py         # Unit tests
├── Dockerfile              # Container configuration
├── docker-compose.yml      # Docker Compose setup
├── deploy.sh               # Deployment script
├── Makefile               # Build automation
├── setup.py               # Package configuration
├── requirements.txt       # Python dependencies
└── README.md             # Project documentation
```

## Requirements

- Python 3.7+
- Webcam
- Windows/macOS/Linux

## Installation

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd virtual-mouse-control
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Run the application:**
   ```bash
   cd src
   python app.py
   ```

2. **Position yourself:**
   - Sit 2-3 feet from your webcam
   - Ensure good lighting
   - Keep hand visible in the camera frame

3. **Control gestures:**
   - **Move Cursor**: Point with index finger
   - **Click**: Pinch index finger and thumb (distance < 3cm)
   - **Scroll Up**: Raise middle finger above index finger
   - **Scroll Down**: Lower middle finger below index finger
   - **Drag**: Hold pinch gesture and move
   - **Switch Apps**: Bring index, middle, and ring fingers together

4. **Exit**: Press `ESC` key to quit

## Technical Details

### Libraries Used
- **OpenCV**: Video capture and image processing
- **MediaPipe**: Hand landmark detection and tracking
- **PyAutoGUI**: Mouse control and automation
- **Math**: Distance calculations for gesture recognition

### Gesture Recognition Logic
- Hand landmarks are detected using MediaPipe's hand tracking model
- Euclidean distance between fingertips determines gesture states
- Screen coordinates are mapped from normalized hand positions
- Gesture thresholds are optimized for reliable detection

### Performance Optimizations
- Single hand detection for better performance
- Minimal detection confidence threshold (0.7)
- Reduced PyAutoGUI pause time (0.01s)
- Failsafe disabled for smooth operation

## Troubleshooting

- **Camera not detected**: Check webcam permissions and connections
- **Gestures not responsive**: Adjust lighting and hand positioning
- **High CPU usage**: Close other applications using the camera
- **Import errors**: Ensure all dependencies are installed correctly

## Future Enhancements

- Multi-hand support
- Customizable gesture sensitivity
- Voice commands integration
- Gesture recording and playback
- Cross-platform optimization

## Deployment

### Local Development
```bash
make install    # Install dependencies
make run        # Run application
make test       # Run tests
make lint       # Code linting
```

### Docker Deployment
```bash
make build      # Build Docker image
make docker-run # Run with Docker Compose
make deploy     # Full deployment
```

### CI/CD Pipeline
- Automated testing on Python 3.8, 3.9, 3.10
- Code linting with flake8
- Docker image building
- Artifact generation

## Contributing

Contributions are welcome! Please feel free to submit pull requests or open issues for bugs and feature requests.