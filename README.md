# YouTube Video Manager

""A simple Python command-line application to manage your YouTube video collection"". Store, organize, and keep track of video names and durations locally.

## Features

- **List All Videos**: View all videos in your collection with their names and durations
- **Add New Video**: Add a new video to your collection by entering the video name and duration
- **Update Video**: Modify the name or duration of an existing video
- **Delete Video**: Remove a video from your collection
- **Persistent Storage**: All videos are saved to a local JSON file for permanent storage

## Requirements

- Python 3.10+ (uses `match` statement for pattern matching)
- No external dependencies required

## Installation

1. Clone or download this repository
2. Navigate to the project directory:
   ```
   cd directory-name
   ```

## Usage

Run the application:
```bash
python directory-name.py
```

### Menu Options

When you run the application, you'll see the following menu:

```
YouTube Manager | Choose any option
1. List all Youtube Videos
2. Add a youtube video
3. Update a youtube Video details
4. Delete a youtube video
5. Exit
```

## Data Storage
Videos are stored in `youtube.txt` as a JSON array with the following format:

```json
[
  {"name": "Video Title", "time": "Duration"},
  {"name": "Another Video", "time": "45 mins"}
]
```