global list_task
list_task = list()
class Task():
    def __init__(self,name_task,description,period,status="Не исполнено"):
        self.name_task=name_task
        self.description=description
        self.period=period
        self.status=status
        list_task.append(self)

    def change_status(self):
        if self.status=="Не исполнено":
            self.status="Исполнено"
            print(f"Задание {self.name_task} исполнено")
            
def list_task_not():
  
   print("Список не исполненных дел")
   print("_________________________")
   for element in list_task:
       if element.status=="Не исполнено":
          print(f"{element.name_task}  -  {element.description} {element.period} ")


task1=Task("По завтракать", "Сварить кофе и сделать бытеры", "с 8 до 9")
task2=Task("Погулять", "Пройти 2 км", "с 9 до 11")
task3=Task("Поработать", "Написать статью", " с 11 до 13")
task4=Task("Обед", "Суп, стейк, чай", "с 13 до 14")
task5=Task("Поработать", "Дополнить, редактировать статью", "с 14 до 17")

task1.change_status()
task2.change_status()

list_task_not()
