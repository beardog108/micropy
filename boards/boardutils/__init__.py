from boards import models
def board_exists(board_name):
    return True

def get_list_of_board_names():
    return models.Boards.objects.all()