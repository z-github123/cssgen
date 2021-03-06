

class WritePv(object):
    """
    Action that writes the specified value to a named PV.
    """

    def __init__(self, pv, value, description=''):
        """
        Construct WritePv action.

        Args:
            pv name of PV to write, this can include macros
            value to write
            description to display
        """
        self.pv_name = pv
        self.description = description
        self.value = value
        self.timeout = 10


class ExecuteCommand(object):
    """
    Action that executes a script command in the specified directory.
    """

    OPI_DIR = '$(opi.dir)'
    HOME_DIR = '$(user.home)'

    def __init__(self, command, description, directory=OPI_DIR):
        """
        Construct ExecuteCommand action.

        The directory can be a real path or one of the predefined helper macros:
            OPI_DIR: the directory containing the OPI file
            HOME_DIR: users home directory

        Args:
            command to execute
            description to display
            directory to execute the script
        """
        self.command = command
        self.description = description
        self.command_directory = directory
        self.wait_time = 10


class OpenOpi(object):
    """Action that opens another opi file."""

    REPLACE_CURRENT = 0
    WORKBENCH_TAB = 1
    WORKBENCH_TAB_LEFT = 2
    WORKBENCH_TAB_RIGHT = 3
    WORKBENCH_TAB_TOP = 4
    WORKBENCH_TAB_BOTTOM = 5
    DETACHED_TAB = 6
    NEW_WORKBENCH = 7
    STANDALONE = 8

    def __init__(self, path, mode=STANDALONE):
        """
        Construct OpenOpi action.

        Args:
            path of opi to open
            mode determining how the opi opens
        """
        self.path = path
        self.mode = mode


class Exit(object):
    """Action that closes the current opi."""
