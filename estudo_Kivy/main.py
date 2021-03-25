from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from  kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
import dbtarefa
import sqlite3

class Gerenciador(ScreenManager):
    pass
class Menu(Screen):
    pass
class Caixa(Screen):
    pass
class Contas(Screen):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)

    def on_pre_enter(self):
        Window.bind(on_keyboard = self.voltar)

    def voltar(self,window,key,*args):
        if key == 27:
            App.get_running_app().root.current = 'menu'
            return True

    def on_pre_leave(self):
        Window.unbind(on_keyboard=self.voltar)


    def addTarefa(self):
        texto = self.ids.texto.text

        dbtarefa.create_table()

        dbtarefa.insert_tarefas(texto)
        self.apaga()
        self.mostrarWidget()

    def apaga(self):
        for widget in range(len(self.children)):
            self.remove_widget(self.children[0])

    def mostrarWidget(self, **kwargs):
        self.apaga()
        super().__init__(**kwargs)
        connection = sqlite3.connect('App_caixa.db')
        c = connection.cursor()
        tudo = c.execute("SELECT * FROM tarefas ORDER BY Tarefa").fetchall()
        for t in tudo:
            for i in t:
                self.ids.box.add_widget(Tarefa(text=i))



class Tarefa(BoxLayout):
    def __init__(self,text='',**kwargs):
        super().__init__(**kwargs)
        self.ids.label.text = text
    def apagaWidget(self):
        text = self.ids.label.text
        connection = sqlite3.connect('App_caixa.db')
        c = connection.cursor()
        c.execute(f'DELETE FROM tarefas WHERE Tarefa="{text}"')
        connection.commit()

class Graficos(Screen):
    pass
class Agenda(Screen):
    pass
class Teste(App):
    def build(self):
        return Gerenciador()

Teste().run()
