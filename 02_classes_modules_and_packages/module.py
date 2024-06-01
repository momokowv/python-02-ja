def function():
    print("Function called!")
    
if __name__ == "__main__":
    print("Module is being run directly")
    function()
else:
    print("Module has been imported")