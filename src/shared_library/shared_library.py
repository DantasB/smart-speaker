import tempfile


def generate_workfolder() -> tempfile.TemporaryDirectory:
    """Generates a workfolder

    Returns:
        tempfile.TemporaryDirectory: the temporary directory generated
    """
    temp_dir = tempfile.TemporaryDirectory()
    return temp_dir


def delete_workfolder(directory: tempfile.TemporaryDirectory) -> None:
    """Deletes the temporary directory generated

    Args:
        directory (tempfile.TemporaryDirectory): the directory path
    """
    directory.cleanup()
