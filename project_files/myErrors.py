# This Python script file simply states a few possibly used errors
# that will occur within the program
class Errors:
  def __init__(self,msg):
    self.msg = msg
  
  def ExceptionError(self):
    raise Exception(self.msg)
    return self.msg
  def OverFlowError_(self):
    raise OverflowError(self.msg)
    return self.msg
  def WarningError(self):
    raise Warning(self.msg)
    return self.msg
  def RuntimeError_(self):
    raise RuntimeError(self.msg)
    return self.msg
  def UserWarning_(self):
    raise UserWarning(self.msg)
    return self.msg
  def InterruptedErrorE(self):
    raise InterruptedError(self.msg)
    return self.msg
  def FutureWarningError(self):
    raise FutureWarning(self.msg)
    return self.msg
  def KeyboardInterruptError(self):
    raise KeyboardInterrupt(self.msg)
    return self.msg

def _err_(type_,msg):

  # Type 1 error msg
  t_1 = Errors(msg)

  # Type 2 error msg
  t_2 = Errors(msg)

  # Type 3 error msg
  t_3 = Errors(msg)

  # Type 4 error msg
  t_4 = Errors(msg)

  # Type 5 error msg
  t_5 = Errors(msg)

  # Type 6 error msg
  t_6 = Errors(msg)

  # Type 7 error msg
  t_7 = Errors(msg)
  
  # Type 8 error msg
  t_8 = Errors(msg)

  if type_ == 1:
    t_1.ExceptionError()
    return "Error type: Exception"
  if type_ == 2:
    t_2.OverFlowError_()
    return "Error type: OverFlow"
  if type_ == 3:
    t_3.WarningError()
    return "Error type: Warning"
  if type_ == 4:
    t_4.RuntimeError_()
    return "Error type: Runtime"
  if type_ == 5:
    t_5.UserWarning_()
    return "Error type: User warning"
  if type_ == 6:
    t_6.InterruptedErrorE()
    return "Error type: InterruptedError"
  if type_ == 7:
    t_7.FutureWarningError()
    return "Error type: FutureWarning"
  if type_ == 8:
    t_8.KeyboardInterruptError()
    return "Error type: KeyboardInterrupt"
  # Useless for the fact that I should know I hard-coded 8 errors, but just in case I forget
  # it will possibly be useful
  else:
    raise Exception("That error was not located. Sorry")
