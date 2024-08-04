class MyClass:
  static_var = 10  # This is a static variable

  def access_static(self):
    print(MyClass.static_var)  # Accessing static variable through class name

obj = MyClass()
obj.access_static()

print(MyClass.static_var)