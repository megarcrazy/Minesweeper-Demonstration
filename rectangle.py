class Rectangle:

    @staticmethod
    def centre_rectangle(rect):
        centre_x, centre_y, width, height = rect
        x = centre_x - width // 2
        y = centre_y - height // 2
        new_rect = (x, y, width, height)
        return new_rect
