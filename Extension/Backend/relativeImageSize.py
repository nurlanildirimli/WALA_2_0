import subprocess
import json
import os


def get_effective_image_sizes(webpage_url, screen_size):
    try:
        script_dir = os.path.dirname(os.path.realpath(__file__))  # Get the directory of the current Python script
        process = subprocess.Popen(
            ['node', 'relativeImageSize.js', webpage_url, str(screen_size[0]), str(screen_size[1])],
            stdout=subprocess.PIPE, cwd=script_dir)
        output, _ = process.communicate()

        image_data = json.loads(output)

        return image_data
    except Exception as e:
        print(f"Error: {e}")
        return []
