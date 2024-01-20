import flet as ft


def main(page: ft.Page): 
    page.theme_mode = "Light"  
    page.title = "Todo App"
    page.window_title = "Todo App"
    page.window_width = 500
    page.window_height = 500
   
    def addTodo(e):
        items = ft.Checkbox(label=text_field.value, value=text_field.value,)
        page.add(items)
        text_field.value = ""
        page.update()
    
    text_field = ft.TextField(autofocus=True,)
    
    btn = ft.FloatingActionButton(icon=ft.icons.ADD, on_click=addTodo)
    page.add(ft.Row([text_field, btn], alignment="spaceEvenly"))
    page.update()

ft.app(main)
