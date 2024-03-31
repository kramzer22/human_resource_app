class Auth:
  def __init__(self, frames) -> None:
    # windows are display frames and it's value if displayed or not
    self._frames = [frames[0], frames[1]]
    
  def display_frame(self, window):
    for key, value in self.__window.items():
      if key == window:
          value = 'selected'
      else:
        value = 'unselected'