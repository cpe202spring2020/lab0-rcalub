def convert_weight(weight,conversion):
  return int(weight)*conversion

def weight_on_planets():
  weight = input('What do you weigh on earth? ')
  print('\nOn Mars you would weigh {:.2f} pounds.\nOn Jupiter you would weigh {:.2f} pounds.' \
    .format(convert_weight(weight,0.38),(convert_weight(weight,2.34))))
  
if __name__ == '__main__':
   weight_on_planets()
