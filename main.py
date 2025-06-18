import datetime
import time
from typing import Union, Optional


def timestamp_to_epoch(timestamp: str, format_str: Optional[str] = None) -> float:
    """
    Convert a timestamp string to epoch time (seconds since January 1, 1970).
    
    Args:
        timestamp (str): The timestamp string to convert.
        format_str (Optional[str]): The format of the timestamp string.
            If None, the function will try to parse the timestamp as an ISO format.
    
    Returns:
        float: The epoch time in seconds.
    
    Examples:
        >>> timestamp_to_epoch("2023-01-01T12:00:00Z")
        1672574400.0
        >>> timestamp_to_epoch("01/01/2023 12:00:00", "%m/%d/%Y %H:%M:%S")
        1672574400.0
    """
    if format_str:
        dt = datetime.datetime.strptime(timestamp, format_str)
        # If the format doesn't include timezone info, assume UTC
        if dt.tzinfo is None:
            dt = dt.replace(tzinfo=datetime.timezone.utc)
    else:
        # Try to parse as ISO format
        dt = datetime.datetime.fromisoformat(timestamp.replace('Z', '+00:00'))
    
    # Convert to epoch time
    return dt.timestamp()


def epoch_to_timestamp(epoch_time: Union[int, float], format_str: str = "%Y-%m-%dT%H:%M:%SZ") -> str:
    """
    Convert epoch time to a formatted timestamp string.
    
    Args:
        epoch_time (Union[int, float]): The epoch time in seconds.
        format_str (str): The desired format of the output timestamp string.
            Default is ISO 8601 format.
    
    Returns:
        str: The formatted timestamp string.
    
    Examples:
        >>> epoch_to_timestamp(1672574400)
        '2023-01-01T12:00:00Z'
        >>> epoch_to_timestamp(1672574400, "%m/%d/%Y %H:%M:%S")
        '01/01/2023 12:00:00'
    """
    dt = datetime.datetime.fromtimestamp(epoch_time, tz=datetime.timezone.utc)
    return dt.strftime(format_str)
