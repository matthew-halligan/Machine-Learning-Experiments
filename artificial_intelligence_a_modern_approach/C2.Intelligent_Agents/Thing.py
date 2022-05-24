class Thing:
    """
    This Represents any physical object that can appear in an Environment.
    Subclass Thing to get the things needed for an environment.  Each Thing
    can have a .__name__ slot (used for output only).
    """

    def __repr__(self):
        return '<{}>'.format(getattr(self, "__name__", self.__class__.__name__))

    def is_alive(self):
        """
        Things that are alive should return True
        :return: boolean
        """
        return hasattr(self, 'alive') and self.alive

    def show_state(self):
        """
        Display the agents internal state.  Subclasses should override.
        :return: None
        """
        print("I don't know how to show state")

    def display(self, canvas, x, y, width, height):
        """
        Display an image of this Thing on the canvas.
        :param canvas: which canvase to display to
        :param x: x value of rectangle
        :param y: y value of rectangle
        :param width: width of image
        :param height: height of image
        :return: None
        """
        pass