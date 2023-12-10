# FrameShift

FrameShift is a Python tool to create a unique visual effect in videos. It works by duplicating a video, inverting the colors of the duplicate, applying semi-transparency, and then overlaying it with a time-shift. This effect highlights the differences between frames, revealing changes over time in a visually striking way.

It will take an input video and create an output that visualizes only the things that change 

Inspired by: [Motion Extraction by Posy](https://www.youtube.com/watch?v=NSS6yAMZF78)

## Installation

install dependencies

```bash
pip install -r requirements.txt
```

## Usage

Run the python file directly

```bash
python frame_shifter.py input.mp4 1000 output.mp4 --duration 20
```

Or use it in your code

```python
from frame_shifter import process_video

# Example usage
process_video("input_video.mp4", 1000, "output_video.mp4")
```

### Parameters

`input_video_path`: Path to the input video file.
`time_shift_ms`: The time shift in milliseconds.
`output_video_path`: Path where the output video will be saved.
`duration` (optional): Duration of the video clip to process.
`frame_shift` (optional): Number of frames to shift instead of time in milliseconds.

note: If both `time_shift_ms` and `frame_shift` are used, both will be applied
