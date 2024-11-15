"""
Some useful tools
"""


def get_duration_string(duration):
    """
    Converts duration in seconds to string
    """
    return f"{duration // 60}:{duration % 60:02}"
