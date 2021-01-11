class AdjacentIndexList:

    @staticmethod
    def get_adjacent_index_list(index = 8):
        index_list = (
            (1, 0), (0, 1), (-1, 0), (0, -1),
            (1, 1), (-1, 1), (-1, -1), (1, -1)
        )
        for adjacent in index_list[:index]:
            yield adjacent
