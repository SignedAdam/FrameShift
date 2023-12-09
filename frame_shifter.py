from moviepy.editor import VideoFileClip, CompositeVideoClip
import numpy as np
import cv2
import argparse

def invert_colors(frame):
    return cv2.bitwise_not(frame)

def make_half_transparent(frame):
    return cv2.addWeighted(frame, 0.5, frame, 0, 0)


def invert_colors2(frame):
    """Invert the colors of a video frame."""
    return 255 - frame


def process_video(input_video_path, time_shift_ms, output_video_path, duration=None, frame_shift=None):
    # Load the original video
    clip = VideoFileClip(input_video_path)

    # Apply the duration if provided
    if duration:
        clip = clip.subclip(0, duration)

    # Duplicate and invert colors
    inverted_clip = clip.fl_image(invert_colors)

    # Apply half transparency
    inverted_clip = inverted_clip.set_opacity(0.5)

    # Time shift
    if frame_shift:
        fps = clip.fps
        time_shift_ms = frame_shift / fps * 1000
    inverted_clip = inverted_clip.set_start(time_shift_ms / 1000.0)

    # Overlay the inverted clip on the original
    final_clip = CompositeVideoClip([clip, inverted_clip.set_position("center")])

    # Write the result to a file
    final_clip.write_videofile(output_video_path, codec="libx264", audio_codec="aac")
                               

def main():
    # Parse command line arguments
    parser = argparse.ArgumentParser(description="Video editor that duplicates, inverts, and makes a video half transparent with a time shift.")
    parser.add_argument("input_video", help="Path to the input video file.")
    parser.add_argument("time_shift_ms", type=int, help="Time shift in milliseconds between the original and processed video.")
    parser.add_argument("output_video", help="Path to the output video file.")
    parser.add_argument("--duration", type=float, help="Duration of the video to process in seconds.", default=None) # the rest is skipped
    parser.add_argument("--frame_shift", type=int, help="Frame shift count between the original and processed video.", default=None)
    args = parser.parse_args()

    # Example usage:
    # python video_editor.py input.mp4 500 output.mp4 --duration 50 --frame_shift 10
    # This will process 'input.mp4' applying a 500 millisecond time shift and an additional 10 frame shift, and save 50 seconds of the result to 'output.mp4'

    # Process the video
    process_video(args.input_video, args.time_shift_ms, args.output_video, args.duration, args.frame_shift)

if __name__ == "__main__":
    main()
