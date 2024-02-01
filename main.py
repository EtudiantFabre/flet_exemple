import flet as ft

def main(page: ft.Page):
    page.bgcolor= ft.colors.GREY_100
    page.appbar = ft.AppBar(
        title=ft.Text('Flet comparer des nombres')
    )
    page.vertical_alignment = "center"
    page.horizontal_alignment = "center"
    
    first_number = ft.TextField(
        label="Premier nombre",
        width=200,
        keyboard_type = "number"
    )
    second_number = ft.TextField(
        label="Deuxième nombre",
        width=200,
        keyboard_type = ft.KeyboardType.NUMBER
    )
    
    result = ft.Text()    
    
    def comparer_nombre():
        number_one = int(first_number.value)
        number_two = int(second_number.value)
        
        if number_one > number_two:
            result.value = str(number_one) + " est sup à " + str(number_two)
        if number_one < number_two:
            result.value = str(number_one) + " est inférieur à " + str(number_two)
        if number_one == number_two:
            result.value = str(number_one) + " est égal à " + str(number_two)
        page.update()
    
    def verifier_nombre(e):
        if (first_number.value.isdecimal() == False) or (second_number.value.isdecimal() == False):
            result.value = "SVP, Veuillez entrer des entiers."
            page.update()
        else:
            comparer_nombre()
    
    btn = ft.ElevatedButton(text="Comparer", on_click=verifier_nombre)
    
    page.add(
        ft.Column([
            first_number,
            second_number,
            result,
            btn
        ], 
        horizontal_alignment="center"
    ))

ft.app(target=main)
