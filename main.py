
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.label import MDLabel
from kivymd.uix.toolbar import MDTopAppBar

class QTcCalculatorApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Red"
        self.theme_cls.theme_style = "Light"

        # Fő elrendezés
        layout = MDBoxLayout(orientation='vertical', spacing="10dp", padding="20dp")

        # Fejléc
        toolbar = MDTopAppBar(title="QTc Kalkulátor")
        layout.add_widget(toolbar)

        # Beviteli mezők
        self.hr_input = MDTextField(hint_text="HR (pulzus)", text="75", input_filter="float")
        self.temp_input = MDTextField(hint_text="Test hőmérséklet (C°)", text="36.5", input_filter="float")
        self.tnt_input = MDTextField(hint_text="hsTnT", text="14.0", input_filter="float")
        self.sek_input = MDTextField(hint_text="SeK (Kálium)", text="4.0", input_filter="float")

        layout.add_widget(self.hr_input)
        layout.add_widget(self.temp_input)
        layout.add_widget(self.tnt_input)
        layout.add_widget(self.sek_input)

        # Számolás gomb
        calc_button = MDRaisedButton(
            text="Kiszámolás",
            pos_hint={"center_x": .5},
            on_release=self.szamol_qtc
        )
        layout.add_widget(calc_button)

        # Eredmény kijelző
        self.result_label = MDLabel(
            text="SZÁMÍTOTT QTc ÉRTÉK: -- ms",
            halign="center",
            font_style="H6"
        )
        layout.add_widget(self.result_label)

        return layout

    def szamol_qtc(self, instance):
        try:
            hr = float(self.hr_input.text)
            temp = float(self.temp_input.text)
            hstnt = float(self.tnt_input.text)
            sek = float(self.sek_input.text)
            
            # A korábban betanított regressziós modell egyenlete:
            qtc = 467.73 - (1.61 * hr) + (1.69 * temp) + (0.013 * hstnt) - (2.09 * sek)
            self.result_label.text = f"SZÁMÍTOTT QTc ÉRTÉK: {qtc:.2f} ms"
        except ValueError:
            self.result_label.text = "Hiba: Kérlek tölts ki minden mezőt!"

if __name__ == '__main__':
    QTcCalculatorApp().run()
