# Reminders #
# After a new session, you can see project root changes to `virtual_lab` x example
# For active virtual machine `source .virtual_lab/bin/active`
# For deactive `deactivate`
# For list all locale libs `pip list`
# For install a new lib `pip install pandas`
# For cancel terminal auto-init virtual-machine search `Auto Activate Environment` in `Code > Settings`
# To execute files, you can use `Play button` or run with `python3 path/file.py`

import cv2

capture = cv2.VideoCapture(0)
while capture.isOpened():
  ret, frame = capture.read()
  if ret == True:
    cv2.imshow("Some Scam", frame)
    if cv2.waitKey(1) == ord("s"):
      break
  else:
    break
  
capture.release()
cv2.destroyAllWindows()